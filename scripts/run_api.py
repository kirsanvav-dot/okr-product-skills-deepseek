#!/usr/bin/env python3
"""Run portable Markdown skills via DeepSeek API with a human gate at each stage.
This is a reference wrapper, not a DeepSeek-native skills runtime. Sends input files to API.
"""
import argparse,os,sys
from pathlib import Path
from openai import OpenAI
STAGES=['00-source-intake','01-discovery-questions','02-okr-design','03-cascade-traceability','04-collision-check','05-capacity-and-initiatives','06-audit-and-defense','07-product-roadmap','08-epic-breakdown','09-prd-write-spec','10-agile-story-writer','11-story-splitter','12-backlog-quality-gates']
parser=argparse.ArgumentParser()
parser.add_argument('--source',action='append',required=True,help='Prepared UTF-8 text export; can repeat')
parser.add_argument('--stage',choices=STAGES,default=STAGES[0])
parser.add_argument('--prior',action='append',default=[],help='Human-approved previous stage text')
parser.add_argument('--out',default='output_stage.md')
parser.add_argument('--model',default=os.getenv('DEEPSEEK_MODEL','deepseek-chat'))
parser.add_argument('--confirm-external-upload',action='store_true',help='Confirm source is permitted for remote processing')
a=parser.parse_args()
if not a.confirm_external_upload: raise SystemExit('STOP: add --confirm-external-upload only after corporate privacy/InfoSec approval.')
if not os.getenv('DEEPSEEK_API_KEY'): raise SystemExit('Set DEEPSEEK_API_KEY')
root=Path(__file__).resolve().parents[1]
skill=(root/'skills'/a.stage/'SKILL.md').read_text(encoding='utf-8')
chunks=[]
for name in a.source+a.prior:
    p=Path(name); chunks.append(f'### FILE {p.name}\n'+p.read_text(encoding='utf-8')[:250000])
prompt=('Выполни только текущий этап. Источники могут быть неполны. ' 'Требуй файл/лист/ячейку, не выдумывай метрики. '
        'После ответа остановись для ручного подтверждения.\n\n'+'\n\n'.join(chunks))
client=OpenAI(api_key=os.environ['DEEPSEEK_API_KEY'],base_url=os.getenv('DEEPSEEK_BASE_URL','https://api.deepseek.com'))
ans=client.chat.completions.create(model=a.model,messages=[{'role':'system','content':skill},{'role':'user','content':prompt}])
result=ans.choices[0].message.content or ''
Path(a.out).write_text(result,encoding='utf-8')
print('Saved',a.out,'stage',a.stage,'chars',len(result))

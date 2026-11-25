#!/usr/bin/env python3
"""Structural trace validator. Does NOT validate causality, actual Jira state or effort."""
import argparse,json,sys
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--epics',required=True);p.add_argument('--stories',required=True);a=p.parse_args()
ep=json.loads(Path(a.epics).read_text(encoding='utf8'))['epics']
st=json.loads(Path(a.stories).read_text(encoding='utf8'))['stories']
issues=[]
eids=[e.get('epic_id') for e in ep];sids=[s.get('story_id') for s in st]
if len(set(eids))!=len(eids): issues.append('Duplicate epic_id')
if len(set(sids))!=len(sids): issues.append('Duplicate story_id')
for e in ep:
 for k in ['epic_id','initiative_id','kr_ids','outcome','acceptance_metric','owner','source_refs']:
  if not e.get(k): issues.append(f"Epic {e.get('epic_id')} missing {k}")
for s in st:
 for k in ['story_id','epic_id','initiative_id','kr_ids','acceptance_criteria','negative_cases','source_refs']:
  if not s.get(k): issues.append(f"Story {s.get('story_id')} missing {k}")
 if s.get('epic_id') not in eids: issues.append(f"Orphan story {s.get('story_id')} -> {s.get('epic_id')}")
for e in ep:
 if not any(s.get('epic_id')==e['epic_id'] for s in st): issues.append(f"Epic {e['epic_id']} has no stories")
for i in issues:print('FAIL',i)
if issues:sys.exit(1)
print('STRUCTURE PASS: references and required fields. Causal links, estimates, tests and factual data still require human review.')

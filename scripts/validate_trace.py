#!/usr/bin/env python3
"""Simple, fully local structural validator of a traceability JSON. Not a causal proof."""
import json,sys
from pathlib import Path
VALID={'DIRECT_MEASURED','DIRECT_PENDING','CONTRIBUTORY','HYPOTHESIS','NONE'}
def main():
    if len(sys.argv)<2: raise SystemExit('Usage: python scripts/validate_trace.py file.json')
    d=json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
    objs=d.get('objectives',[]);links=d.get('links',[])
    ids=[x.get('id') for x in objs]; errs=[]
    if len(set(ids))!=len(ids): errs.append('Duplicate objective IDs')
    for i,x in enumerate(links,1):
        for k in ('parent_id','child_id'):
            if x.get(k) not in ids: errs.append(f'link {i} unknown {k}: {x.get(k)}')
        if x.get('grade') not in VALID: errs.append(f'link {i} bad grade')
        if not x.get('mechanism'): errs.append(f'link {i} no mechanism')
        if not x.get('evidence'): errs.append(f'link {i} no evidence statement')
    for obj in objs:
        if obj.get('owner')!='TOP' and not any(x.get('child_id')==obj['id'] for x in links): errs.append(f'orphan {obj["id"]}')
    print(f'objects={len(objs)} links={len(links)} errors={len(errs)}')
    for x in errs: print('ERROR',x)
    sys.exit(bool(errs))
if __name__=='__main__': main()

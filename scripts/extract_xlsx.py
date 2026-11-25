#!/usr/bin/env python3
"""Export workbook values with sheet/cell refs for LLM grounding; does not modify workbook."""
import sys,openpyxl
from pathlib import Path
if len(sys.argv)<2: raise SystemExit('Usage: python scripts/extract_xlsx.py FILE.xlsx [max_chars_per_cell]')
source=Path(sys.argv[1]); cap=int(sys.argv[2]) if len(sys.argv)>2 else 8000
wb=openpyxl.load_workbook(source,read_only=True,data_only=False)
print('SOURCE:',source.name)
for ws in wb:
    print('\n### SHEET:',ws.title)
    for row in ws.iter_rows():
        cells=[]
        for c in row:
            if c.value is not None:
                val=str(c.value).replace('\n',' ⏎ ')
                cells.append(f'{c.coordinate}: {val[:cap]}'+('…[TRUNCATED]' if len(val)>cap else ''))
        if cells: print(' | '.join(cells))

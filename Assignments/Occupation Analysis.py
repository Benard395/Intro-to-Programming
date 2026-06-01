from pathlib import Path
import csv
P = Path(__file__).with_name('occupation-2018-census-csv.csv')
rows = []
with P.open(encoding='utf-8', newline='') as f:
    for r in csv.reader(f):
        if len(r) < 3: continue
        code = r[0].strip().strip('"')
        if not code.isdigit(): continue
        try:
            rows.append((code, r[1].strip().strip('"'), int(r[2].strip().strip('"'))))
        except Exception:
            pass
most = max(rows, key=lambda x: x[2])
least = min(rows, key=lambda x: x[2])
grape = next((x for x in rows if x[1].lower()=='grape grower'), None)
occ14298 = next((x for x in rows if x[2]==14298), None)
code451311 = next((x for x in rows if x[0]=='451311'), None)
top5 = sorted(rows, key=lambda x: x[2], reverse=True)[:5]
print(f"Most common: {most[1]} ({most[2]})")
print(f"Least common: {least[1]} ({least[2]})")
print(f"Grape Growers: {grape[2] if grape else 'not found'}")
print(f"14298 employees: {occ14298[1] if occ14298 else 'not found'}")
print(f"Code 451311: {code451311[1] if code451311 else 'not found'}\n")
print('Top 5:')
for _, o, c in top5:
    print(f"- {o}: {c}")

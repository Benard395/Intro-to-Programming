import csv, os
csv_file = os.path.join(os.path.dirname(__file__), 'faithful (2).csv')
with open(csv_file, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader, None)
    rows = [(float(r[1]), float(r[2])) for r in reader if len(r) >= 3 and r[1].strip() and r[2].strip()]
if not rows:
    print('No valid data found.')
else:
    durations, waits = zip(*rows)
    longest_wait = max(waits)
    print(f'Average eruption length: {sum(durations)/len(durations):.3f} minutes')
    print(f'Longest eruption length: {max(durations):.3f} minutes')
    print(f'Shortest eruption length: {min(durations):.3f} minutes')
    print(f'Average eruption wait: {sum(waits)/len(waits):.3f} minutes')
    print(f'Shortest eruption wait: {min(waits):.0f} minutes')
    print(f'Longest eruption wait: {longest_wait:.0f} minutes')
    print(f'Eruption length at longest wait: {durations[waits.index(longest_wait)]:.3f} minutes')

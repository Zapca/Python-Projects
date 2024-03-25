fname = input("Enter file name: ")
fh = open(fname)

hour_counts = {}

for line in fh:
    if line.startswith("From "):
        words = line.split()
        hour = words[5].split(":")[0]
        hour_counts[hour] = hour_counts.get(hour, 0) + 1

[print(hour, count) for hour, count in sorted(hour_counts.items())]
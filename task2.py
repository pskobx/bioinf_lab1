total_len = 0
gc_count = 0

with open("reads.fastq.txt") as f:
    for i, line in enumerate(f):
        if i % 4 == 1:
            l = line.strip()
            total_len += len(l)
            gc_count += l.count('G') + l.count('C')

print("GC-состав:", round(gc_count / total_len * 100, 2))

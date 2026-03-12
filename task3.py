total_cnt = 0
cnt = 0

with open("reads.fastq.txt") as f:
    for i, line in enumerate(f):
        if i % 4 == 3:
            l = line.strip()
            cnt += ord(l[9]) - 33
            total_cnt += 1
            

print("Phred:", round(cnt / total_cnt))

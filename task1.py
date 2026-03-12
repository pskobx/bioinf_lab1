count = 0
total_len = 0
min_len = 10 ** 18
max_len = 0

with open("reads.fastq.txt") as f:
    for i, line in enumerate(f):
        if i % 4 == 1:
            length = len(line.strip())
            count += 1
            total_len += length

            min_len = min(min_len, length)
            max_len = max(max_len, length)

print("Общее число прочтений:", count)
print("Минимальная длина прочтения:", min_len)
print("Средняя длина прочтения:", round(total_len / count))
print("Максимальная длина прочтения:", max_len)

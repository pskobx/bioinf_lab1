trimmed_strings = 0
filtered_strings = 0
remaining_strings = 0
total_len = 0
min_len = 10 ** 18
max_len = 0

with open("reads.fastq.txt") as f:
    for i, line in enumerate(f):
        if i % 4 == 3:
            qual = line.strip()

            length = len(qual)
            new_length = length

            for j in range(length - 4):
                s = 0
                for k in range(j, j + 5):
                    s += ord(qual[k]) - 33

                if s / 5 < 30:
                    new_length = j
                    break

            if new_length == 0:
                trimmed_strings += 1
            else:
                filtered_strings += 1
                total_len += new_length
                min_len = min(min_len, new_length)
                max_len = max(max_len, new_length)

                if new_length >= 60:
                    remaining_strings += 1

print("Сколько прочтений подверглось триммингу:", trimmed_strings)
print("Минимальная длина равна:", min_len)
print("Средняя длина равна:", round(total_len / filtered_strings))
print("Максимальная длина равна:", max_len)
print("Оставшееся число прочтений:", remaining_strings)

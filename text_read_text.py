t1 = "zh-text.txt"
t2 = "en-text.txt"
t1_l = []
with open(t1, "r", encoding="utf-8") as f:
    zh = f.readlines()
    for row in zh:
        t1_l.append(row.strip())
t2_l = []
with open(t2, "r", encoding="utf-8") as f:
    en = f.readlines()
    for row in en:
        t2_l.append(row.strip())
print(len(t1_l))
for row in t1_l:
    print(row)
print(len(t2_l))
for row in t2_l:
    print(row)

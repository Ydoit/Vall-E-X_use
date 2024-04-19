import os


for i in range(1, 11):
    if not os.path.exists(f"en/speaker{i}"):
        os.mkdir(f"en/speaker{i}")
for i in range(1, 11):
    if not os.path.exists(f"zh/speaker{i}"):
        os.mkdir(f"zh/speaker{i}")

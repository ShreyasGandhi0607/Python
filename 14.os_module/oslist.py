import os

# for i in range(0,10):
#     os.mkdir(f"data/Day{i+1}")
folders = os.listdir("data")

print(folders)
# + id="9023581f" outputId="46e

for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))
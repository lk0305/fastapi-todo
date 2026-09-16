import os

with open("1.txt",mode="r",encoding="utf-8") as f1, \
    open("2.txt",mode="w",encoding="utf-8") as f2:
        for line in f1:
            line = line.strip()
            if line.startswith("周"):
                line = line.replace("周","张")
            f2.write(line)
            f2.write("\n")
os.remove("1.txt")
os.rename("2.txt","1.txt")


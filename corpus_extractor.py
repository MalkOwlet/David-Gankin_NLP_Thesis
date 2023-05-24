import os
import csv

path = "C:/Users/asus/Desktop/ВУЗ/Курсовая/Тексты"
os.chdir(path)
try:
    os.mkdir("annotated")
except FileExistsError:
    pass

ann_path = path + "/annotated/"

final = open(path + "/final.csv", "w")
fr = csv.writer(final, quoting=csv.QUOTE_ALL)
fr.writerow(["FILE", "SENTENCE", "ERROR", "CORRECTION"])

for files in os.listdir(path):
    if files.endswith(".ann"):
        data = dict()
        file = open(files, "r")
        text = file.readlines()
        file.close()

        file_essay = open(files[:-3] + "txt", "r")
        essay = file_essay.read()
        sentence_array = essay.split(".")
        file_essay.close()

        tag = "Absence_comp_sent"
        token_num = None
        for line in text:
            if line[0] == "T":
                if tag in line:
                    seg = line.split("\t")
                    data[seg[0]] = [None, None, None]
                    data[seg[0]][1] = seg[-1][:-1]
                    for s in sentence_array:
                        if seg[-1][:-1] in s:
                            data[seg[0]][0] = s
            elif line[0] == "#":
                seg = line.split("\t")
                num = seg[1].split()[-1]
                if num in data:
                    data[num][2] = seg[-1][:-1]
        for key, value in data.items():
            fr.writerow([files] + value)

final.close()

import pandas as pd
import json

df = pd.read_table("TrainDataSet.tsv", sep="\t")
#df = pd.read_table("DevDataSet.tsv", sep="\t")
data = []
for i in range(len(df)):
    try:
        if int(df.loc[i][4]) == 1:
            if df.loc[i][2].find(df.loc[i][1]) == df.loc[i][2].rfind(df.loc[i][1]):
                l1 = []
                l2 = []
                l3 = []
                l1.append(df.loc[i][1])
                l2.append(df.loc[i][1].find(df.loc[i][1]))
                l2.append(df.loc[i][1].find(df.loc[i][1]) + len(df.loc[i][1]))
                l2.append("ABSENCE OF A NECESSARY COMPONENT")
                l3.append(l2)
                dic = {"entities": l3}
                l1.append(l2)
                data.append(dic)
        if int(df.loc[i][4]) == 0:
            if int(df.loc[i][6]) != 0:
                if df.loc[i][6].find(df.loc[i][1]) == df.loc[i][6].rfind(df.loc[i][1]):
                    l1 = []
                    l2 = []
                    l3 = []
                    l1.append(df.loc[i][6])
                    l2.append(df.loc[i][6].find(df.loc[i][1]))
                    l2.append(df.loc[i][6].find(df.loc[i][1]) + len(df.loc[i][1]))
                    l2.append("ABSENCE OF A NECESSARY COMPONENT")
                    l3.append(l2)
                    dic = {"entities": l3}
                    l1.append(l2)
    except:
        pass

with open("TrainDataSet.json", "w") as output:
#with open("DevDataSet.json", "w") as output:
    output.write(json.dumps(data))
import pandas as pd
import sys
import os.path

args = sys.argv
root, ext = os.path.splitext(args[1])

df_tsv = pd.read_table(args[1]).fillna('データ無し').replace("'", "''", regex=True)
table_name = root
column_num = len(df_tsv.columns.values.tolist())

print('USE sample01;')

labels = ""
i = 0
for label in df_tsv.columns.values.tolist():
    if i == 0:
        labels += '`'
    if not i == column_num-1:
        labels += label + '`, `'
    else:
        labels += label + '`'
    i+=1

for index, row in df_tsv.iterrows():

    values = ""
    for i in range(column_num):
        if i == 0:
            values += "'"
        if not i == column_num-1:
            values += str(row[i]) + "','"
        else:
            values += str(row[i]) + "'"
        i+=1

    line = 'INSERT INTO ' + table_name + '(' + labels + ')' + " VALUES (" + values + ");"
    print(line)
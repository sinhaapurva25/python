# For Private Placement
import pandas as pd

with open(r'Topics-Practiced\mergeCSVCols_privatePlacement.csv_123', 'r') as fl:
    f = fl.readlines()
numberOfLines = len(f)

res = ''
count = 0
lineToRemove = []
detailLineIndex = None
for i in range(numberOfLines):
    if f[i].strip() == '':
        count += 1
    if count == 2:
        lineToRemove = [i, i+1]
        break

f = f[:lineToRemove[0]]+f[lineToRemove[1]+1:]
sep = [i for i in range(len(f)) if f[i].strip() == ''][0]

def arr2DToCSV(arr2D):
    arr2DColumns = arr2D[0]
    df_arr2D = pd.DataFrame(columns=arr2DColumns)

    arr2D = arr2D[1:]

    for i in arr2D:
        df_arr2D.loc[len(df_arr2D)] = i

    return df_arr2D

header = [i.strip('\n').rstrip(',').split(',') for i in f[:sep]]
df_arr2D = arr2DToCSV(header)
df_arr2D.to_csv(r"Topics-Practiced\mergeCSVCols_privatePlacementheader.csv_123.csv",index=False)

details = [i.strip('\n').rstrip(',').split(',') for i in f[sep+1:]]
df_arr2D = arr2DToCSV(details)
df_arr2D.to_csv(r"Topics-Practiced\mergeCSVCols_privatePlacementdetails.csv_123.csv",index=False)

# header = [i.strip('\n').rstrip(',').split(',') for i in f[:sep]]

# headerColumns = header[0]
# df_header = pd.DataFrame(columns=headerColumns)

# header = header[1:]

# for i in header:
#     df_header.loc[len(df_header)] = i

# df_header.to_csv(r"Topics-Practiced\mergeCSVCols_privatePlacementHeader.csv_123.csv",index=False)
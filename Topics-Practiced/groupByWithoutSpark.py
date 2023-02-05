import pandas as pd

f = pd.read_csv(r'groupByWithoutSpark.csv')

res = f.groupby(['state','city']).groups

for k in res:
    print(f"{k[0]},{k[1]},{sorted([f['temp'][j] for j in res[k]])}")
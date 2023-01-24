import pandas as pd

with open(r'data.json') as k:
  df = pd.read_json('data.json')
print(df)
# print("before",df.head(10))

x = df.Calories.mean()#df["Calories"].mean()
df["Calories"].fillna(x, inplace = True)
# print("after",df.head(10))

# df = pd.read_csv('pandas_practice.csv')
# print(df.loc[9999].Gender)

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
myvar = pd.DataFrame(mydataset)
print(myvar)
import pandas as pd

certificates_earned = pd.Series([8, 2, 5, 6],index=['Tom', 'Kris', 'Ahmad', 'Beau'])
print("Pandas","\n",certificates_earned[certificates_earned > 5])

a=[[39, 28]]
b=[[38, 29]]
print(a[0][0])
print(a[0][0])


mydataset = {
  'cars': [],
  'passings': []
}
myvar = pd.DataFrame(mydataset)
# myvar = pd.DataFrame([[0, 1,2,3,4,5],[6,7,8,9,10,11]],index=['a','b'],columns=['q','w','e','r','t','y'])
print(myvar)
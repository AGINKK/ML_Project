import pandas as pd

name = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Evan'],
    'Age': [25, 32, 45, 28, 22],
    'class':['Mca','Bcom','Mcom',]
}

df=pd.DataFrame(name)
print(df)
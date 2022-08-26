import pandas as pd

# Creating Pandas Data Frame using list of dicts.

sals_ld = [
    {'id': 1, 'sal': 1500.0},
    {'id': 2, 'sal': 2000.0, 'comm': 10.0},
    {'id': 3, 'sal': 2200.0, 'active': False}
]

# Create data frame

sals_df = pd.DataFrame(sals_ld)
print(sals_df)

# Getting number of records and columns.
print(sals_df.count())
print(sals_df.count()['id'])

# getting data type of colm

print(sals_df.dtypes)

# replacing NaN values in colm by using fillna

print(sals_df.fillna(0.0))

# replacing NaN values in a perticular column
print(sals_df.fillna({'comm':0.0}))

#We can also drop multiple columns by passing column names as list.
print(sals_df.drop(columns=['comm', 'active']))
print(sals_df.drop(['comm', 'active'], axis=1))

#priny data in ascending or decending order
print(sals_df.sort_index(ascending=False))
print(sals_df.sort_index(ascending=True))
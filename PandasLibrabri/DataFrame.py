import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
#load data into a DataFrame object:

df=pd.DataFrame(data)
print(df)

# Creating Pandas Data Frame using list of tuples.
sals_ld = [(1, 1500.0), (2, 2000.0, 10.0), (3, 2200.00)]
sals_df = pd.DataFrame(sals_ld)
print(sals_df)

#assign colm name
sals_df = pd.DataFrame(sals_ld, columns=['id', 'sal', 'comm'])
print(sals_df)

#print specific colm

print(sals_df['id'])
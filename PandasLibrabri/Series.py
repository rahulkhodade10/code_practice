import pandas as pd

a = [1, 7, 2, 6, 8]
myvar = pd.Series(a)
print(myvar)

# Labels: If nothing else is specified, the values are labeled with their index number. First value has index 0,
# second value has index 1 etc.

myvar = pd.Series(a, index=['a', 'b', 'c', 'd', 'e'])
print(myvar)

# Dict as series
d = {"JAN": 10, "FEB": 15, "MAR": 12, "APR": 16}
s=pd.Series(d)
print(s)
print(s.sum())
print(s[0])

##Local path


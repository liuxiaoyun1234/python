
from __future__ import print_function
import pandas as pd
import numpy as np


s = pd.Series([12 ,23 ,np.nan ,45] ,index=['a' ,'b' ,'c' ,'d'])

print(s)

dates = pd.date_range('20190526' ,periods=6 ,freq='Y')
print(dates)

# print(np.random.randn(6,4))

df = pd.DataFrame(np.random.randn(6 ,4) ,index=dates ,columns=['A' ,'B' ,'C' ,'D'])

print(df)
rdate = range(4)
print(rdate)

df2 = pd.DataFrame({'A':1.0,
                    'B':pd.Timestamp('20190304'),
                    'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D':np.array([3]*4,dtype='int32'),
                    'E':pd.Categorical(['test','train','test','train']),
                    'F':'foo'})

print(df2)

print(df2.dtypes)
print('=============================')
print(df2.index)
print(df2.columns)
print(df2.values)
print('#############################')
print(df2.describe())
print(df2.T)
print(df2.sort_index(axis=1,ascending=False))
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
print(df2.sort_values(by='B'))
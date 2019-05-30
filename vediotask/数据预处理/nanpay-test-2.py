from __future__ import print_function
import pandas as pd
import numpy as np

dates = pd.date_range('20130101',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index = dates,columns=['A','B','C','D'])
print(df)
df.iloc[0,1]=np.nan
df.iloc[1,2]=np.nan
print(df)
print(df.dropna(axis=0,how='any'))
print(df.fillna(value='asd'))
print(pd.isnull(df))

left = pd.DataFrame({'key':['K0','K1','K2','K3'],'A':['A0','A1','A2','A3'],'B':['B0','B1','B2','B3']})
print(left)
right = pd.DataFrame({'key':['K0','K1','K2','K3'],'C':['C0','C1','C2','C3'],'D':['D0','D1','D2','D3']})
print(right)
res = pd.merge(left,right,how='inner',on='key')
print(res)

df1 =  pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
print(df1)
df2 =  pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
print(df2)
df3 =  pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])
print(df3)
res = pd.concat([df1,df2,df3],axis=0,ignore_index=True)
print(res)
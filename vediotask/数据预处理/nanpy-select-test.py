
from __future__ import print_function

import numpy as np
import pandas as pd

dates = pd.date_range('20190526' ,periods=6 )

df = pd.DataFrame(np.random.randn(6 ,4) ,index=dates ,columns=['A' ,'B' ,'C' ,'D'])

print(df)
print('#############')
print(df.A)
print('111')
print(df['A'])
print('222')
print(df[0:3])
print('333')
print(df['20190528':'20190530'])
print('444')
print(df.loc['20190528'])
print('555')
print(df.loc[:,['A','B']])
print('666')
print(df.loc['20190528',['A','B']])
print('777')
print(df)
print('888')
print(df.iloc[3])
print('999')
print(df.iloc[3,1])
print('00000')
print(df.iloc[3:5,0:2])
print('11111')
print(df.iloc[[1,2,3],[1,2]])
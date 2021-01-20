import pandas as pd
import random
import numpy as np
a=np.random.randn(10)


# print(s)
df=pd.DataFrame(a,columns=["A"])
df["B"]=df["A"]*100
print(df['B'].min())
print(df)
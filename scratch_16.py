import numpy as np
import datetime as date
import pandas as pd
#df=pd.read_csv('/Users/yashjain/Desktop/Cars93_miss.csv')
df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))

def fu(x,y):
    a=
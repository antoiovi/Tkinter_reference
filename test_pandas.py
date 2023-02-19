import pandas as pd

f="data/xxxxxcsv"
df=pd.read_csv(f,sep=';',decimal='.')
df.columns
df.dtypes
x=df.iloc[:,[0,4,6,9,10]]
x.columns
x.columns=['date','station','sensor','value','state']
x
x['sensor'].unique()
x['station']="STATION_A"
x
def renamesensor(s):
    if "NO2" in s:
        return "NO2"
    elif "NOx" in s:
        return "NOx"
    elif "NO" in s:
      return "NO"
    elif "O3" in s:
      return "O3"
      
      
x.loc[:,('sensor')]=x['sensor'].apply(lambda x: renamesensor(x))

x['state']=x['state'].apply(lambda x: x if x=='V' else 'N')

x['state'].unique()


f2="data/yyyy.csv"
df=pd.read_csv(f2,sep=';',decimal='.')
df.columns
df.dtypes
y=df.iloc[:,[0,4,6,9,10]]
y.columns
y.columns=['date','station','sensor','value','state']
y
y['sensor'].unique()
y.loc[:,'station']="STATION_B"
y

      
y.loc[:,('sensor')]=y['sensor'].apply(lambda k: renamesensor(k))

y['state']=y['state'].apply(lambda k: k if k=='V' else 'N')

y['state'].unique()

df=pd.concat([x,y])
df
df.reset_index(inplace=True)
df.columns=['date','hour','station','sensor','value','state']
df
df.to_csv("data/enviromental.csv", index=False )


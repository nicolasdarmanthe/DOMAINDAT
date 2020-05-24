import pandas as pd
from subInfo_extractor import *

juicy_tbl = get_suburb_info(state = 'ACT', suburb='Braddon', postcode=2612, property_type='unit',room_num=1)

for i in juicy_tbl['series']['seriesInfo']: 
    print("Year:", i['year']) 
    print("Month:", i['month'])
    for j in i['values']:
        print(str(j), i['values'][str(j)])

df_master = pd.DataFrame()
for i in range(1,len(juicy_tbl['series']['seriesInfo'])):
    df = pd.DataFrame.from_dict(juicy_tbl['series']['seriesInfo'][i])
    df_master = df_master.append(df)

df_master.to_csv('C:\\Users\\nicol\\OneDrive\\Documents\\DOMAIN_PROJ\\DOMAINDAT\\data.csv')

print("Type:", type(df['values'])) 
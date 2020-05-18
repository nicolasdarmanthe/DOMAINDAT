import pandas as pd
from subInfo_extractor import *

juicy_tbl = get_suburb_info(state = 'ACT', suburb='Braddon', postcode=2612, property_type='unit',room_num=1)

for i in juicy_tbl['series']['seriesInfo']: 
    print("Year:", i['year']) 
    print("Month:", i['month'])
    for j in i['values']:
        print(str(j), i['values'][str(j)])

df = pd.DataFrame(test, columns = ['year','month','values'])

df['ID'] = df.index
pd.wide_to_long(df, ['median Sold Price','number Sold','highest sold price', 'lowest sold price','5thpcntle','25th pcntle',
    '75th pcntle','95th pcntle',"medianSaleListingPrice", "numberSaleListing", "highestSaleListingPrice", 
    "lowestSaleListingPrice", "auctionNumberAuctioned", "auctionNumberSold", "auctionNumberWithdrawn", 
    "daysOnMarket", "discountPercentage", "medianRentListingPrice", "numberRentListing", "highestRentListingPrice", "lowestRentListingPrice"], 
    i=['year'], j='month')

print("Type:", type(df['values'])) 

#todo
#find better way of indexing into subinfo tbl
#find how to parse json object and export to csv
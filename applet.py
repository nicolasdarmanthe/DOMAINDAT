from subInfo_extractor import *

print('State?')
state = input()
print('Suburb?')
suburb = input()
print('postcode?')
postcode = input()
print('Type of property? Options are unit or house')
property_type=input()
print('Number of rooms?')
room_num=input()
print('CSV file name?')
fname = input()

get_suburb_info(state, suburb, postcode,property_type, room_num,fname)

print('That\'s it! Your file was saved as '+fname+'.csv')
input()
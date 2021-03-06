def get_suburb_info(state = 'ACT', suburb='Braddon', postcode=2612, property_type='house',room_num=3, fname='data'):

    import requests
    import json

    #Global
    client_id = 'client_8cc4467817e24eda06ff64feb271fd10'
    client_secret = 'secret_f00582474fc0391e4f587d074810d365'
    auth_url = 'https://auth.domain.com.au/v1/connect/token'
    
    #--------------------Get suburbID using AdressLocators API-------------------

    scopes = ['api_addresslocators_read']
    url_endpoint = 'https://api.domain.com.au/v1/addressLocators'
    #search_level = '?searchLevel=Address&streetNumber=100'
    #street_name = '&streetName=Harris&streetType=Street'
    search_level = '?searchLevel=Suburb'
    thesub = '&suburb='+suburb
    thestate = '&state='+state
    thepostcde = '&postcode='+str(postcode)

    response = requests.post(auth_url, data = {
        'client_id':client_id,
        'client_secret':client_secret,
        'grant_type':'client_credentials',
        'scope':scopes,
        'Content-Type':'text/json'
        })
    json_res = response.json()
    access_token=json_res['access_token']
    print(access_token)
    auth = {'Authorization':'Bearer ' + access_token}
    #url = url_endpoint + search_level + street_name + suburb
    url = url_endpoint + search_level + thesub + thestate + thepostcde
    res1 = requests.get(url, headers=auth)    
    subinfo_tbl = res1.json()
    #extract SuburbID from above
    subID = subinfo_tbl[0]['ids'][0]['id']

    #--------------------Using suburbID, extract suburb performance data-------------------

    scopes = ['api_suburbperformance_read']
    url_endpoint = 'https://api.domain.com.au/v1/suburbPerformanceStatistics'
    thestate = '?state='+state #not sure if necessary to make lower case
    suburbID = '&suburbId='+ str(subID)
    propCatgry = '&propertyCategory='+property_type
    binsize = '&chronologicalSpan=3' #in months. No better time res unfortunately.
    binstart =  '&tPlusFrom=1'
    binend = '&tPlusTo=60'
    bednum = '&bedrooms='+str(room_num)
    # &values=HighestSoldPrice%2CLowestSoldPrice #use comma (%2C) to separate arguments
    response = requests.post(auth_url, data = {
        'client_id':client_id,
        'client_secret':client_secret,
        'grant_type':'client_credentials',
        'scope':scopes,
        'Content-Type':'text/json'
        })
    json_res = response.json()
    access_token=json_res['access_token']
    print(access_token)
    auth = {'Authorization':'Bearer ' + access_token}
    url = url_endpoint + thestate + suburbID + propCatgry + binsize + binstart + binend +bednum
    res1 = requests.get(url, headers=auth)    
    juicy_tbl = res1.json()

    import pandas as pd
    df_master = pd.DataFrame()
    for i in range(1,len(juicy_tbl['series']['seriesInfo'])):
        df = pd.DataFrame.from_dict(juicy_tbl['series']['seriesInfo'][i])
        df_master = df_master.append(df)

    df_master.to_csv('.\\'+fname+'.csv')
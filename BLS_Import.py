import requests
import json
import pandas as pd

#Importing data from bls
headers = {'Content-type': 'application/json'}
data = json.dumps({"seriesid": ['WMU00311401020000004721112500','WMU00311401020000004720312500', 'WMU00311401020000001190212400','WMU00311401020000004990212500','OEUM003114000000033202103','OEUM003114000000047202103',
                                'OEUM003114000000047214103','OEUM003114000000047218103','WMU00311401020000004721522500','WMU00311401020000005330322500','OEUM003114000000051412203','OEUM003114000000047208103','OEUM003114000000047222103',
                                'WMU003114010200000047203125A2','WMU003114010200000047203125A3','WMU003114010200000049902125A3','WMU003114010200000047101100A1','WMU003114010200000047211100A3',
                                'WMU003114010200000051412100A1','WMU003114010200000053303200A1','WMU003114010200000051412125A2',
                                'WMU003114010200000053303225A3','WMU003114010200000047215225A3'

],"startyear":"2023", "endyear":"2023","registrationkey":"b4092c7d5bba47da86e46675db19bfa3"})
p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=data, headers=headers)
json_data = json.loads(p.text)

#Iterating through json and grabbing information from each
data_list = []
for series in json_data['Results']['series']:
    series_id = series['seriesID']
    for entry in series['data']:
        data_list.append({
            'Trade': series_id,
            'year': entry['year'],
            'periodName': entry['periodName'],
            'wage': float(entry['value'])  # Convert value to float
        })
# Create DataFrame
df = pd.DataFrame(data_list)

#Rename files imports by trade
df.loc[df.Trade == 'WMU00311401020000004721112500', 'Trade'] = 'Electrician'
df.loc[df.Trade == 'WMU00311401020000004720312500', 'Trade'] = 'Carpenter'
df.loc[df.Trade == 'WMU00311401020000001190212400', 'Trade'] = 'Construction Manager'
df.loc[df.Trade == 'WMU00311401020000004990212500', 'Trade'] = 'HVAC'
df.loc[df.Trade == 'OEUM003114000000033202103', 'Trade'] = 'Fire Inspector'
df.loc[df.Trade == 'OEUM003114000000047202103', 'Trade'] = 'Brickmason'
df.loc[df.Trade == 'OEUM003114000000047214103', 'Trade'] = 'Painter'
df.loc[df.Trade == 'OEUM003114000000047218103', 'Trade'] = 'Roofer'
df.loc[df.Trade == 'WMU00311401020000004721522500', 'Trade'] = 'Plumber'
df.loc[df.Trade == 'WMU00311401020000005330322500', 'Trade'] = 'Trucker'
df.loc[df.Trade == 'OEUM003114000000051412203', 'Trade'] = 'Welder'
df.loc[df.Trade == 'OEUM003114000000047208103', 'Trade'] = 'Drywall'
df.loc[df.Trade == 'OEUM003114000000047222103', 'Trade'] = 'Steel Worker'
#Above is each trade's average hourly rate for a full time tradesman

df.loc[df.Trade == 'WMU003114010200000047203125A2', 'Trade'] = 'Intermediate Carpenter'
df.loc[df.Trade == 'WMU003114010200000047203125A3', 'Trade'] = 'Experiecned Capenter'
df.loc[df.Trade == 'WMU003114010200000049902125A3', 'Trade'] = 'Experienced HVAC'
df.loc[df.Trade == 'WMU003114010200000047101100A1', 'Trade'] = 'Entry Level HVAC'
df.loc[df.Trade == 'WMU003114010200000047211100A3', 'Trade'] = 'Experienced Electrician'
df.loc[df.Trade == 'WMU003114010200000051412100A1', 'Trade'] = 'Entry Level Welder'
df.loc[df.Trade == 'WMU003114010200000053303200A1', 'Trade'] = 'Entry Level Trucker'
df.loc[df.Trade == 'WMU003114010200000051412125A2', 'Trade'] = 'Intermediate Welder'
df.loc[df.Trade == 'WMU003114010200000053303225A3', 'Trade'] = 'Experienced Trucker'
df.loc[df.Trade == 'WMU003114010200000047215225A3', 'Trade'] = 'Experienced Plumber'
#Above is each trade's average hourly rate for a full time tradesman sorted by experience level where possible


# Display DataFrame
print(df)
import requests
import json
import pandas as pd

headers = {'Content-type': 'application/json'}
data = json.dumps({"seriesid": ['WMU00311401020000004720312500','WMU00311401020000004721112500', 'WMU00311401020000001190212400','WMU00311401020000002911412500','WMU00311401020000004990212500','OEUM003114000000033202103',
                                'OEUM003114000000047202103','OEUM003114000000047214103','OEUM003114000000047218103','OEUM003114000000047401103','WMU00311401020000004721522500','WMU00311401020000005330322500','OEUM003114000000051412203'
],"startyear":"2023", "endyear":"2023","registrationkey":"b4092c7d5bba47da86e46675db19bfa3"})
p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=data, headers=headers)
json_data = json.loads(p.text)

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
df.loc[df.Trade == 'WMU00311401020000002911412500', 'Trade'] = 'Registered Nurse'
df.loc[df.Trade == 'WMU00311401020000004990212500', 'Trade'] = 'HVAC'
df.loc[df.Trade == 'OEUM003114000000033202103', 'Trade'] = 'Fire Inspector'
df.loc[df.Trade == 'OEUM003114000000047202103', 'Trade'] = 'Brickmason'
df.loc[df.Trade == 'OEUM003114000000047214103', 'Trade'] = 'Painter'
df.loc[df.Trade == 'OEUM003114000000047218103', 'Trade'] = 'Roofer'
df.loc[df.Trade == 'OEUM003114000000047401103', 'Trade'] = 'Building Inspector'
df.loc[df.Trade == 'WMU00311401020000004721522500', 'Trade'] = 'Plumber'
df.loc[df.Trade == 'WMU00311401020000005330322500', 'Trade'] = 'Trucker'
df.loc[df.Trade == 'OEUM003114000000051412203', 'Trade'] = 'Welding'


# Display DataFrame
print(df)
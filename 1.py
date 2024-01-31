import pandas as pd
import time
import numpy as np
from test import transform, regeocode
# print(regeocode(117.125531,36.19890319))

df = pd.read_excel('stage_info2.xlsx')
#
# lon_adjusted = []
# lat_adjusted = []
# provinces = []
# citys = []
# districts = []
# adcodes = []
# for index, row in df.iterrows():
#     print(index)
#     lon = row['lng']
#     lat = row['lat']
#     try:
#         lon, lat = transform(lon,lat)
#         lon_adjusted.append(lon)
#         lat_adjusted.append(lat)
#     except:
#         lon, lat = '', ''
#         lon_adjusted.append(lon)
#         lat_adjusted.append(lat)
#         continue
#     # print(lon,lat)
#     try:
#         province, city, district, adcode = regeocode(lon, lat)
#         provinces.append(province)
#         citys.append(city)
#         districts.append(district)
#         adcodes.append(adcode)
#     except:
#         province, city, district, adcode = '','','',''
#         provinces.append(province)
#         citys.append(city)
#         districts.append(district)
#         adcodes.append(adcode)
#         continue
#
# df['lon_adjusted'] = lon_adjusted
# df['lat_adjusted'] = lat_adjusted
# df['province'] = provinces
# df['city'] = citys
# df['district'] = districts
# df['adcode'] = adcodes
# df.to_csv('stage_info2_adjusted.csv')

df = pd.read_excel('stage_info5.xlsx')

lon_adjusted = []
lat_adjusted = []
provinces = []
citys = []
districts = []
adcodes = []
for index, row in df.iterrows():
    print(index)
    lon = row['lng']
    lat = row['lat']
    try:
        lon, lat = transform(lon,lat)
        lon_adjusted.append(lon)
        lat_adjusted.append(lat)
    except:
        lon, lat = '', ''
        lon_adjusted.append(lon)
        lat_adjusted.append(lat)
        continue
    # print(lon,lat)
    try:
        province, city, district, adcode = regeocode(lon, lat)
        provinces.append(province)
        citys.append(city)
        districts.append(district)
        adcodes.append(adcode)
    except:
        province, city, district, adcode = '','','',''
        provinces.append(province)
        citys.append(city)
        districts.append(district)
        adcodes.append(adcode)
        continue

df['lon_adjusted'] = lon_adjusted
df['lat_adjusted'] = lat_adjusted
df['province'] = provinces
df['city'] = citys
df['district'] = districts
df['adcode'] = adcodes
df.to_csv('stage_info5_adjusted.csv')
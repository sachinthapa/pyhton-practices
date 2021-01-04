import pandas as pd

climate_temp = pd.read_csv("climate_temp.csv")
climate_precip = pd.read_csv("climate_precip.csv")

# print(climate_temp.head())
print('climate_temp -> ', climate_temp.shape)
# print(climate_precip.head())
# print(climate_precip.shape)

precip_one_station = climate_precip[climate_precip["STATION"]
                                    == "GHCND:USC00045721"]
# print(precip_one_station.head())
print('precip_one_station -> ', precip_one_station.shape)

inner_merge = pd.merge(
    precip_one_station, climate_temp, on=[
        'STATION', 'DATE'])
print('inner_merge -> ', inner_merge.shape)

outer_merge = pd.merge(precip_one_station, climate_temp,
                       how='outer', on=['STATION', 'DATE'])
print('outer_merge -> ', outer_merge.shape)

left_merged = pd.merge(climate_temp, precip_one_station,
                       how="left", on=["STATION", "DATE"])
print('left_merged -> ', left_merged.shape)

right_merged = pd.merge(
    climate_temp, precip_one_station, how="right", on=[
        "STATION", "DATE"])
print('right_merged -> ', right_merged.shape)
#print('precip_one_station', precip_one_station.columns)
#print('right_merged -> ',right_merged.columns)
#print('climate_temp -> ',climate_temp.columns)

left_join = precip_one_station.join(
    climate_temp, lsuffix="_left", rsuffix="_right")

inner_merged_total = pd.merge(
    climate_temp, climate_precip, on=[
        "STATION", "DATE"])
inner_joined_total = climate_temp.join(climate_precip.set_index(
    ["STATION", "DATE"]), lsuffix="_x", rsuffix="_y", on=["STATION", "DATE"])

#print(inner_merged_total.head())
#print(inner_joined_total.head())

reindexed = pd.concat([climate_precip,climate_temp], ignore_index=True)
print(reindexed)



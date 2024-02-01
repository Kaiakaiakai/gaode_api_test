import pandas as pd
import requests


if __name__ == '__main__':
    df = pd.read_csv('stage_info5_adjusted.csv')
    response = []
    success = []
    msgs = []
    for index, row in df.iterrows():
        print(index)
        partnerId = row['stage_code']
        opentime = row['营业时间']
        name = row['stage_name']
        address = row['address']
        telephone = row['master_phone']
        lon = row['lon_adjusted']
        lat = row['lat_adjusted']
        pic = '' if isinstance(row['oss_file_url'], float) else row['oss_file_url']
        province = row['province']
        city = row['city']
        district = row['district']
        adcode = row['adcode']


        url = 'https://api-ggc.amap.com/openapi/data/createOrderApi'
        data = {
            "key": "03895162f2fd8277a57100e089aadf52", #调用方 token
            "channel": "73OWJT", #调用方标识
            "companyId": "628090", #公司 id,限定数据写入哪个账号。
            "groupId": "9442", #分组 id,限定数据写入哪个账号。
            "brandId": "5633", #品牌 id，限定数据写入哪个品牌。
            "partnerId": partnerId, #合作方唯一 id，接入方标记数据的唯一 id，后续修改数据的将继承此 id 执行。
            "status": "1", #地点是否已经关闭。
            "building": "0", #地点当前的营业状态。
            "name": name, #地点在地图上的展示名称。
            "province": province, #地点所在省份。
            "city": city, #地点所在城市。
            "district": district, #地点所在区县。
            "adcode": adcode, #地点所在区县的地理编码。
            "address": address, #地点在地图上的展示地址。
            "lon": lon, #地点在地图上的展示经度。精确到六位小数以上。
            "lat": lat, #地点在地图上的展示纬度。精确到六位小数以上。
            "telephone": str(telephone), #地点在地图上的展示电话号码。
            "categoryName": "生活服务;生活服务场所;生活服务场所", #地点的经营类型。爱心驿站地点可统一赋值："生活服务;生活服务场所;生活服务场所"
            "opentime": opentime, #地点对应的营业时间。
            "pic": pic
        }
        print(data)
        try:
            res = requests.post(url=url, json=data).json()
            response.append(res)
            success.append(res["success"])
            msgs.append(res['msg'])
        except:
            response.append({})
            success.append(False)
            msgs.append('')
            continue
        print(index, res)


        # break
    df['res'] = response
    df['success'] = success
    df['msg'] = msgs
    df.to_csv('stage_result_5.csv')
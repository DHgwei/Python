import json
import requests
import csv
from urllib.parse import quote


f = open('read1.csv',mode='w',encoding='utf-8-sig',newline='')
csv_writer = csv.DictWriter(f,fieldnames=[
    '昵称',
    '内容',
])
csv_writer.writeheader()


headers = {

    "cookie":"buvid3=18D82174-863A-DB0C-E743-60873A55500815277infoc; b_nut=1736494215; _uuid=C23D2BE5-1D23-D867-22EA-A4155E623B9714948infoc; enable_web_push=DISABLE; buvid4=4CF62208-3A91-DF3D-CFF9-378C19AD511215991-025011007-L1%2FU%2B1SlTOR50HPiFRf6mQ%3D%3D; rpdid=|(k||lkJ)JJl0J'u~JYRmRkm~; header_theme_version=CLOSE; hit-dyn-v2=1; LIVE_BUVID=AUTO4917365083288553; is-2022-channel=1; buvid_fp_plain=undefined; PVID=2; enable_feed_channel=ENABLE; CURRENT_QUALITY=80; home_feed_column=5; browser_resolution=1536-730; fingerprint=fb29a08c7b17096111155a1607e34fb7; buvid_fp=fb29a08c7b17096111155a1607e34fb7; SESSDATA=f6688c80%2C1758269677%2C1cbed%2A32CjD0AOV4M90rWZ1jY4Qm-xW6IX39QwLudOJ2M2tMs-QXLHKaJU4k-oK7OKzIgkerDFYSVmdPWS1BWnZzTnZoVkFKRi1zZHFPLVJXTTVma0xxUXZDUEJqLVFDLS00eWZ3MmRpaGpCZmpCOEdyOGFzRGNxcEZEU0F2Nk1yWG93U3JRbFdkX2NmSlpBIIEC; bili_jct=66b6d33fa1b1410ba6931a1afaad0ad9; DedeUserID=372208078; DedeUserID__ckMd5=d4d6e2db641e2f38; sid=4nlg3mdi; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDMxNDg4MTAsImlhdCI6MTc0Mjg4OTU1MCwicGx0IjotMX0.Fcy6Y_zS6W__OCReL4d4GFVyxQy_0fl1utZWKcK9jZQ; bili_ticket_expires=1743148750; b_lsid=C8E6AD4E_195CCA399BD; bp_t_offset_372208078=1048218680195809280; CURRENT_FNVAL=4048",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
}

url ='https://api.bilibili.com/x/v2/reply/wbi/main'
data = {
    'oid' : '422395850',
    'type': '1',
    'mode': '2',
    'pagination_str':'{"offset":"{\"type\":3,\"direction\":1,\"Data\":{\"cursor\":41}}"}',
    'plat': '1',
    'web_location': '1315875',
    'w_rid': 'f246aacdabb25eb591fd191632a486ad',
    'wts': '1742897960',

}


response = requests.get(url=url,headers=headers,params=data)

json_data = response.json()
print(json_data)

replies = json_data['data']['replies']

for index in replies:
    ctime = index['ctime']
    dit = {
        '昵称':index['member']['uname'],
        '内容':index['content']['message'].replace('\n',''),
    }
    csv_writer.writerow(dit)
    print(dit)

pagination_str = json.dumps(json_data['data']['cursor']['pagination_reply']['next_offset'])
print(pagination_str)

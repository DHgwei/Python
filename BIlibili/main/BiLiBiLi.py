#导入数据请求模块
import requests
#导入日期模块
from datetime import datetime
#导入csv模块
import csv
#导入哈希模块
import hashlib
#导入序列化模块
import json
#导入编码的模块
from urllib.parse import quote
#导入时间模块
import time

def GetSign(wts,NextPage):
    "w_rid机密参数获取"
    # pagination_str = {"offset":NextPage}
    pagination_str = '{"offset": %s} '% NextPage
    #加密传入参数
    l=[
        #更换这个就行
        'oid=113249127306308'
        'type=1'
        'mode=2'
        f'pagination_str={quote(pagination_str)}'
        'plat=1 '                                             
        'web_location=1315875'
        f'wts={wts}'
    ]
    #列表合并成字符串
    y = '&'.join(l)
    #合并加密参数
    string = y +'ea1db124af3c7062474693fa704f4ff8'
    #使用md5加密
    MD5 = hashlib.md5()
    #传入加密参数
    MD5.update(string.encode('utf-8'))
    #进行加密处理
    w_rid =MD5.hexdigest()
    print(w_rid)
    # return w_rid
    return w_rid,pagination_str
# #测试
# exit()




#创建文件对象
f = open('read.csv',mode='w',encoding='utf-8-sig',newline='')
#字典写入方法
csv_writer=csv.DictWriter(f,fieldnames=[
        '昵称',
        '性别',
        '地区',
        '日期',
        '内容',
])
#写入表头
csv_writer.writeheader()

def GetContent(NextPage):

    "发送请求"
    #模拟浏览器
    headers = {
        #cookie 用户信息，常用于检测是否有登录账号
        "cookie":"buvid3=18D82174-863A-DB0C-E743-60873A55500815277infoc; b_nut=1736494215; _uuid=C23D2BE5-1D23-D867-22EA-A4155E623B9714948infoc; enable_web_push=DISABLE; buvid4=4CF62208-3A91-DF3D-CFF9-378C19AD511215991-025011007-L1%2FU%2B1SlTOR50HPiFRf6mQ%3D%3D; rpdid=|(k||lkJ)JJl0J'u~JYRmRkm~; header_theme_version=CLOSE; hit-dyn-v2=1; LIVE_BUVID=AUTO4917365083288553; is-2022-channel=1; buvid_fp_plain=undefined; PVID=2; enable_feed_channel=ENABLE; CURRENT_QUALITY=80; home_feed_column=5; browser_resolution=1536-730; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDI4ODU1MjksImlhdCI6MTc0MjYyNjI2OSwicGx0IjotMX0.akSi-eKzSMnx-jPfPgjYKgUc1qQMGyWABs1KhcDqrNo; bili_ticket_expires=1742885469; fingerprint=fb29a08c7b17096111155a1607e34fb7; bp_t_offset_372208078=1047452707138306048; buvid_fp=fb29a08c7b17096111155a1607e34fb7; SESSDATA=f6688c80%2C1758269677%2C1cbed%2A32CjD0AOV4M90rWZ1jY4Qm-xW6IX39QwLudOJ2M2tMs-QXLHKaJU4k-oK7OKzIgkerDFYSVmdPWS1BWnZzTnZoVkFKRi1zZHFPLVJXTTVma0xxUXZDUEJqLVFDLS00eWZ3MmRpaGpCZmpCOEdyOGFzRGNxcEZEU0F2Nk1yWG93U3JRbFdkX2NmSlpBIIEC; bili_jct=66b6d33fa1b1410ba6931a1afaad0ad9; DedeUserID=372208078; DedeUserID__ckMd5=d4d6e2db641e2f38; sid=4nlg3mdi; b_lsid=1BEB75C1_195C559C667; CURRENT_FNVAL=2000",
        # user-agent 用户代理，表示浏览器/设备基本身份信息
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"

    }

    #请求网址
    url = 'https://api.bilibili.com/x/v2/reply/wbi/main'
    # url ='https://api.bilibili.com/x/v2/reply/wbi/main?oid=633056059&type=1&mode=2&pagination_str=%7B%22offset%22:%22%22%7D&plat=1&seek_rpid=&web_location=1315875&w_rid=2be105d1050c7864c95f443437c6b261&wts=1742713358'
   #获取时间戳
    wts = int(time.time())
   #获取w_rid加密参数
    # w_rid = GetSign(wts=wts,NextPage=NextPage)
    w_rid,pagination_str = GetSign(wts=wts,NextPage=NextPage)
    print(pagination_str)
    #######发送请求

    ##额外构建请求
    #查询参数
    data = {
        'oid': '113249127306308',
        'type': '1',
        'mode': '2',
        # 'pagination_str': '{"offset":%s}' % NextPage,
        'pagination_str': pagination_str,
        'plat':'1',
        # 'seek_rpid':' ',
        'web_location': '1315875',
        'w_rid': w_rid,
        ' wts': wts,
    }

    #使用第三方模块:requests
    response = requests.get(url=url,params=data,headers=headers)

    # response = requests.get(url=url,headers=headers)

    "获取数据"
    #response.text 文本
    #response.json 字典，列表
    #response.context 图片
    #获取相应的json数据->字典
    json_data = response.json()
    #测试
    print(json_data)
    # "解析数据,提取需要的数据：评论"
    #第一次提取，提取评论所在列表位置
    # replies = json_data['data']['replies']
    if 'data' in json_data and 'replies' in json_data['data']:
        replies = json_data['data']['replies']
    else:
        print("Expected keys not found in JSON data")
        replies = None  # 或者采取其他适当的措施

    return replies

    ##测试
    #print(replies)


    #for循环遍历，提取列表里面的元素
    for index in replies:
        #提取具体每条评论的信息内容
        #提取时间戳
        ctime = index['ctime']

       ##测试
        print(type(ctime), ctime)  # 调试信息
        #把时间戳转成日期
        date = str(datetime.fromtimestamp(ctime))
        dit = {
            '昵称':index['member']['uname'],
            '性别':index['member']['sex'],
            '地区':index['reply_control']['location'],
            '日期':date,
            '内容':index['content']['message'],
        }

        #写入数据
        csv_writer.writerow(dit)
        print(dit)
    #获取写一页pagination_str的参数
    #json.dumps转换序列字符串
    pagination_str = json.dumps(json_data['data']['cursor']['pagination_reply']['next_offset'])

    ##测试
    print(pagination_str)
    return pagination_str

NextPage = '" "'
for page in range(1,21):
    print(f'正在采集第{page}页的数据内容')
    NextPage = GetContent(NextPage=NextPage)
#批量采集数据
#pagination_str-第一页是空的 -- 后续页参数没有规则一串数字，大概率参数在上一页中响应数据中返回
#seek_rpid：第一页有，后续没有这个参数，并且第一页是空的  -删掉不管，同样可以得到数据 --判断采集的是第一页携带
#w_rid：加密参数
#1.通过开发者工具搜索
#2.段断点调试分析，得出加密位置at(y + a)--加密参数y+a --函数方法 at
#var y = l.join("&")  ->   列表合并字符串  a值是固定的
#wts：时间戳->请求/访问当前页面时间点-通过time模块获取当前时间戳




#字典取值
    #键值对取值:根据冒号左边的内容[键]，提取冒号右边的内容[值]














"保存数据"





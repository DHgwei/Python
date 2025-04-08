
#drissionpage模块
#自动化模块
from DrissionPage import  ChromiumPage
from datetime import datetime
import csv

f = open('../message/message1.csv', mode='w', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f,fieldnames=['昵称','地区','日期','内容'])
csv_writer.writeheader()


dp = ChromiumPage()
dp.listen.start('aweme/v1/web/comment/list/')
dp.get('https://www.douyin.com/video/7460403983648132406')
for page in range(1,50):
    print(f'正在采集第{page}页的数据内容')
    resp = dp.listen.wait()
    json_data = resp.response.body
    comments = json_data['comments']
    for index in comments:
        create_time = index['create_time']
        date = str(datetime.fromtimestamp(create_time))
        dit = {
            '昵称':index['user']['nickname'],
            '地区':index['ip_label'],
            '日期':date,
            '内容':index['text'],
        }
        csv_writer.writerow(dit)
        print(dit)
    tab = dp.ele('css:.ayFW3zux')
    dp.scroll.to_see(tab)

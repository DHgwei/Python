#数据来源分析
# 1.明确需求
# 明确采集网站以及数据内容
# 网址：https://www.zhipin.com/web/geek/job?city=100010000&experience=102
# 数据：职位信息##

# 2.抓包分析
# 通过浏览器开发者工具分析对应数据的位置
# 打开开发者工具/F12
# 刷新网页
# 通过 关键字 搜索找到对应的数据位置
# 关键信息你需要的内容
# 数据包地址
#关于应届生的内容#
# https://www.zhipin.com/wapi/zpgeek/search/joblist.json?scene=1&query=&city=100010000&experience=102&payType=&partTime=&degree=&industry=&scale=&stage=&position=&jobType=&salary=&multiBusinessDistrict=&multiSubway=&page=1&pageSize=30#

# 代码实现步骤#
# request基本实现步骤
# 基本步骤分为四步：
# 发送请求：模拟浏览器对于Url地址发送请求
# 获取数据：提取服务器返回响应数据
# 解析数据：提取我们需要的数据内容
# 保存数据：提取的数据保存表格、文本、数据库、json文件中

# 为什么不选择使用request去请求获取数据呢？
# 某些网站数据内容（请求），存在加密内容-》需要js逆向
# 比如boss-》cookie中-Zp——stoken_时效性
#
# drissionpage自动化模块
# 模拟人的行为操作浏览器
# 点击 输入 拖拽 获取数据。。。。
#1.可以直接通过元素面板，进行元素定位获取相关数据内容
#2.可以直接监听数据，获取响应数据
#
#drissionpage采集基本步骤：
#1.打开浏览器，访问网站（发送请求）
#2.监听数据，获取相应数据（获取数据）
#监听数据-》在执行动作之前

####注意细节：
#需要配置浏览器可执行文件路径
#通过抓包分析找到的数据包链接地址，进行监听，并监听数据-》在执行动作之前


#3.解析数据：提取我们需要的数据内容
#4.保存数据：提取的数据保存表格、文本、数据库、json文件中

#点击下一页按钮
#1.定位按键元素
#2。定位进行相关操作
#dp.ele('css:.ui-icon-arrow-right').click()
#-dp.ele()  通过元素定位
#-css:.ui-icon-arrow-right   使用css语法查找元素
#-click()   点击操作



# 导入自动化模块
from DrissionPage import ChromiumPage
# 导入格式化输出模块
from pprint import pprint
# 导入csv模块
import csv

for i in range(520,540 ):
    # 创建文件对象
    # 可改文件名称
    f = open(f'data\data{i}.csv', mode='w', encoding='utf-8', newline='')
    #字典写入方法
    csv_writer = csv.DictWriter(f, fieldnames=[
            '职位',
            '城市',
            '企业名',
            '学历',
            '薪资',
            '经验',
            '领域',
            '规模',
            '融资',
            '技能要求',
            '基本福利',

    ])
    #写入表头
    csv_writer.writeheader()

    #实例化浏览器对象(自动打开浏览器)
    dp = ChromiumPage()
    #监听数据包
    dp.listen.start('wapi/zpgeek/search/joblist.json')
    #访问网站
    dp.get('https://www.zhipin.com/web/geek/job?city=100010000&experience=102')
    #循环翻页
    for page in range(1 , 11):
        print(f'正在采集第{page}页的数据内容')
        #下滑网页页面到底部
        dp.scroll.to_bottom()
        #等待数据包加载
        resp = dp.listen.wait()
        #获取响应数据
        json_data = resp.response.body
        "解析数据"
        #提取职位信息所在列表
        jobList = json_data['zpData']['jobList']
        #for循环遍历，提取列表里面元素（30个岗位信息）
        for index in jobList:
            print(index)
            #提取职位信息数据，保存字典
            dit = {
                '职位': index['jobName'],
                '城市': index['cityName'],
                '企业名': index['brandName'],
                '学历': index['jobDegree'],
                '薪资': index['salaryDesc'],
                '经验': index['jobExperience'],
                '领域': index['brandIndustry'],
                '规模': index['brandScaleName'],
                '融资': index['brandStageName'],
                '技能要求': ''.join(index['skills']),
                '基本福利': ''.join(index['welfareList']),
            }
            # join 列表合并字符串
            #写入数据
            csv_writer.writerow(dit)
            print(dit)
        #点击下一页(元素定位)
        dp.ele('css:.ui-icon-arrow-right').click()
       #dp.ele('css:.options-pages a:last-of-type').click()




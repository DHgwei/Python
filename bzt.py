####数据可视化
#简单使用可视化
#1.利用pandas模块对数据进行读取处理
#2.利用pyecharts可视化模块进行可视化(可以复制官方文档中的代码，修改数据即可)
#pyecharts官方文档链接:https://gallery.pyecharts.org/#/README##


#导入数据处理模块
import pandas as pd
#导入配置项
from pyecharts import options as opts
#导入饼图
from pyecharts.charts import Pie
#生成随机数据
from pyecharts.faker import Faker
#读取csv文件
df = pd.read_csv('../data/data.csv')
#print(df.head())
#获取x轴数据内容
x_city = df['城市'].value_counts().index.to_list()
#获取y轴数据内容
y_city = df['城市'].value_counts().to_list()
print(x_city)
print(y_city)

c = (
    Pie()
    .add(
        "",
        [
            list(z)
            for z in zip(
                x_city,  # x轴数据
                y_city,  # y轴数据
            )
        ],
        center=["40%", "50%"],
    )
    .set_global_opts(
        #设置可视化标题
        title_opts=opts.TitleOpts(title="应届生 招聘城市分布情况"),
        legend_opts=opts.LegendOpts(type_="scroll", pos_left="80%", orient="vertical"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    #导出可视化效果:保存html文件
    .render("pie_应届生 招聘城市分布情况.html")
)

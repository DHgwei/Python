#导入数据处理模块
import pandas as pd
#导入配置项
from pyecharts import options as opts
#导入柱状图
from pyecharts.charts import Bar
from pyecharts.charts import Line

#读取csv文件
df = pd.read_csv('../data/data.csv')
#print(df.head())
#获取x轴数据内容
x_edu = df['学历'].value_counts().index.to_list()
#获取y轴数据内容
y_edu = df['学历'].value_counts().to_list()
#获取x轴数据内容
x_sal = df['薪资'].value_counts().index.to_list()
#获取y轴数据内容
y_sal = df['薪资'].value_counts().to_list()


c_bar = (
    Bar()
    .add_xaxis(x_edu)
    .add_yaxis("学历", y_edu, stack="stack1")
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="Bar-毕业生学历要求分布"))
    .render("Bar_edu.html")

)


df = pd.read_csv('../data/data.csv')
#获取x轴数据内容
x_sal = df['薪资'].value_counts().index.to_list()
#获取y轴数据内容
y_sal = df['薪资'].value_counts().to_list()


c_line = (
    Line()
    .add_xaxis(x_sal)
    .add_yaxis("薪资", y_sal, is_connect_nones=True)
    .set_global_opts(title_opts=opts.TitleOpts(title="Line-毕业生薪资分布"))
    .render("Line_sal.html")
)
#导入数据处理模块
import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Line
#读取csv文件
df = pd.read_csv('../data/data.csv')
#获取x轴数据内容
x_exp = df['薪资'].value_counts().index.to_list()
#获取y轴数据内容
y_exp = df['薪资'].value_counts().to_list()


c = (
    Line()
    .add_xaxis(x_exp)
    .add_yaxis("薪资", y_exp, is_connect_nones=True)
    .set_global_opts(title_opts=opts.TitleOpts(title="毕业生薪资分布"))
    .render("KSH/salary.html")
)

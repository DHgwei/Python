#导入数据处理模块
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Geo
#读取csv文件
df = pd.read_csv('../data/data.csv')
#print(df.head())
#获取x轴数据内容
x_city = df['城市'].value_counts().index.to_list()
#获取y轴数据内容
y_city = df['城市'].value_counts().to_list()

c = (
    Geo()
    .add_schema(maptype="china")
    .add("geo", [list(z) for z in zip(x_city, y_city)])
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(is_piecewise=True),
        title_opts=opts.TitleOpts(title="Geo-全国毕业生城市招聘（分段型）"),
    )
    .render("geo_全国毕业生城市招聘.html")
)

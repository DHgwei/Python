import pandas as pd
import glob
import os

# 定义CSV文件所在的文件夹路径
path = r'/data/'

# 使用glob.glob函数获取所有匹配的CSV文件路径
all_files = glob.glob(os.path.join(path, "*.csv"))

# 创建一个空的DataFrame来存储合并后的数据
df_merged = pd.DataFrame()

# 遍历所有CSV文件，读取每个文件并将其添加到已合并的数据中
for file in all_files:
    df = pd.read_csv(file, encoding='utf-8')  # 根据实际情况调整编码
    df_merged = pd.concat([df_merged, df], ignore_index=True)

# 将合并后的数据保存为一个新的CSV文件
df_merged.to_csv(os.path.join(path, 'data.csv'), index=False, encoding='utf-8')

import pandas as pd

# 输入文件路径和输出文件路径
input_file = '../data/Zfline/zfxls/04-04.xls'      # 替换为你的xls文件路径
output_file = '../data/Zfline/zfcsv/zfcsv1.csv'     # 输出的csv文件路径

# 读取xls文件
df = pd.read_excel(input_file)

# 保存为csv文件
df.to_csv(output_file, index=False, encoding='utf-8-sig')

print(f"文件已成功从 {input_file} 转换为 {output_file}")

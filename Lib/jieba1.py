# 导入所需的库
import jieba
from collections import Counter
import csv

# 定义CSV文件路径和TXT文件路径
csv_file_path = '../message/message1.csv'
txt_file_path = '../message/message1.txt'


# 打开CSV文件
with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csv_file:
    # 创建CSV读取器
    csv_reader = csv.DictReader(csv_file)

    # 打开TXT文件
    with open(txt_file_path, mode='w', encoding='utf-8') as txt_file:
        # 遍历CSV文件的每一行
        for row in csv_reader:
            # 提取所需的列
            message = row['内容']

            # 将提取的内容写入TXT文件
            txt_file.write(f"{message}\n")

print(f"成功将 {csv_file_path} 中的部分内容提取并保存到 {txt_file_path}.")

# 读取文本文件
with open('../message/message.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# 使用jieba进行分词
words = jieba.lcut(text)

# 统计词频
word_counts = Counter(words)

# 按词频从高到低排序，并输出前100个高频词语
for word, count in word_counts.most_common(100):
    print(f'("{word}", {count}),')


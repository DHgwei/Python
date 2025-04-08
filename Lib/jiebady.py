import jieba
from collections import Counter
from pyecharts.charts import WordCloud
from pyecharts import options as opts

# 示例中文文本
with open('../zfdata/zfms/zfms1.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. 使用 jieba 进行中文分词
words = jieba.lcut(text)

# 2. 去除停用词（可根据需要扩展停用词列表）
stopwords = set("，。！？；：「」‘’“”()（）")
filtered_words = [word for word in words if word not in stopwords and len(word) > 1]  # 去除单个字的词

# 3. 统计词频
word_freq = Counter(filtered_words)

# 4. 转换成适用于 pyecharts 词云的格式
wordcloud_data = [(word, freq) for word, freq in word_freq.items()]

# 5. 创建词云对象
wordcloud = (
    WordCloud()
    .add("", wordcloud_data, word_size_range=[20, 100])  # 词大小范围
    .set_global_opts(title_opts=opts.TitleOpts(title="中文词云"))
)

# 6. 生成 HTML 并保存
wordcloud.render("../CY/zfcy/zfcy1.html")

print("词云已生成，文件名为 zfcy1.html")

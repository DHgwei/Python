import pandas as pd
import jieba1
from wordcloud import WordCloud
import numpy as np
from PIL import Image
df = pd.read_csv('../message/message.csv')
#获取评论内容
content = ' '.join([str(i) for i in df['内容']])
#分词处理
string = ' '.join(jieba.lcut(content))
print(string)
wc = WordCloud(
    background_color='white',
    height=700,
    width=1000,
    font_path='msyh.ttc',
    stopwords={'了','的','是','我','都','就是','也','有','就','在','那','啊','真的','：','？','。','，','毕业','工作','人','就业','万','没','去','看','今年'}
)
wc.generate(string)
wc.to_file('CY/cy.png')
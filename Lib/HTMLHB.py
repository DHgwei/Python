from bs4 import BeautifulSoup

# 创建一个空的BeautifulSoup对象
combined_html = BeautifulSoup('', 'html.parser')

# 打开要整合的HTML文件，依次将它们添加到combined_html中
with open('Bar_edu.html', 'r', encoding='utf-8') as f:
    html1 = BeautifulSoup(f.read(), 'html.parser')
    combined_html.append(html1)

with open('Line_sal.html', 'r', encoding='utf-8') as f:
    html2 = BeautifulSoup(f.read(), 'html.parser')
    combined_html.append(html2)

# 将combined_html输出到一个新的HTML文件中
with open('combined.html', 'w', encoding='utf-8') as f:
    f.write(combined_html.prettify())

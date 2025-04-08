from DrissionPage import WebPage
from DrissionPage.common import Actions

wp = WebPage()
ac = Actions(wp)
wp.ele('xpath://div[@class="search-icon"]').click()
#wp.get('https://www.xiaohongshu.com/')
wp.listen.start('web/v1/search/notes')
for page in range(5):
    packet = wp.listen.wait()
    print(packet.response.body)
    ac.scroll(delta_y=1500)
    wp.listen.stop()

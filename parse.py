import urllib.request
from bs4 import BeautifulSoup as bs
import re
import os
import time

UserAgent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'
page = 0
hua = 700


def download_img(img_url, path):
    # 设置http header
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"}
    request = urllib.request.Request(img_url, headers=header)
    try:
        response = urllib.request.urlopen(request)
        # img_name = "img.jpg"
        filename1 = "F:\\Desktop\\"+path.split('-')[0]+"\\"
        filename2 = path[path.index('-')+1:]
        filename = filename1 + filename2
        if not os.path.exists(filename1):
            os.mkdir(filename1)
        if (response.getcode() == 200):
            with open(filename, "wb") as f:
                f.write(response.read())  # 将内容写入图片
        return filename
    except:
        return "failed"


def main(r2):
    # r1 = open('demo.html', 'rb')
    # r2 = r1.read().decode('utf-8')
    r3 = bs(r2, "html.parser")

    mhurl = "2013/02/2717234313.jpg"

    r4 = r3.find_all('script')

    for i in r4:
        content = i.contents
        if content and content[0]:
            re1 = re.compile('var mhurl')
            if re1.search(content[0]):
                start = content[0].find('var mhurl')
                pos = content[0][start:].find(';')
                mhurl = content[0][start:start+pos+1].split('\"')[1]
                break

    mhss = "https://p5.manhuapan.com"
    mhpicurl = mhss + "/" + mhurl

    title = r3.title.string
    num = re.compile('\d+')
    num = num.findall(title)
    if len(num) == 1:
        num.append('1')
    title2 = '-'.join(num)
    title3 = (title2 + '-' + mhurl).replace('/', '-')

    download_img(mhpicurl, title3)

    r6 = r3.select('.pure-button-primary')
    for i in r6:
        if '下一话吧' == i.text:
            return False
    return True


def geturl():
    return 'https://manhua.fzdm.com/02/'+str(hua)+'/index_'+str(page)+'.html'


def getHtml(url):
    head = {
        "User-Agent": UserAgent
    }
    try:
        html = urllib.request.urlopen(urllib.request.Request(
            url, headers=head)).read().decode('utf-8')
        global page
        if main(html):
            page += 1
            getHtml(geturl())
        else:
            page = 0
    except Exception as a:
        print(a)
    finally:
        pass


def range2(hua2, cout):
    global hua
    hua = hua2
    for i in range(cout):
        hua = hua2 + i
        print(str(hua)+'画开始时间:'+time.asctime(time.localtime(time.time())))
        getHtml(geturl())


if __name__ == '__main__':
    range2(705, 40)
    print('结束时间:'+time.asctime(time.localtime(time.time())))

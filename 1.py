# -*- coding: utf-8 -*-
import re
import six.moves.urllib as urllib
# import urllib
# from urllib import *
import requests

def get_onepage_urls(onepageurl):
    if not onepageurl:
        print('beginning...')
        return [], ''
    try:
        html = requests.get(onepageurl)
        html.encoding = 'utf-8'
        html = html.text
    except Exception as e:
        print(e)
        pic_urls = []
        next_url = ''
        return pic_urls, next_url
    pic_urls = re.findall('"objURL":"(.*?)",', html, re.S)
    next_urls = re.findall(re.compile(r'<a href="(.*)" class="n">下一页</a>'), html, flags=0)
    next_url = 'http://image.baidu.com' + next_urls[0] if next_urls else ''
    return pic_urls, next_url


def download_pic(keyword, pic_urls):
    for i, pic_url in enumerate(pic_urls):
        try:
            pic = requests.get(pic_url, timeout=15)
            outpath = 'D:\\Code_python\\SVM\\Pictures\\' + '%s_'% keyword + str(i ) + '.jpg' # 图片存储地址
            with open(outpath, 'wb') as f:
                f.write(pic.content)
                print('The picture %s is downloaded successfully: %s' % (str(i ), str(pic_url)))
        except Exception as e:
            print('The picture %s is failure: %s' % (str(i ), str(pic_url)))
            print(e)
            continue


if __name__ == '__main__':
    keywordList = ['单个苹果', '单个菠萝', '单个西红柿'] # 图片种类
    index = 0
    for keyword in keywordList:
        print('start to download: %s' % keyword)
        url_init_first = r'http://image.baidu.com/search/flip?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1497491098685_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&ctd=1497491098685%5E00_1519X735&word='
        url_init = url_init_first + urllib.parse.quote(keyword, safe='/')
        all_pic_urls = []
        onepage_urls, next_url = get_onepage_urls(url_init)
        all_pic_urls.extend(onepage_urls)
        next_count = 0  # 下载计数
        while True:
            onepage_urls, next_url = get_onepage_urls(next_url)
            next_count += 1
            if next_url == '' and onepage_urls == []:
                break
            all_pic_urls.extend(onepage_urls)
        download_pic(index, list(set(all_pic_urls)))
        index += 1

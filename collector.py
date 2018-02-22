from multiprocessing.dummy import Pool
import re
import os
import time

import requests

research_url = 'https://www.natureasia.com/zh-cn/research/highlight/'
review_url = 'https://www.natureasia.com/zh-cn/life-sci/review/'


def get_(x):
    try:
        resp = requests.get(''.join((research_url, str(x))), timeout=10)
        print(resp.url, resp.status_code)
        return resp
    except Exception as _:
        print(x, _)
        return None


def func_(x):
    # if os.path.isfile(os.getcwd() + '/static/pages/%s.html' % x):
    #     return False

    resp = get_(x)
    if not resp:
        return False

    title = re.findall('h1 class="title">(.*?)</h1', resp.text)
    title = title[0] if title else title

    journal = re.findall('p class="journal">(.*?)</p', resp.text)
    journal = journal[0] if journal else journal

    date = re.findall('p class="pub-date">(.*?)</p', resp.text)
    date = date[0] if date else date

    hl = re.findall('div class="hl-text">([\s\S]*?)</div', resp.text)
    hl = hl[0] if hl else hl

    doi = re.findall('(doi:.*?)\|', resp.text)
    doi = doi[0] if doi else doi

    link = re.findall('href="(.*?)">原创文章</a>', resp.text)
    link = link[0] if link else link

    if not hl:
        print(x, 'no hl')
        return False
    with open(os.getcwd() + '/template.html', 'r') as f:
        print(x, 'get')
        html_ = f.read()
        html_ = html_.format(title=title,
                             journal=journal,
                             date=date,
                             hl=hl,
                             doi=doi,
                             link=link)
        with open(os.getcwd() + '/static/pages/%s.html' % x, 'w', encoding='utf-8') as wf:
            wf.write(html_)


resp_ = requests.get('https://www.natureasia.com/zh-cn/research/', timeout=5)
ids = re.findall('"/zh\-cn/research/\S*/(\d{1,5})"', resp_.text)

p = Pool(100)
p.map(func_, ids)
p.close()
p.join()

import requests
from lxml import html
import os
page=requests.get(url4)
tree = html.fromstring(page.content)
path="test"
imgs=tree.xpath('//img')
filename_prefix='t'
imgformat=".jpeg"

for i in range(0,len(imgs)):
    with open(os.path.join(path,filename_prefix + str(i) + imgformat), 'wb') as f:
    imgdata=requests.get(imgs[i].get("src"))
    f.write(imgdata.content)

from urllib.request import Request,urlopen
import re
html = """
<li>
 <a class="magazine_wrap" href="https://www.ugirls.com/Shop/Detail/Product-471.html" target="_blank" title="[U369]韩沫瑜">
<img class="magazine_img lazy" src="https://img.ugirls.tv/uploads/magazine/cover/ed307f893aaaf74dd88d02cdf07d8c82_cover_web_l.jpg" data-original="[图片][图片]https://img.ugirls.tv/uploads/magazine/cover/ed307f893aaaf74dd88d02cdf07d8c82_cover_web_l.jpg" alt="[U369]韩沫瑜" width="" height="" style="display: block;">                         		
<div class="magazine_detail">
<h1 class="magazine_title">[U369]韩沫瑜</h1>
<div class="magazine_other_info">
<p>发行时间/<span>2018.05.23 03:47:16</span></p>
<p>订阅量/<span>5200</span></p>
</div>
<div class="magazine_desp">
她打开了夏天的窗，薄荷味的海风扑面而来，她轻抚被风吹乱的头发...<span class="desp_over">[详细]</span>
</div>
</div>
 </a>
 <div class="magazine_view">
<a title="订阅量" class="icon-heart"></a><span class="like_count">5200</span>
</div>
<div class="magazine_model_info">
<a href="https://www.ugirls.com/Models/Detail/Model-936.html" target="_blank" title="韩沫瑜"><img class="lazy" src="[图片]https://img.ugirls.tv/uploads/users/header/5e94296440fe0fdbabee55384578050e.jpg" data-original="[图片][图片]https://img.ugirls.tv/uploads/users/header/5e94296440fe0fdbabee55384578050e.jpg" style="width: 26px; height: 26px; display: inline;" alt="韩沫瑜" width="26" height="26"></a>
<h1 class="magazine_model_name"><a href="https://www.ugirls.com/Models" target="_blank" title="模特">模特</a>/<a href="[图片]https://www.ugirls.com/Models/Detail/Model-936.html" target="_blank" title="韩沫瑜">韩沫瑜</a></h1>
<a class="magazine_tag" href="https://www.ugirls.com/Index/Search/Magazine-64.html" target="_blank" title="妩媚专辑">妩媚</a>
</div>                          
</li>
"""
r = re.compile('<img.*?magazine_img.*?src="(.*?)".*?data-original.*?>',re.S)
bin = re.findall(r,html)
print(bin)



url = 'https://www.ugirls.com/Models/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
}
q = Request(url,headers=headers)
e = urlopen(q)
r = e.read().decode('utf-8')
with open('雨果.html', 'w', encoding='utf-8') as f:
    f.write(r)
with open('雨果.html', 'r', encoding='utf-8') as f:
    a = f.read()
    #print(a)

    # < img
    #
    #
    # class ="model_img" src="https://img.ugirls.tv/uploads/users/models/modellistrecommend/aec035060df6798689a921aac8900191.jpg" width="156" height="243.75" alt="Zora若拉:" >
t = re.compile('<img .*?model_img.*?src="(.*?)".*?>',re.S)
bin = re.findall(t,a)
print(bin)

for i in bin:
    print(i)
    b = i

    with open('雨果图片网址.txt', 'a',encoding='utf-8') as f:
        f.write(b+'\n')

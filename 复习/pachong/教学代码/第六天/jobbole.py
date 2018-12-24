# <li class="media">
# <a id="38654voteflag" title="顶起，让更多人看到" alt="顶起，让更多人看到" class="href-style p-cnt  vote-post-up  register-user-only " data-post-id="38654" data-current-vote="1">
# <span id="38654votetotal">27</span>
# <i class="fa fa-chevron-up"></i>
# </a>
                                        
# <div class="media-body">
# <h3 class="p-tit">
# <a target="_blank" href="http://top.jobbole.com/38654/">地址 1.1.1.1，Cloudflare 推新公共 DNS 服务</a>
# <label class="hide-on-480 small-domain-url"></label>
# </h3>
# <p class="p-meta">
# <span>04/02</span>
# <span>
# <a href="http://top.jobbole.com/38654/#comments">
# <i class="fa fa-comments-o">
# </i>
#  5 
# </a>
# </span>
# </p>
# </div>                                
# </li>

# li_list //li[@class="media"] 拿到所有的文章列表 element
for item in li_list:
    title = item.xpath('.//h3[@class="p-tit"]/a/text()')[0]
    link = item.xpath('.//h3[@class="p-tit"]/a/@href')[0]
    publish_time = item.xpath('.//p[@class="p-meta"]/span[1]/text()')[0]
    # tag = item.xpath('.//p[@class="p-meta"]/span[@class="p-tags"]/a/text()')
    tag = item.xpath('.//span[@class="p-tags"]/a/text()')
    if len(tag) == 0:
        tag = '没有标签'
    #如果存在i[@class="fa fa-comments-o"]，说明肯定与评论
    comment = item.xpath('.//i[@class="fa fa-comments-o"]')
    if len(comment) == 0:
        #没找到i[@class="fa fa-comments-o"]，说明没有评论
        comment = '0'
    elif len(comment) > 0:
        #找到了i[@class="fa fa-comments-o"]，说明有评论
        #分为两种情况，一种是有标签、有评论，一种是没有标签，有评论
        if tag == '没有标签': #没有标签，有评论的判断
            #没有标签的情况
            comment = item.xpath('.//p[@class="p-meta"]/span[2]/a/text()')[0]
        else: #有标签，有评论的判断
            comment = item.xpath('.//p[@class="p-meta"]/span[3]/a/text()')[0]
            
           
    

    # if len(title) == 0:
    #     title = title[0]


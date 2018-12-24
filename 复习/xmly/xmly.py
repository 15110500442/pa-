import requests
import json
import os


headers = {

    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'Cookie': 'x_xmly_traffic=utm_source%253A%2526utm_medium%253A%2526utm_campaign%253A%2526utm_content%253A%2526utm_term%253A%2526utm_from%253A; device_id=xm_1543642838695_jp51399jj6zaa6; _xmLog=xm_1543642890852_jp514dicx8iprh; trackType=web; x_xmly_traffic=utm_source%3A%26utm_medium%3A%26utm_campaign%3A%26utm_content%3A%26utm_term%3A%26utm_from%3A; login_from=weixin; 1&remember_me=y; 1&_token=141798460&48AB819742684NdVE791F48029445513119A4AD370BBA9766A5344295348217F1BC174CA5BE27773; 1_l_flag="141798460&48AB819742684NdVE791F48029445513119A4AD370BBA9766A5344295348217F1BC174CA5BE27773_2018-12-01 13:45:59"; Hm_lvt_4a7d8ec50cfd6af753c4f8aee3425070=1543673626,1543673883,1543673931,1543748058; Hm_lpvt_4a7d8ec50cfd6af753c4f8aee3425070=1543748058'
}

def get_all_urls():
    start_urls = 'https://www.ximalaya.com/revision/explore/getCategories'
    response = requests.get(start_urls,headers=headers).text
    for i in range(2):
        jsons = json.loads(response)['data']['categoryGroupInfo'][i]['categories'][0]
        name = jsons['name']
        displayName = jsons['displayName']
        for j in range(35):
            details_all_urls = 'https://www.ximalaya.com/revision/category/queryCategoryPageAlbums?category={}&subcategory=&meta=&sort=1&page={}&perPage=30'.format(name,j)
            get_details_urls(details_all_urls,displayName)

def get_details_urls(url,name1):
    response = requests.get(url,headers=headers).text
    jsons = json.loads(response)['data']['albums'][0]
    name = jsons['title']
    albumId = jsons['albumId']
    for i in range(1,4):
        details_url = 'https://www.ximalaya.com/revision/play/album?albumId={}&pageNum={}&sort=-1&pageSiz'.format(albumId,i)
        mkdir_folder(name)
        os.chdir(r'/home/jinlei/learn/爬虫/爬虫文件/xmly/音频文件/'+name)
        get_details(details_url)
def mkdir_folder(name):
    '''
    创建文件夹
    :param name:
    :return:
    '''
    path = name.strip()
    isExists = os.path.exists(os.path.join(r'/home/jinlei/learn/爬虫/爬虫文件/xmly/音频文件/',path))
    if not isExists:
        print('正在创建一个{}的文件夹'.format(name))
        os.makedirs(os.path.join(r'/home/jinlei/learn/爬虫/爬虫文件/xmly/音频文件/',path))
        return True
    else:
        print('{}文件夹已经存在'.format(name))
        return False


def get_details(details_url):
    try:
        response = requests.get(details_url,headers=headers).text
        jsons = json.loads(response)['data']['tracksAudioPlay'][0]
        link = jsons['src']
        name = jsons['trackName']
        download(link,name)
    except Exception as err:
        print(err, "错误")

def download(url,name):
    try:
        download_file = requests.get(url,headers=headers).content
        with open(name,'wb') as f:
            f.write(download_file)
    except Exception as err:
        print(err, "错误")


if __name__ == '__main__':
    get_all_urls()























'''
  
  # wenxue_ertong_details_url = 'https://www.ximalaya.com/revision/category/detailCategoryPageInfo?category={}&subcategory='.format(name)
        # wenxue_ertong_details_response = requests.get(wenxue_ertong_details_url,headers=headers).text
        # json1 = json.loads(wenxue_ertong_details_response)['data']['subcategories'][9]
        # link = json1['link']
        # print(link)

    # for i in range(2):
    #     jsons = json.loads(response)['data']['categoryGroupInfo'][i]['categories'][0]['subcategories']
    #
        # print(jsons)

'''
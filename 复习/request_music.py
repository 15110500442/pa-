import requests
from lxml import  etree
import json
def get_data():
    url = 'https://music.163.com/weapi/artist/list?csrf_token=bc971e002b5d6618022a6f62deaf8aff'
    header = {
        'Cookie': '_iuqxldmzr_=32; _ntes_nnid=d342f3a4325db61a74b59eaba8e3ce94,1543366456428; _ntes_nuid=d342f3a4325db61a74b59eaba8e3ce94; __utmc=94650624; __utmz=94650624.1543366461.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); WM_NI=XTL2Bfu%2BoHaYK8WUCX7kyKn9OC1f9%2F5xsmqyGMZ5of5sJ%2Fq5GoECeEe8%2B6YDN9%2B7LmIzSo7ETGoJE%2FV%2BNswMzYLUBVHEs%2FHvK6Xr0DE3o4DH5cZU%2FVrXsLK%2BaXVixAqua2M%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb2b841b5effbb7ee7989a88fb2c85b869e8bbbf345f297bb90ce3fb0b09eabd62af0fea7c3b92a9c8c84d3c16eb7f5a1a9e45389e899b6c254f5b5b7aced338d9dff87bc25f7a8bd8ef473859396d6ee6ef7ad86d0f43f85b18ba4e84fa7e8e5d7dc508ee7e5d8cf678ba69d90b64f9899a1abc82596f58294f647ba8784b6c15e8c9bbdd0cb7e89ea9893b35087eda1d5c744f7bd96b6ae5eb288bdadca21a3889a8afb4bb3abafd3d037e2a3; WM_TID=Yylfb1Ylo6VAFBABFBNtbzMr5Op0oQdT; __utma=94650624.894879050.1543366461.1543366461.1543371421.3; playerid=11577767; JSESSIONID-WYYY=eCPD%5C1GIiaxiuHyHgh0TgE4qZIEEKgEcH%2B6OFywEwaotJO7mflqj2Ji1Q9eoWA9Qa22bOw0Qm%2B5VZkgtz4nPOMBjDCn%2Bj4ZKf3s%5Cmtobw0CXA2csgb82UJlj1c2SjPYxgjY0FDaHxv5K1jXU12%5ClNAjv67hNX6hXWOgZIzU36aQ8zPiW%3A1543376959893; MUSIC_U=9de0b492647e466135757c175cbbbd722f62ec5feaf3725eb89a11bc94e9e12772408fe876baa3a9abebd35ee8b1704e39b61e28bcc3f61b8540ea6a0a55e79877a74413fafbef35; __remember_me=true; __csrf=5a8500b23e4b23b1ea04d45c5a20389b; jsessionid-cpta=yDkTYOpK1ojNSKFqLQ3kX881XGeYDam%5CneQHSzUMkxBCyfuVnhxyq%5Co0ZGwu1BKu4ANB%2BF%5Cd0LBhlDebvkikqEuZ4YLIkxPzGdkrENHb0ApC%2F%5C1uP6QLzLHW8viYeh%5CvU7HygzxOeIDoHLaQN85OKcKeHWjIlpm8MBKFzJafB0TW%2FWIf%3A1543376165382; c98xpt_=30; NETEASE_WDA_UID=1578673950#|#1543375284959; __utmb=94650624.35.10.1543371421',
        'Origin': 'https://music.163.com',
        'Accept': '*/*',
        'Referer': 'https://music.163.com/discover/artist/signed/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'User-Agent': 'Mozilla / 5.0(X11;Linuxx86_64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 70.0.3538.110Safari / 537.36',
    }
    data = {
        'params': '2igQDoF29R9FnCqsIap7eqZRGLDlNh+vl3Ori0I/hnrgUfofm3gRk5tKpQdQGEpDgkFcqeIzpO1rqUz1awwQ0QCcQMjM2KDTKvUynP405h89wXD1ee+C9W1Ada0kmGwKfSMq2c4XWE29Vcc6eq02hZKq6QO1w7GjOcqhqlyj3P0zHYQsp+Ccgk+HDxbwAX8i4MIeGs5N06CDqH9uc5FAoBk/jt1eJSFqSPvtKopZte4=',
        'encSecKey': '0dcfb8162eb390b050c1af17635e915a8252c2d4a4bac1c208948cbbc6ed338abc1bbefc0cd275274bf72d6326f11c7026385db5e6ca8febcaae819a4896449151d4874b7676fd73791ec4ac1c09d7f833b9c862ef7a968c32eddd1c0f0aaf475da35519cf62cd86056169b43caab006617b51d33d0cb617d1011ec853b743ae',
    }
    response = requests.post(url,headers=header,data=data)
    new_url1 = []
    for i in range(3):
        jsons = json.loads(response.text)['artists'][i]
        id = jsons['id']
        new_url = 'https://music.163.com/artist?id={}'.format(id)
        new_url1.append(new_url)

    return new_url1,header
get_data()

def get_music():
    new_url,header = get_data()
    for i in range(3):
        rep = requests.get(new_url[i])
        for i in range(30):




            music_url = 'https://music.163.com/#/song?id=574566207'
            a = requests.get(music_url)
            print(a.text)
            # music_data = {
            #     'params': 'doBpWosE8ZYt/4fuK5FOLFHd4FYJmKPtWhtkQ9UQM+FXEVb0YiNOncIKvCby9/NSCSJBjmoiajC+OzkrKg01pBCJCms6jQ5BLm75r4VoQlP1iWawKJZv/2C42BXWUhmx5Kun/jUY4pkDNwmIqOatvgiCYOe2qRaRj4fJ0oMujZ+PJC7iYaEW54/vCLCwvsid',
            #     'encSecKey': '6c69c5987f1954c6330037d90d8d0b5c18f5537e472120f673d892709d6815a5556c201e388c48ac57da851487d8446303628b107b618214ced70bff9cdfc62a2531f469d48af7497bd5218b3128b56e318f884d2e61ee3c58a30ba718ad2547e284b5833a5882dd7f7aa99f982dcf48313f957414d69a704743384d0b817201',
            # }
            # music_rep = requests.post(music_url,headers=header,data=music_data)
            # music = json.loads(music_rep.text)['data']
            # print(music)

#
#
#
#
get_music()

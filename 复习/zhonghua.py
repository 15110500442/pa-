import requests
import json
from lxml import etree
import re
def get_data():
    for i in range(1,78):
        url = 'http://faculty.hust.edu.cn/system/resource/tsites/asy/asyqueryteacher.jsp?collegeid=0&disciplineid=0&pageindex={}&pagesize=12&rankid=0&honorid=0&py=&viewmode=8&viewid=66528&siteOwner=1391599222&viewUniqueId=66528&showlang=&type=pyteacher'.format(i)
        response = requests.get(url).text
        for i in range(12):
            detail_url = json.loads(response)['teacherData'][i]['url']
            detail_data(detail_url)

def detail_data(detail_url):
    try:
        response = requests.get(detail_url)
        response.encoding = 'utf-8'
        html = etree.HTML(response.text)
        if html.xpath('//div[@class="dft-main clearfix"]'):
            name = html.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/h2/text()')[0]
            gerenxinxi = ''.join(html.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/p/text()')).split()
            dict_gerenxinxi = {i.split('：')[0]: i.split('：')[1] for i in gerenxinxi if '：' in i}
            # 性别
            sex = dict_gerenxinxi.get('性别','-')
            # 在职信息
            employment_information = dict_gerenxinxi.get('在职信息','-')
            # 毕业院校
            graduated_school = dict_gerenxinxi.get('毕业院校','-')
            # 所在单位
            current_unit = dict_gerenxinxi.get('所在单位','-')
            # 学科
            subject = dict_gerenxinxi.get('学科','-')
            # 学位
            Bachelor_of_science = dict_gerenxinxi.get('学位','-')
            # 学历
            education = dict_gerenxinxi.get('学历','-')
            # 个人信息
            personal_information = {
                '姓名':name,
                '性别':sex,
                '在职信息':employment_information,
                '毕业院校':graduated_school,
                '所在单位':current_unit,
                '学科':subject,
                '学位':Bachelor_of_science,
                '学历':education,
            }
            # 联系方式
            lianxifangshi = ''.join(html.xpath('/html/body/div[2]/div[2]/div[1]/div[3]/div[2]//p//text()')).replace('·','').replace(',',' ').split()
            # 字典_联系方式
            dict_lianxifangshi = {i.split('：')[0]: i.split('：')[1] for i in lianxifangshi}
            # 邮编
            zip_code = json.loads(requests.get('http://faculty.hust.edu.cn/system/resource/tsites/tsitesencrypt.jsp?id=_tsites_encryp_tsothercontact_tsccontent&content={}&mode=8'.format(dict_lianxifangshi.get('邮编','-'))).text)['content']
            # 办公地址
            office_address = json.loads(requests.get('http://faculty.hust.edu.cn/system/resource/tsites/tsitesencrypt.jsp?id=_tsites_encryp_tsothercontact_tsccontent&content={}&mode=8'.format(dict_lianxifangshi.get('通讯/办公地址','-'))).text)['content']
            # 办公室电话
            office_phone = json.loads(requests.get('http://faculty.hust.edu.cn/system/resource/tsites/tsitesencrypt.jsp?id=_tsites_encryp_tsothercontact_tsccontent&content={}&mode=8'.format(dict_lianxifangshi.get('办公室电话','-'))).text)['content']
            # 移动电话
            mobile_phone = json.loads(requests.get('http://faculty.hust.edu.cn/system/resource/tsites/tsitesencrypt.jsp?id=_tsites_encryp_tsothercontact_tsccontent&content={}&mode=8'.format(dict_lianxifangshi.get('移动电话','-'))).text)['content']
            # 邮箱
            email = json.loads(requests.get('http://faculty.hust.edu.cn/system/resource/tsites/tsitesencrypt.jsp?id=_tsites_encryp_tsothercontact_tsccontent&content={}&mode=8'.format(dict_lianxifangshi.get('邮箱','-'))).text)['content']
            # 联系方式总结
            dict_contact_information = {
                '邮编':zip_code,
                '办公地址':office_address,
                '办公室电话':office_phone,
                '移动电话':mobile_phone,
                '邮箱':email,
            }
            # 个人简介:
            personal_profile = html.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]//p/text()')[0]
            # 个人教育
            education_experience = ''.join(html.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]//dl//text()')).replace('&nbsp','').replace('\n','').replace(' ','')
            # 工作经历
            work_experience = ''.join(html.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[2]//dl//text()')).replace('&nbsp','').replace('\n','').replace(' ','')
            all_xinxi = {
                '个人信息':personal_information,
                '联系方式':dict_contact_information,
                '个人简介':personal_profile,
                '个人教育':education_experience,
                '工作经历':work_experience
            }
        else:
            html.xpath('//div[@class="con1090"]')
            name = html.xpath('/html/body/div[2]/div/div[3]/div[1]/div[1]/div[1]/span/text()')
            gerenxinxi = html.xpath('/html/body/div[2]/div/div[3]/div[1]/div[2]/div//p//text()')
            dict_gerenxinxi = {i.split('：')[0]: i.split('：')[1] for i in gerenxinxi}
            #  = html.xpath('/html/body/div[2]/div/div[3]/div[1]/div[2]/div/p[1]/text()')
            # sex = gerenxinxi1.xpath('//p[1]/text()')
            print(name)
            print(dict_gerenxinxi)
            # print(sex)

            #dict_gerenxinxi = {i.split('：')[0]: i.split('：')[1] for i in gerenxinxi}
    except Exception as err:
        pass


if __name__ == '__main__':
    get_data()
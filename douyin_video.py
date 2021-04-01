# -*- encoding=utf8 -*-

import requests
import json
import os

def get_video_url():


    count = 21
    #是否有下一页
    has_more = True
    #下一页
    max_cursor = 0
    video_list = []
    sec_uid = 'MS4wLjABAAAAq7ZG19rMoAb9xfPI_Z0aGWTKvMx5xd-KTR_a8gRoKKY'
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'accept':'application/json',
        # 'accept-encoding':'gzip, deflate, br',
        # 'accept-language':'zh-CN,zh;q=0.9',
        'x-requested-with':'XMLHttpRequest',
        'referer':'https://www.iesdouyin.com/share/user/60351935698?u_code=19618i997&sec_uid=MS4wLjABAAAA6c6_1FhEvI8puPhfany3BZxT3v1_05jNUXze22meTFE&did=MS4wLjABAAAA0kC1aOYBSevkeY06xHsgu1A8IJ8eh2W5m9CoR2PdziQ&iid=MS4wLjABAAAAZWwJlOh8B41FLDE35vxFv-GGakGVCk0Q3ChyEQhnLfRlmRAYyZDHLNKkISNY7jSi&with_sec_did=1&timestamp=1617175452&utm_source=copy&utm_campaign=client_share&utm_medium=android&share_app_name=douyin',

    }

    a = 1
    while has_more:
        url = 'https://www.iesdouyin.com/web/api/v2/aweme/post/?sec_uid='+str(sec_uid)+'&count='+str(count)+'&max_cursor='+str(max_cursor)+'&aid=1128&_signature=cz.ukgAAE1tXDHip08dT5HM.7o&dytk='

        resp = requests.get(url,headers=headers).content.decode(encoding='utf-8')

        result = json.loads(resp)

        #True
        has_more = result['has_more']
        #下一页

        # print(result)
        videos = result['aweme_list']

        for video in videos:

            title = video['desc']
            vdurl = video['video']['play_addr']['url_list'][0]

            down_video(a,title,vdurl)
            print('正在下载第%s个视频.....' % a)
            a += 1
            video_list.append(vdurl)
        video_list = list(set(video_list))
        # print(len(video_list))
        if has_more:
            max_cursor = result['max_cursor']
        else:
            break

def down_video(a,title,vdurl):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    }

    try:
        os.mkdir(os.path.dirname(os.path.abspath(__file__)) + './' + 'douyin_wulin')
    except:
        ...
    res = requests.get(vdurl, headers=headers).content
    with open("douyin_wulin/"+"%s.mp4"%a,'wb+') as tp:

        tp.write(res)


get_video_url()

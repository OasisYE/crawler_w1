from urllib import request,parse
import requests
import json

def Tran1(keyword):
    '''
    使用userlib 爬取有道翻译信息
    :param keyword:
    :return:
    '''
    base_url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc'

    # 构建请求对象
    data = {
        'i': keyword,
        "doctype": "json"
    }
    data = parse.urlencode(data) #编码转换

    # headers = {
    #     #'Content-Length': len(data)
    #     'Connection':'keep-alive'
    # }

    req = request.Request(url=base_url, data=bytes(data, encoding='utf-8'))
    res = request.urlopen(req)


    str_json = res.read().decode('utf-8')  # 获取响应的json字串

    myjson = json.loads(str_json)  # 把json转字典

    info = myjson['translateResult'][0][0]['tgt']
    print(info)

def Tran2(keyword):
    '''
    使用requests爬取有道翻译信息
    :param keyword:
    :return:
    '''
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc'

    # 定义请求参数
    data = {
        'i': keyword,
        "doctype": "json"
    }

    # 发送请求，抓取信息
    res = requests.post(url,data=data)

    # 解析结果并输出
    str_json = res.content.decode('utf-8') # 获取响应的json字串
    myjson = json.loads(str_json) # 把json转字典
    info = myjson['translateResult'][0][0]['tgt']
    print(info)

if __name__ == '__main__':
    while True:
        keyword = input('输入翻译的单词：')
        if keyword == 'q':
            break
        Tran2(keyword)
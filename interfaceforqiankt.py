import requests
import  json  

def test():
    #公用数据
    url = 'http://api.qkt.qianjifang.com.cn/'
    phone = '18506826613'

    #发送验证码
    Codetype =1
    apiurl=url+'api/SMS/Send/Code'
    payload = {"Phone":phone,"CodeType":Codetype,"Domain":'sss'}
    headers = {"Content-Type":"application/json"}
    r = requests.post(url=apiurl,data = json.dumps(payload),headers = headers)
    print('发送验证码',r.status_code)

    #登录
    code = '1234'
    apiurl = url+'api/Token'
    payload = {"grant_type":'phonecode', "phone": phone,"code":code}
    r = requests.post(url=apiurl, data = payload)
    session = r.json()["token_type"]+" "+r.json()["access_token"]
    print('登录',r.status_code)
    


if  __name__ == '__main__':
    test()

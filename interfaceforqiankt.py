import requests
import  json  
import xlrd,xlwt
import time
import datetime

def test():
    url = 'http://api.qkt.qianjifang.com.cn/'
    Origin = 'http://test.qkt.qianjifang.com.cn'
    companyid='FD6E54FE-0E31-4041-885B-C012BC7DD763'
    phone = '18506826613'

    #发送验证码(SMS)
    Codetype =1
    apiurl=url+'api/SMS/Send/Code'
    payload = {"Phone":phone,"CodeType":Codetype,"Domain":'sss'}
    headers = {"Content-Type":"application/json"}
    r = requests.post(url=apiurl,data = json.dumps(payload),headers = headers)
    testprint('发送验证码',r.status_code,r.text)

    # time.sleep(1)

    #验证验证码（Verify）
    code = '1234'
    apiurl = url+'api/Verify/Code'
    headers = {"Content-Type":"application/json"}
    payload = {"codeType":1, "phone": phone,"code":code}
    r = requests.get(url=apiurl, params = payload)
    testprint('验证验证码',r.status_code)

    time.sleep(1)

    #登录
    code = '1234'
    apiurl = url+'api/Token'
    payload = {"grant_type":'phonecode', "phone": phone,"code":code}
    r = requests.post(url=apiurl, data = payload)
    testprint('登录',r.status_code)
    session = r.json()["token_type"]+" "+r.json()["access_token"]
    userid = r.json()["id"]

    # time.sleep(1)

    # #获取当前会员信息(Customer)
    # apiurl = url+'api/Customer'
    # headers = {'Content-Type': "application/json",'Authorization':session,"Origin":Origin}
    # r = requests.get(url=apiurl, headers = headers)
    # testprint('获取当前会员信息',r.status_code)

    # time.sleep(1)

    # #获取当前会员ID111(Customer)
    # apiurl = url+'api/Customer/id'
    # headers = {'Content-Type': "application/json",'Authorization':session,"Origin":Origin}
    # payload = {"id": userid}
    # r = requests.get(url=apiurl, headers = headers,params= json.dumps(payload))
    # testprint('获取当前会员ID111',r.status_code,r.text)
    # customerid = r.json()["id"]

    # time.sleep(1)

    # #获取当前会员ID222(Customer)
    # apiurl = url+'api/Customer'
    # headers = {'Content-Type': "application/json",'Authorization':session,"Origin":Origin}
    # payload = {"id": userid}
    # r = requests.get(url=apiurl, headers = headers,params= json.dumps(payload))
    # testprint('获取当前会员ID222',r.status_code)
    # customerid = r.json()["id"]

    time.sleep(1)

    #增加客户(Client)
    apiurl = url +'api/Client'
    headers = {'Content-Type': "application/json",'Authorization':session,"Origin":Origin}
    payload = {"display": "客户3号","phone": "18506826613","level":'' }
    r = requests.post(url=apiurl, headers = headers,data = json.dumps(payload))
    testprint('增加客户',r.status_code,r.text)
    clientid = r.json()["id"]

    # time.sleep(1)

    # #更新客户等级(Client)
    # apiurl = url +'api/Client/{0}/Level'.format(clientid)
    # headers = {'Content-Type': "application/json",'Authorization':session,"Origin":Origin}
    # payload = {"Level":4}
    # r = requests.post(url=apiurl, headers = headers,data = json.dumps(payload))
    # testprint('更新客户等级',r.status_code,r.text)

    # time.sleep(1)

    #更新客户备注(Client)
    apiurl = url +'api/Client/{0}/Remarks'.format(clientid)
    headers = {'Content-Type': "application/json",'Authorization':session,"Origin":Origin}
    payload = {"remarks":'哈哈哈哈'}
    r = requests.post(url=apiurl, headers = headers,data = json.dumps(payload))
    testprint('更新客户备注',r.status_code,r.text)
    

    # time.sleep(1)

    # #获取所有客户信息(Client)
    # apiurl = url+'api/Client'
    # headers = {'Content-Type': "application/json",'Authorization':session,"Origin":Origin}
    # r = requests.get(url=apiurl, headers = headers)
    # testprint('获取所有客户信息',r.status_code,r.text)

    # time.sleep(1)

    # #获取单个客户信息(Client)
    # apiurl = url+'api/Client'
    # headers = {'Content-Type': "application/json",'Authorization':session,"Origin":Origin}
    # payload = {"remarks":'哈哈哈哈'}
    # r = requests.get(url=apiurl, headers = headers,params= payload)
    # testprint('获取单个客户信息',r.status_code,r.text)

    # time.sleep(1)

    # #获取维护客户数(Client)
    # apiurl = url+'api/Client/Maintain/Number'
    # headers = {'Content-Type': "application/json",'Authorization':session,"Origin":Origin}
    # r = requests.get(url=apiurl, headers = headers)
    # testprint('获取维护客户数',r.status_code,r.text)

    # time.sleep(1)

    # #客户维护(Client)
    # apiurl = url+'api/Client/Maintain'
    # headers = {'Content-Type': "application/json",'Authorization':session,"Origin":Origin}
    # payload = [{"id":clientid,"display":"qqq"}]
    # r = requests.post(url=apiurl, headers = headers,data = json.dumps(payload) )
    # testprint('客户维护',r.status_code,r.text)

    # time.sleep(1)

    # #获取维护消息(Client)
    # apiurl = url+'api/Client/SmsMessage'
    # headers = {'Content-Type': "application/json",'Authorization':session,"Origin":Origin}
    # payload = {"CompanyNumber":companyid}
    # r = requests.get(url=apiurl, headers = headers,params=payload)
    # testprint('获取维护消息',r.status_code,r.text)

    # time.sleep(1)
    # #客户意向（Client）
    # apiurl = url+'api/Client/AddIntention?CompanyNumber={CompanyNumber}'

    # time.sleep(1)

    # #增加事件(Event)
    # apiurl = url+'api/Event/Add'
    # headers = {'Content-Type': "application/json",'Authorization':session,"Origin":Origin}
    # payload = {"Clients":[clientid],"title":'增加了一个很大的事件',"TriggerTime":"2019-07-26 19:21:34.723","Cycle":1}
    # r = requests.post(url = apiurl, headers = headers,data = json.dumps(payload))
    # testprint('增加事件',r.status_code,r.text)
    # EventId = r.json()[0]["id"]

    # time.sleep(1)
    
    # #获取所有事件详情(Event)
    # apiurl = url+'api/Event'
    # headers = {'Content-Type': "application/json",'Authorization':session,"Origin":Origin}
    # r = requests.get(url = apiurl, headers = headers)
    # testprint('获取所有事件详情',r.status_code,r.text)

    # time.sleep(1)

    # #获取事件详情(Event)
    # apiurl = url+'api/Event'
    # headers = {'Content-Type': "application/json",'Authorization':session,"Origin":Origin}
    # payload = {"clientId":clientid}
    # r = requests.get(url = apiurl, headers = headers,params=payload )
    # testprint('获取所有事件详情',r.status_code,r.text)

    # time.sleep(1)

    # #删除事件(Event)
    # apiurl = url+'api/Event/Delete/{0}'.format(EventId)
    # headers = {'Content-Type': "application/json",'Authorization':session,"Origin":Origin}
    # r = requests.post(url = apiurl, headers = headers)
    # testprint('删除事件',r.status_code)

def testprint(name,code,text=''):
    print(code,name)
    

if  __name__ == '__main__':
    test()

import unittest
import ddt
from common import ReadExcl,ReadDB
import ReadConfig 
import requests
import  json 

sheet_name = "ClientMaintain"
api='api/Client/Maintain'

excel = ReadExcl.Xlrd()

@ddt.ddt
class TestClientMaintain(unittest.TestCase): 
    def setUp(self):
        """
        :return:
        """

    def tearDown(self):
        """
        :return:
        """

    @ddt.data(*excel.get_xls_next(sheet_name))
    def test_ClientMaintain(self, data):
        readdb = ReadDB.Pymssql()
        excel = ReadExcl.Xlrd()
        readconfig=ReadConfig.ReadConfig()
        #填写求求参数
        url = readconfig.get_url('url')+api
        session =  readconfig.get_member('session')
        origin = readconfig.get_url('origin')
        headers = {'Content-Type': "application/json",'Authorization':session,"Origin":origin}
        readdb.SetCustomerMoney(str(data["money"]),readconfig.get_member('userid'))
        if data['isone']:
            payload = [{"id":readconfig.get_client('clientid2'),"display":"qqq"}]
        else:
            payload = [{"id":readconfig.get_client('clientid3'),"display":"qqq"},{"id":readconfig.get_client('clientid4'),"display":"qqq"}]
        r = requests.post(url=url, headers = headers,data = json.dumps(payload))

        #处理请求数据到excl用例文件
        excel.set_cell(sheet_name,int(data["case_id"]),excel.get_sheet_colname(sheet_name)["result_code"],r.status_code,excel.set_color(r.status_code))
        excel.set_cell(sheet_name,int(data["case_id"]),excel.get_sheet_colname(sheet_name)["result_msg"],r.text,excel.set_color())
        excel.save()
        
        if r.status_code==200 or r.status_code==204:
            orderprice = readdb.GetClientMaintainOrder(r.json()['orderId'])
            usermoney = readdb.GetUserMoney(readconfig.get_member('userid'))
            self.assertEqual(orderprice,usermoney,data["case_describe"])
        self.assertEqual(r.status_code,data['expected_code'],data["case_describe"])


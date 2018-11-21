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
        self.readdb = ReadDB.Pymssql()
        self.excel = ReadExcl.Xlrd()
        self.readconfig=ReadConfig.ReadConfig()

    def tearDown(self):
        """
        :return:
        """

    @ddt.data(*excel.get_xls_next(sheet_name))
    def test_ClientMaintain(self, data):
        #填写求求参数
        print(str(data["money"]))
        url = self.readconfig.get_url('url')+api
        session =  self.readconfig.get_member('session')
        origin = self.readconfig.get_url('origin')
        headers = {'Content-Type': "application/json",'Authorization':session,"Origin":origin}
        self.readdb.SetCustomerMoney(str(data["money"]),self.readconfig.get_member('userid'))
        # payload = {"display": str(data["display"]),"phone": str(data["phone"]),"level": str(data["level"])}
        # r = requests.post(url=url, headers = headers,data = json.dumps(payload))

        # #处理请求数据到excl用例文件
        # self.excel.set_cell(sheet_name,int(data["case_id"]),self.excel.get_sheet_colname(sheet_name)["result_code"],r.status_code,self.excel.set_color(r.status_code))
        # self.excel.set_cell(sheet_name,int(data["case_id"]),self.excel.get_sheet_colname(sheet_name)["result_msg"],r.text,self.excel.set_color())
        # self.excel.save()
        
        # if r.status_code==200 or r.status_code==204:
        #     print('111')
 
        # self.assertEqual(r.status_code,data['expected_code'],data["case_describe"])


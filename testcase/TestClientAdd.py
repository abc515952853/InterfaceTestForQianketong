import unittest
import ddt
from common import ReadExcl,ReadDB
import ReadConfig 
import requests
import  json 

sheet_name = "ClientAdd"
api='api/Client'

excel = ReadExcl.Xlrd()

@ddt.ddt
class TestClientAdd(unittest.TestCase): 
    def setUp(self):
        """
        :return:
        """

    def tearDown(self):
        """
        :return:
        """

    @ddt.data(*excel.get_xls_next(sheet_name))
    def test_ClientAdd(self, data):
        excel = ReadExcl.Xlrd()
        readconfig=ReadConfig.ReadConfig()
        readdb = ReadDB.Pymssql()
        
        #填写求求参数
        url = readconfig.get_url('url')+api
        session =  readconfig.get_member('session')
        origin = readconfig.get_url('origin')
        headers = {'Content-Type': "application/json",'Authorization':session,"Origin":origin}
        payload = {"display": str(data["display"]),"phone": str(data["phone"]),"level": str(data["level"])}
        r = requests.post(url=url, headers = headers,data = json.dumps(payload))

        #处理请求数据到excl用例文件
        excel.set_cell(sheet_name,int(data["case_id"]),excel.get_sheet_colname(sheet_name)["result_code"],r.status_code,excel.set_color(r.status_code))
        excel.set_cell(sheet_name,int(data["case_id"]),excel.get_sheet_colname(sheet_name)["result_msg"],r.text,excel.set_color())
        excel.save()
        
        if r.status_code==200 or r.status_code==204:
            self.assertIn('id', r.json(),data["case_describe"]) 
            clientinfo = readdb.GetClientinfo(r.json()['id'])
            self.assertEqual(clientinfo['display'],str(data["display"]),data["case_describe"])
            self.assertEqual(clientinfo['level'],data['level'],data["case_describe"])
            self.assertEqual(clientinfo['phone'],str(data["phone"]),data["case_describe"])
            self.assertEqual(clientinfo['companyId'],readconfig.get_member('companyId'),data["case_describe"])
            self.assertEqual(clientinfo['customerId'],readconfig.get_member('customerId'),data["case_describe"])

            readconfig.set_client('clientid',r.json()['id'])
 
        self.assertEqual(data['expected_code'],r.status_code,data["case_describe"])


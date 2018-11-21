import unittest
import ddt
from common import ReadExcl,ReadDB
import ReadConfig 
import requests
import  json 

sheet_name = "ClientRemarks"
api='api/Client/{0}/Remarks'

excel = ReadExcl.Xlrd()

@ddt.ddt
class TestClientRemarks(unittest.TestCase): 
    def setUp(self):
        """
        :return:
        """

    def tearDown(self):
        """
        :return:
        """

    @ddt.data(*excel.get_xls_next(sheet_name))
    def test_ClientRemarks(self, data):
        excel = ReadExcl.Xlrd()
        readconfig=ReadConfig.ReadConfig()
        readdb = ReadDB.Pymssql()
        
        #填写求求参数
        url = readconfig.get_url('url')+api.format(readconfig.get_client('clientid1'))
        session =  readconfig.get_member('session')
        origin = readconfig.get_url('origin')
        headers = {'Content-Type': "application/json",'Authorization':session,"Origin":origin}
        payload = {"remarks": str(data["remarks"])}
        r = requests.post(url=url, headers = headers,data = json.dumps(payload))

        #处理请求数据到excl用例文件
        excel.set_cell(sheet_name,int(data["case_id"]),excel.get_sheet_colname(sheet_name)["result_code"],r.status_code,excel.set_color(r.status_code))
        excel.set_cell(sheet_name,int(data["case_id"]),excel.get_sheet_colname(sheet_name)["result_msg"],r.text,excel.set_color())
        excel.save()
        
        if r.status_code==200 or r.status_code==204: 
            clientinfo = readdb.GetClientinfo(readconfig.get_client('clientid1'))
            self.assertEqual(clientinfo['remarks'],str(data['remarks']),data["case_describe"])
        self.assertEqual(r.status_code,data['expected_code'],data["case_describe"])


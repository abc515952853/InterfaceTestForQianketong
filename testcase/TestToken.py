import unittest
import ddt
from common import ReadExcl
import ReadConfig 
import requests
import  json 

sheet_name = "Token"
api='api/Token'

excel = ReadExcl.Xlrd()

@ddt.ddt
class TestToken(unittest.TestCase): 
    def setUp(self):
        """
        :return:
        """

    def tearDown(self):
        """
        :return:
        """

    @ddt.data(*excel.get_xls_next(sheet_name))
    def test_Token(self, data):
        excel = ReadExcl.Xlrd()
        readconfig=ReadConfig.ReadConfig()
        #填写求求参数
        url = readconfig.get_url('url')+api
        payload = {"grant_type":str(data["grant_type"]),"phone":str(data["phone"]),"code":str(data["code"])}
        r = requests.post(url=url, data = payload)
        #处理请求数据到excl用例文件
        excel.set_cell(sheet_name,int(data["case_id"]),excel.get_sheet_colname(sheet_name)["result_code"],r.status_code,excel.set_color(r.status_code))
        excel.set_cell(sheet_name,int(data["case_id"]),excel.get_sheet_colname(sheet_name)["result_msg"],r.text,excel.set_color())
        excel.save()
        #存储数据到本地config数据文件
        if r.status_code==200 or r.status_code ==204:
            session = r.json()["token_type"]+" "+r.json()["access_token"]
            readconfig.set_member('session',session)
            readconfig.save()
        self.assertEqual(r.status_code,data['expected_code'],data["case_describe"])

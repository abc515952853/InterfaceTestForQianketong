import unittest
import ddt
from common import ReadExcl
import ReadConfig 
import requests
import  json 

sheet_name = "CodeVerify"
api='api/Verify/Code'

excel = ReadExcl.Xlrd()

@ddt.ddt
class TestCodeVerify(unittest.TestCase): 
    def setUp(self):
        """
        :return:
        """


    def tearDown(self):
        """
        :return:
        """

    @ddt.data(*excel.get_xls_next(sheet_name))
    def test_CodeVerify(self, data):
        readconfig=ReadConfig.ReadConfig()
        excel = ReadExcl.Xlrd()

        #填写求求参数
        url = readconfig.get_url('url')+api
        payload = {"phone":str(data["phone"]),"codeType":int(data["type"]),"code":str(data["code"])}
        r = requests.get(url=url,params = payload)

        # 处理请求数据到excl用例文件
        excel.set_cell(sheet_name,int(data["case_id"]),excel.get_sheet_colname(sheet_name)["result_code"],r.status_code,excel.set_color(r.status_code))
        excel.set_cell(sheet_name,int(data["case_id"]),excel.get_sheet_colname(sheet_name)["result_msg"],r.text,excel.set_color(r.status_code))
        excel.save()
        
        self.assertEqual(r.status_code,data['expected_code'],data["case_describe"])

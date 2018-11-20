import unittest
import ddt
from common import ReadExcl
import ReadConfig 
import requests
import  json 

sheet_name = "CodeSend"
api='api/SMS/Send/Code'

excel = ReadExcl.Xlrd()

@ddt.ddt
class TestCodeSend(unittest.TestCase): 
    def setUp(self):
        """
        :return:
        """

    def tearDown(self):
        """
        :return:
        """

    @ddt.data(*excel.get_xls_next(sheet_name))
    def test_CodeSend(self, data):
        excel = ReadExcl.Xlrd()
        readconfig=ReadConfig.ReadConfig()
        
        #填写求求参数h
        url = readconfig.get_url('url')+api
        payload = {"Phone":str(data["phone"]),"CodeType":int(data["type"]),"Domain":'sss'}
        headers = {"Content-Type":"application/json"}
        r = requests.post(url=url,data = json.dumps(payload),headers = headers)
        #处理请求数据到excl用例文件
        excel.set_cell(sheet_name,int(data["case_id"]),excel.get_sheet_colname(sheet_name)["result_code"],r.status_code,excel.set_color(r.status_code))
        excel.set_cell(sheet_name,int(data["case_id"]),excel.get_sheet_colname(sheet_name)["result_msg"],r.text,excel.set_color())
        excel.save()
        
        #存储数据到本地config数据文件
        if r.status_code==200 or r.status_code ==204:
            readconfig.set_member('phone',str(data['phone']))
            readconfig.save()
        self.assertEqual(data['expected_code'],r.status_code,data["case_describe"])

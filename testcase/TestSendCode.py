import unittest
import ddt
from common import ReadExcl
import ReadConfig 
import requests
import  json 

sheet_name = "SendCode"

excel = ReadExcl.Xlrd()

@ddt.ddt
class TestSendCode(unittest.TestCase): 
    def setUp(self):
        """
        :return:
        """

    def tearDown(self):
        """
        :return:s
        """

    @ddt.data(*excel.get_xls_next(sheet_name))
    def test_Sencode(self, data):
        excel = ReadExcl.Xlrd()
        readconfig=ReadConfig.ReadConfig()
        payload = {"Phone":str(data["phone"]),"CodeType":int(data["type"]),"Domain":'sss'}
        headers = {"Content-Type":"application/json"}
        r = requests.post(url='http://api.qkt.qianjifang.com.cn/api/SMS/Send/Code',data = json.dumps(payload),headers = headers)
        excel.set_cell(sheet_name,int(data["case_id"]),excel.get_sheet_colname(sheet_name)["result_code"],excel.get_sheet_colname(sheet_name)["result_msg"],r.status_code,r.text,excel.set_color())
        excel.save()
        if r.status_code==204:
            readconfig.set_member('phone',str(data['phone']))
            readconfig.save()
        self.assertEqual(data['expected_code'],r.status_code)

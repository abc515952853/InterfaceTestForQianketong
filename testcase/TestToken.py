import unittest
import ddt
from common import ReadExcl
import ReadConfig 
import requests
import  json 

sheet_name = "Token"

excel = ReadExcl.Xlrd()

@ddt.ddt
class TestToken(unittest.TestCase):
    def setUp(self):
        """
        :return:
        """

    def tearDown(self):
        """
        :return:s
        """

    @ddt.data(*excel.get_xls_next(sheet_name))
    def test_Token(self, data):
        excel = ReadExcl.Xlrd()
        readconfig=ReadConfig.ReadConfig()

        payload = {"grant_type":'code', "username": data['username'],"password":data['password']}
        r = requests.post(url='http://api.hhx.qianjifang.com.cn/api/Token', data = payload)
        excel.set_cell(sheet_name,int(data["case_id"]),excel.get_sheet_colname(sheet_name)["result_code"],excel.get_sheet_colname(sheet_name)["result_msg"],r.status_code,r.text)
        excel.save()
        if r.status_code==200:
            session = r.json()["token_type"]+" "+r.json()["access_token"]
            readconfig.set_member('session',session)
        self.assertEqual(data['expected_code'],r.status_code)
    
    
    
    
    
    
    

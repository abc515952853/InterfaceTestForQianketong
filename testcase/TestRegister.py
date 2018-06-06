import unittest
import ddt
from common import ReadExcl
import ReadConfig 
import requests
import  json 

sheet_name = "Register"

excel = ReadExcl.Xlrd()

@ddt.ddt
class TestRegister(unittest.TestCase):
    def setUp(self):
        """
        :return:
        """

    def tearDown(self):
        """
        :return:s
        """

    @ddt.data(*excel.get_xls_next(sheet_name))
    def test_Register(self, data):
        excel = ReadExcl.Xlrd()
        readconfig=ReadConfig.ReadConfig()
        payload = {"Number":  data['Number'], "TjNumber": data['TjNumber'],"phone":str(data["phone"]),"code":str(data["code"])}
        headers = {"Content-Type":"application/json"} 
        r = requests.post(url='http://api.hhx.qianjifang.com.cn/api/Account/Register',data = json.dumps(payload),headers = headers)
        excel.set_cell(sheet_name,int(data["case_id"]),excel.get_sheet_colname(sheet_name)["result_code"],excel.get_sheet_colname(sheet_name)["result_msg"],r.status_code,r.text)
        excel.save()
        if r.status_code==204:
            readconfig.set_member('phone',str(data['phone']))
            readconfig.set_member('mrename',str(data['Number']))
            readconfig.set_member('mtjid',str(data['TjNumber']))
        self.assertEqual(data['expected_code'],r.status_code)
    
    
    
    
    
    
    

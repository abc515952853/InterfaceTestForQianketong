import unittest
import ddt
from common import ReadExcl
import ReadConfig 
import requests
import  json 

class TestHome(unittest.TestCase):    
    def setUp(self):
        """
        :return:
        """
    
    def tearDown(self):
        """
        :return:
        """

    def test_Account(self):
        readconfig=ReadConfig.ReadConfig()
        headers = {"Content-Type":"application/json","Authorization":readconfig.get_member("session")} 
        r = requests.get(url='http://api.hhx.qianjifang.com.cn/api/Home',headers = headers)
        self.assertEqual(200,r.status_code)
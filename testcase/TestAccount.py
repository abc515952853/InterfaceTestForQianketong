import unittest
import ddt
from common import ReadExcl
import ReadConfig 
import requests
import  json 

class TestAccount(unittest.TestCase):
    def setUp(self):
        """
        :return:
        """

    def tearDown(self):
        """
        :return:s
        """

    def test_Account(self):
        readconfig=ReadConfig.ReadConfig()
        r = requests.get(url='http://api.hhx.qianjifang.com.cn/api/Account')
        # if r.status_code == 200:
        #     readconfig.set_member('mrename',r.json())
        #     readconfig.save()
        self.assertEqual(200,r.status_code)

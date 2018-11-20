import unittest
import ddt
from common import ReadExcl,ReadDB
import ReadConfig 
import requests
import  json 

api='api/Customer'
case_describe = '获取会员信息'

class Customer(unittest.TestCase): 
    def setUp(self):
        """
        :return:
        """

    def tearDown(self):
        """
        :return:
        """

    def test_Customer(self):
        readconfig=ReadConfig.ReadConfig()
        readdb = ReadDB.Pymssql()

        url = readconfig.get_url('url')+api
        session =  readconfig.get_member('session')
        origin = readconfig.get_url('origin')
        headers = {'Content-Type': "application/json",'Authorization':session,"Origin":origin}
        r = requests.get(url=url, headers = headers)
        if r.status_code==200:
            self.assertIn('id', r.json()) 
            customerinfo = readdb.GetCustomer(readconfig.get_member('phone'))
            self.assertEqual(r.json()['userId'],customerinfo['userid'],case_describe) 
            self.assertEqual(r.json()['nickname'],customerinfo['nickname'],case_describe) 
            self.assertEqual(r.json()['companyName'],customerinfo['companyshort'],case_describe) 
            self.assertEqual(r.json()['id'],customerinfo['customerid'],case_describe) 
            readconfig.set_member('customerid',customerinfo['customerid'])
            readconfig.set_member('companyid',customerinfo['companyid'])
        else:
            self.assertEqual(200,r.status_code,case_describe)                    

        

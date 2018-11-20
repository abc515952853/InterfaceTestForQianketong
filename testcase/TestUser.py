import unittest
import ddt
from common import ReadExcl,ReadDB
import ReadConfig 
import requests
import  json 

api='api/User'
case_describe = '获取用户信息'

class User(unittest.TestCase): 
    def setUp(self):
        """
        :return:
        """

    def tearDown(self):
        """
        :return:
        """

    def test_User(self):
        readconfig=ReadConfig.ReadConfig()
        readdb = ReadDB.Pymssql()

        url = readconfig.get_url('url')+api
        session =  readconfig.get_member('session')
        origin = readconfig.get_url('origin')
        headers = {'Content-Type': "application/json",'Authorization':session,"Origin":origin}
        r = requests.get(url=url, headers = headers)
        if r.status_code==200:
            self.assertIn('id', r.json()) 
            userinfo = readdb.GetUser(readconfig.get_member('phone'))
            self.assertEqual(r.json()['id'],userinfo['userid'],case_describe) 
            self.assertEqual(r.json()['nickname'],userinfo['nickname'],case_describe) 
            self.assertEqual(r.json()['blogId'],userinfo['blogid'],case_describe)
            self.assertEqual(r.json()['customerId'],userinfo['customerid'],case_describe)
            readconfig.set_member('userid',userinfo['userid'])
        else:
            self.assertEqual(200,r.status_code,case_describe)                   

        

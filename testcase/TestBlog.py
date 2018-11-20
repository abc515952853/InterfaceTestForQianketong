import unittest
import ddt
from common import ReadExcl,ReadDB
import ReadConfig 
import requests
import  json 

api='api/Blog'
case_describe = '获取主页信息'

class Blog(unittest.TestCase): 
    def setUp(self):
        """
        :return:
        """

    def tearDown(self):
        """
        :return:
        """

    def test_Blog(self):
        readconfig=ReadConfig.ReadConfig()
        readdb = ReadDB.Pymssql()

        url = readconfig.get_url('url')+api
        session =  readconfig.get_member('session')
        origin = readconfig.get_url('origin')
        headers = {'Content-Type': "application/json",'Authorization':session,"Origin":origin}
        r = requests.get(url=url, headers = headers)
        if r.status_code==200:
            self.assertIn('id', r.json(),case_describe) 
            customerinfo = readdb.GetBlog(readconfig.get_member('phone'))
            self.assertEqual(r.json()['id'],customerinfo['blogid'],case_describe) 
            self.assertEqual(r.json()['phone'],customerinfo['phone'],case_describe) 
            self.assertEqual(r.json()['companyName'],customerinfo['companyName'],case_describe) 
            self.assertEqual(r.json()['nickname'],customerinfo['nickname'],case_describe) 
            readconfig.set_member('blogid',customerinfo['blogid'])
        else:
            self.assertEqual(200,r.status_code,case_describe)   
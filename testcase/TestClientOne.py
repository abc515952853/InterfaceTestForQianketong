import unittest
import ddt
from common import ReadExcl,ReadDB
import ReadConfig 
import requests
import  json 

api='api/Client'
case_describe = '获取单个客户'

class ClientOne(unittest.TestCase): 
    def setUp(self):
        """
        :return:
        """

    def tearDown(self):
        """
        :return:
        """

    def test_ClientOne(self):
        readconfig=ReadConfig.ReadConfig()
        readdb = ReadDB.Pymssql()

        url = readconfig.get_url('url')+api
        session =  readconfig.get_member('session')
        origin = readconfig.get_url('origin')
        headers = {'Content-Type': "application/json",'Authorization':session,"Origin":origin}
        r = requests.get(url=url, headers = headers)
        if r.status_code==200:
            clientinfo = readdb.GetClientinfo(readconfig.get_client('clientid1'))
            self.assertEqual(r.json()[0]['display'],clientinfo['display'],case_describe)
            self.assertEqual(r.json()[0]['level'],clientinfo['level'],case_describe)
            self.assertEqual(r.json()[0]['status'],clientinfo['status'],case_describe)

        else:
            self.assertEqual(r.status_code,200,case_describe)   
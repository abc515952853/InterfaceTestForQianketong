import unittest
import ddt
from common import ReadExcl,ReadDB
import ReadConfig 
import requests
import  json 

api='api/Client'
case_describe = '获取所有客户'

class ClientAll(unittest.TestCase): 
    def setUp(self):
        """
        :return:
        """

    def tearDown(self):
        """
        :return:
        """

    def test_ClientAll(self):
        readconfig=ReadConfig.ReadConfig()
        readdb = ReadDB.Pymssql()

        url = readconfig.get_url('url')+api
        session =  readconfig.get_member('session')
        origin = readconfig.get_url('origin')
        headers = {'Content-Type': "application/json",'Authorization':session,"Origin":origin}
        r = requests.get(url=url, headers = headers)
        if r.status_code==200:
            clientallid = readdb.GetClientAllinfo(readconfig.get_member('customerid'))
            responeclientallid = []
            for i in range(len(r.json())):
                responeclientallid.append(r.json()[i]['id'])
                self.assertIn(r.json()[i]['id'],clientallid,case_describe)
            self.assertEqual(len(responeclientallid),len(clientallid),case_describe)
        else:
            self.assertEqual(r.status_code,200,case_describe)   
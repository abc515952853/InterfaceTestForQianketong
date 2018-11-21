import unittest
import ddt
from common import ReadExcl,ReadDB
import ReadConfig 
import requests
import  json 

api='api/Client/Maintain/Number'
case_describe = '获取客户维护数量信息'

class ClientMaintainNumber(unittest.TestCase): 
    def setUp(self):
        """
        :return:
        """

    def tearDown(self):
        """
        :return:
        """

    def test_ClientMaintainNumber(self):
        readconfig=ReadConfig.ReadConfig()
        readdb = ReadDB.Pymssql()

        url = readconfig.get_url('url')+api
        session =  readconfig.get_member('session')
        origin = readconfig.get_url('origin')
        headers = {'Content-Type': "application/json",'Authorization':session,"Origin":origin}
        r = requests.get(url=url, headers = headers)
        if r.status_code==200 or r.status_code == 204:
            maintainnumber = readdb.GetClientMaintainNumber(readconfig.get_member('customerid'))
            self.assertEqual(r.json()['maintainNumber'],maintainnumber,case_describe)            
        else:
            self.assertEqual(r.status_code,200,case_describe)                   

        

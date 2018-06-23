#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#doc:https://github.com/coinexcom/coinex_exchange_api/wiki/

import time
import hashlib
import json
import requests

class Client(object):

    def __init__(self,access_id,secret_key):
        self.access_id = access_id
        self.secret_key = secret_key
        self.headers = {'Content-Type': 'application/json; charset=utf-8'}

    def get_sign(self, params):
        sort_params = sorted(params)
        data = []
        for item in sort_params:
            data.append(item + '=' + str(params[item]))
        str_params = "{0}&secret_key={1}".format('&'.join(data), self.secret_key)
        token = hashlib.md5(str.encode(str_params)).hexdigest().upper()
        return token

    def balance(self,symbol='USDT'):
        url = 'https://api.coinex.com/v1/balance/'
        tonce = int(time.time() * 1000)
        params = {'access_id': self.access_id, 'tonce': tonce}
        self.headers['AUTHORIZATION'] = self.get_sign(params)
        resp = requests.get(url,headers=self.headers,params=params).text
        try:
            resp_dict = json.loads(resp)
            return resp_dict['data'][symbol]['available']
        except:
            raise Exception

    def put_limit(self,symbol,type,amount,price):
        url = 'https://api.coinex.com/v1/order/limit'
        tonce = int(time.time() * 1000)
        params = {'access_id':self.access_id,
                'market':symbol.upper(),
                'type':type,
                'amount':str(amount),
                'price':str(price),
                'tonce':tonce
                }
        self.headers['AUTHORIZATION'] = self.get_sign(params)
        resp = requests.post(url,headers=self.headers,data=json.dumps(params)).text
        try:
            resp_dict = json.loads(resp)
            return resp_dict['data']['id']
        except:
            raise Exception

    def cancel_order(self,symbol,id):
        url = 'https://api.coinex.com/v1/order/pending'
        tonce = int(time.time() * 1000)
        params = {'access_id':self.access_id,
                'id':int(id),
                'market':symbol,
                'tonce':tonce
                }
        self.headers['AUTHORIZATION'] = self.get_sign(params)
        resp = requests.delete(url,headers=self.headers,params=params).text
        try:
            resp_dict = json.loads(resp)
            return resp_dict['message']
        except:
            raise Exception

    @staticmethod
    def get_price(symbol,asks_or_bids):
        url = 'https://api.coinex.com/v1/market/depth'
        resp_json = requests.get(url, params={'market': symbol, 'limit': 1, 'merge': 0}).text
        try:
            resp_dict = json.loads(resp_json)
            price = resp_dict['data'][asks_or_bids][0][0]
            return price
        except:
            raise Exception
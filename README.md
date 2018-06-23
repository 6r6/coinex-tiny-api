# CoinEX Api
> 非官方 / Unofficial


## Usage
```python
#填写你的key和secret
c = Client('#','#')

#获取账户余额。可选参数为BTC/BCH/USDT，成功则返回数量
print(c.balance('BCH'))

#根据深度图获取卖1价格,asks/bids
print(c.get_price('CETBCH','asks'))
print(c.get_price('CETBCH','bids'))

#限价交易。交易对symbol:CETUSDT，type:sell/buy，成功则返回订单ID
print(c.put_limit('CETBCH','buy','100','0.0000230'))

#取消订单,成功返回文本"Ok"
print(c.cancel_order('CETBCH','500300500'))
```

***
**请注意，代码未经完整测试，风险自担 / Use at your own risk**

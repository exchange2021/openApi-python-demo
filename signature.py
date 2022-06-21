import hmac
import json
import requests
import time

#拼接签名
#meet the signature
def preHash(timestamp, method, requestPath, queryString, body):
    #拼接签名
    pre = timestamp + method + requestPath
    if queryString.strip() != '':
        pre = pre + '?' +queryString.strip()
    if body.strip() != '':
        pre = pre + body.strip()
    print(pre)
    return pre

#生成签名
#generate signature
def toSign(timestamp, method, requestPath, queryString, body, secretKey):
    return hmac.new(secretKey.encode('UTF-8'),
                    preHash(timestamp, method, requestPath, queryString, body).encode('UTF-8'),
                    "SHA256").hexdigest()

# 输入的您的apiKey和secretKey
# Enter your apiKey and secretKey
apikey = 'xxx'
secret = 'xxx'

if __name__ == '__main__':

# get请求
# get request
    #设置OpenApi调用的域名url
    #set the domain url for calling OpenApi
    url = "https://openapi.xxx.com/sapi/v1/account"
    current = str(round(time.time() * 1000))

    #生成签名
    # generate signature
    sign = toSign(current, 'GET', '/sapi/v1/account', '', '', secret)

    #构造Headers
    # Construct Headers
    getheaders = {
        'X-CH-APIKEY': apikey,
        'X-CH-TS': current,
        'Content-Type': 'application/json',
        'X-CH-SIGN': sign
    }

    response = requests.get(url=url, headers=getheaders)
    print(response.text.encode('utf8'))




#post请求
#post request
    # 设置OpenApi调用的域名url
    # set the domain url for calling OpenApi
    url = "https://openapi.xxx.com/sapi/v1/order"
    current = str(round(time.time() * 1000))
    param = json.dumps({"symbol":"xxx","volume":"1","side":"SELL","price":"1","type":"LIMIT"})

    # 生成签名
    # generate signature
    sign = toSign(current, 'POST', '/sapi/v1/order', '', param, secret)

    # 构造Headers
    # Construct Headers
    postHeaders = {
        'X-CH-APIKEY': apikey,
        'X-CH-TS': current,
        'Content-Type': 'application/json',
        'X-CH-SIGN': sign
    }
    response = requests.post(url=url, headers=postHeaders, data=param)
    print(response.text.encode('utf8'))








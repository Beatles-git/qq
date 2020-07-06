import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="gb18030")
import requests


def qcd_requests(url,data,method='post',token=None):
    token = {'X-Lemonban-Media-Type': 'lemonban.v2',
                  'Authorization': token}
    if method=='get':
        result=requests.get(url,json=data,headers=token)
        print(result.json())
        return result.json()
    else:
        result = requests.post(url, json=data, headers=token)
        return result.json()


# if __name__ == '__main__':
#     #登录数据
#     log_url = 'http://120.78.128.25:8766/futureloan/member/login'
#     log_data = {
#         "mobile_phone": "15815541780",
#         "pwd": "lemon123456"
#     }
#     #发起登录请求
#     result=qcd_requests(log_url,log_data)
#     #返回result提取token值
#     token=result['data']['token_info']['token']
#     print(result)
#     print('token值是：',token)
#     #充值数据
#     rec_url='http://120.78.128.25:8766/futureloan/member/recharge'
#     rec_data={
#       "member_id": "206792",
#       "amount": "500000"
#     }
#     qcd_requests(rec_url,rec_data,'post','Bearer '+token)
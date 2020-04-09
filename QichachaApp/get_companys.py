# import sys,os
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# print(sys.path)

from qichacha_api.client import RequestClient

appKey = '27e678686c9444c1a2f55cda49e099b8'
secret_key = '747CE52A7158E3C7F50C2DD25FA71744'

if __name__ == "__main__":
    rc = RequestClient(appKey=appKey, secret_key=secret_key)
    res = rc.get_details_by_name("上海物通农业发展有限公司")
    print(res)
    # print(res.content)
    # print(res.text)
    print("查询完毕")
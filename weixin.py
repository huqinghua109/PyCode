
import time
import requests
import json

MYCORPID = 'ww94dd7702f69e2a5c'
MYSECRET = 'x7UsuHkj35C_Y5vn6MaoitLdGe3hoJSon_zjmK8mlDs'
TOWHO = 'HuQingHua'
AGENTID = 1000003

class WeChat:
    def __init__(self):
        self.CORPID = MYCORPID
        self.CORPSECRET = MYSECRET
        self.AGENTID = AGENTID
        self.TOUSER = TOWHO  # 接收者用户名

    def _get_access_token(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        values = {'corpid': self.CORPID,
                  'corpsecret': self.CORPSECRET,
                  }
        req = requests.post(url, params=values)
        data = json.loads(req.text)
        # print(data)
        return data["access_token"]

    def get_access_token(self):
        try:
            with open('./access_token.conf', 'r') as f:
                t, access_token = f.read().split()
        except:
            with open('./access_token.conf', 'w') as f:
                access_token = self._get_access_token()
                cur_time = time.time()
                f.write('\t'.join([str(cur_time), access_token]))
                return access_token
        else:
            cur_time = time.time()
            if 0 < cur_time - float(t) < 7260:
                return access_token
            else:
                with open('./access_token.conf', 'w') as f:
                    access_token = self._get_access_token()
                    f.write('\t'.join([str(cur_time), access_token]))
                    return access_token

    def send_data(self, message):
        msg = message.encode('UTF-8')
        send_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + self.get_access_token()
        send_values = {
            "touser": self.TOUSER,
            "msgtype": "text",
            "agentid": self.AGENTID,
            "text": {
                "content": msg
                },
            "safe": 0
            }
        send_data = '{"msgtype": "text", "safe": "0", "agentid": %s, "touser": "%s", "text": {"content": "%s"}}' % (self.AGENTID, self.TOUSER, msg)
        r = requests.post(send_url, send_data)
        print(r.content)
        return r.content


if __name__ == '__main__':
    wx = WeChat()
    msg = '%s:python-test' % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    wx.send_data(msg)
    print('over')
import requests


class ZhouNuan(object):
    CorpID = 'wx7cc2586b6e9016a7'
    contact_secret = 'jTleq3LLvrz0ovJllHcLJMDDPP2-I4faj5JyGoYf9IQ'

    url = 'https://qyapi.weixin.qq.com/cgi-bin'

    def __init__(self):
        pass

    def _get_token(self, secret):
        resp = requests.get(self.url + '/gettoken?corpid=%s&corpsecret=%s'
                            % (self.CorpID, secret))

        json_ = resp.json()
        if json_['errcode']:
            raise ValueError(resp.text)
        else:
            return json_['access_token']

    def get_contact_token(self):
        return self._get_token(self.contact_secret)

    def get_users(self, department_id):
        token = self.get_contact_token()
        resp = requests.get(self.url + '/user/list?access_token=%s&department_id=%s&fetch_child=1' %
                            (token, department_id))
        json_ = resp.json()
        if json_['errcode']:
            raise ValueError(resp.text)
        else:
            return json_

    def get_all_users(self):
        return self.get_users(1)

    def login_by_qr(self):
        pass

    def get_redirect(self, agent_id):
        return 'https://open.work.weixin.qq.com/wwopen/sso/qrConnect?' + \
               'appid=' + self.CorpID + '&agentid=' + str(agent_id) + \
               '&redirect_uri=http://miss-fish.com&state=web_login@gyoss9'

    def get_code(self, agent_id):
        return 'https://open.weixin.qq.com/connect/oauth2/authorize?appid=%s&redirect_uri=%s&response_type=code&scope=snsapi_privateinfo&agentid=%s''#wechat_redirect' % (self.CorpID, 'http://miss-fish.com', agent_id)


zn = ZhouNuan()
print(zn.get_contact_token())

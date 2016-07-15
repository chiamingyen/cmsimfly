from authomatic.providers import oauth2

# 希望設計流程來保全 consumer_key 與 consumer_secret 字串
CONFIG = {
        'google': {
            'class_': oauth2.Google,
            'consumer_key': '418441298841-hcbnnh847rq735sg92digsjlk3vf489a.apps.googleusercontent.com',
            'consumer_secret': 'wjj5f_N4UxLZ83L3m1XkMB60',
            #'scope': oauth2.Google.user_info_scope
            # 以下將只檢視(瞭解您在 Google 上的身分)與(檢視電子郵件地址)
            'scope': ['email']
        }
    }
import os
# 確定程式檔案所在目錄, 在 Windows 有最後的反斜線
_curdir = os.path.join(os.getcwd(), os.path.dirname(__file__))
# 若在 uwsgi 模式執行, 則 uwsgi 必須改為 True
uwsgi = False
# 設定在 uwsgi 與近端的資料儲存目錄
config_dir = _curdir + "/config/"
static_dir = _curdir + "/static"
class Init(object):
    def __init__(self):
        # hope to create downloads and images directories　
        if not os.path.isdir(_curdir+"/downloads"):
            try:
                os.makedirs(_curdir+"/downloads")
            except:
                print("mkdir error")
        if not os.path.isdir(_curdir+"/images"):
            try:
                os.makedirs(_curdir+"/images")
            except:
                print("mkdir error")



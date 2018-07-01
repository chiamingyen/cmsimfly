#!/usr/bin/python
# 導入 os 模組, 主要用來判斷是否以 uwsgi 或一般近端模式執行
import os
# 導入同目錄下的 flaskapp.py
import flaskapp
import ssl

# 即使在近端仍希望以 https 模式下執行
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('localhost.crt', 'localhost.key')

# 以下開始判斷在 uwsgi 模式或近端執行, 相關設定在 init.py 中
# 目前有多重位置設定 uwsgi, 必須整合一下
uwsgi = False
if uwsgi:
    # 表示程式在雲端執行
    application = flaskapp.app
else:
    # 表示在近端執行, 以 python3 wsgi.py 執行
    flaskapp.app.run(host='127.0.0.1', port=9443, debug=True, ssl_context=context)


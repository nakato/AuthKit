﻿# -*- coding: utf-8 -*-

from authkit.authenticate import middleware, sample_app

app = middleware(
    sample_app,
    setup_method='form,cookie',
    cookie_secret='secret encryption string',
    form_authenticate_user_data = """
        الإعلاني:9406649867375c79247713a7fb81edf0
        username2:4e64aba9f0305efa50396584cfbee89c
    """,
    form_authenticate_user_encrypt = 'authkit.users:md5',
    form_authenticate_user_encrypt_secret = 'some secret string',
    form_charset='UTF-8',
    cookie_signoutpath = '/signout',
)

if __name__ == '__main__':
    from paste.httpserver import serve
    serve(app, host='0.0.0.0', port=8080)
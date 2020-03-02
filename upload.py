
# -*- coding: utf-8 -*-
# flake8: noqa
from qiniu import Auth, put_file, etag
import qiniu.config
import os
import glob
#需要填写你的 Access Key 和 Secret Key
access_key = 'aj2RE5fZURXVzSTiBCAXoryLJEzf3lw-ggXXlc_A'
secret_key = 'OIy6qtCuJf71njFth0iovanfi7ZU_q1alW15vKCg'
#构建鉴权对象
q = Auth(access_key, secret_key)
#要上传的空间
bucket_name = 'swyoung-photo'


def upload_file(file):
    #上传后保存的文件名
    key = file
   # print("file:"+file)
   # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, key, 3600)
    #要上传文件的本地路径
    localfile = file;
   # print("localfile:"+localfile)
    ret, info = put_file(token, key, localfile)
    print(info)
    assert ret['key'] == key
    assert ret['hash'] == etag(localfile)


def upload_dir():
    #要上传的文件夹
    upload_dir = 'photos_tmp/'
    for img in glob.glob(upload_dir+"*"):
        upload_file(img)
    upload_dir = 'min_photos_tmp/'
    for img in glob.glob(upload_dir+"*"):
        upload_file(img)


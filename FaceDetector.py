#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import abstractmethod
from aip import AipFace
import base64
from Config import baiduAI

import cv2

class FaceDetector(object):
    @abstractmethod
    def run(self, image):
        return NotImplemented
        

class BaiduFaceDetector(FaceDetector):
    """docstring for BaiduFaceDetector"""
    def __init__(self, options=None):
        self._options = options
        self._client = AipFace(baiduAI['APP_ID'], baiduAI['API_KEY'], baiduAI['SECRET_KEY'])
        
    def run(self, image):
        print('Detecting ...')

        cv2.imwrite('./01.png', image)

        ret = {}
        img = None
        with open('./01.png', 'rb') as fp:
            img = fp.read()
            image64 = base64.b64encode(img)
            ret = self._client.detect(image64, "BASE64")
            print(ret)

        return {
            'frame': img,
            'error_msg': ret['error_msg'],
            'location': ret['result']['face_list'][0]['location'] if self.successDetectFace(ret) else None
        }

    @staticmethod
    def successDetectFace(ret):
        return ret and (ret['error_msg'] == 'SUCCESS')

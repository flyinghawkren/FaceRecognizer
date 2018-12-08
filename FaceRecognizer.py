#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import abstractmethod
from aip import AipFace
import base64
from Config import baiduAI

class FaceRecognizer(object):
    @abstractmethod
    def run(self, image):
        return NotImplemented

class BaiduFaceRecognizer(FaceRecognizer):
    """docstring for BaiduFaceDetector"""
    def __init__(self, options=None):
        self._options = options
        self._client = AipFace(baiduAI['APP_ID'], baiduAI['API_KEY'], baiduAI['SECRET_KEY'])
        
    def run(self, image):
        print('Recognizing ...')
        image64 = base64.b64encode(image)
        ret = self._client.detect(image64, "BASE64", None)
        return ret

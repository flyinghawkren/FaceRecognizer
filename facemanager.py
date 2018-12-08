#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from aip import AipFace
import base64
from Config import baiduAI

class BaiduFaceManager(object):
    def __init__(self):
        self._client = AipFace(baiduAI['APP_ID'], baiduAI['API_KEY'], baiduAI['SECRET_KEY'])

    def addFace(self, name, imgFile):
        print('Add Face for {0}.'.format(name))

        with open(imgFile, 'rb') as fp:
            img = fp.read()
            image64 = base64.b64encode(img)

            ret = self._client.addUser(image64, "BASE64", baiduAI['GROUP'], name)
            print(ret)

    def updateFace(self, name, imgFile):
        print('Update Face for {0}.'.format(name))

        with open(imgFile, 'rb') as fp:
            img = fp.read()
            image64 = base64.b64encode(img)

            ret = self._client.faceDelete(image64, "BASE64", baiduAI['GROUP'], name)
            print(ret)

    def deleteFace(self, name):
        print('Update Faces for {0}.'.format(name))
        ret = self._client.deleteUser(baiduAI['GROUP'], name)
        print(ret)

def argsParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action='version', version='1.0.0')
    subparsers = parser.add_subparsers()

    def addFace(args):
        BaiduFaceManager().addFace(args.name, args.image)

    def updateFace(args):
        BaiduFaceManager().updateFace(args.name, args.image)

    def deleteFace(args):
        BaiduFaceManager().deleteFace(args.name)

    add_parser = subparsers.add_parser('add')
    add_parser.add_argument('name', help='name of the person to add')
    add_parser.add_argument('image', help='image of the person to add')
    add_parser.set_defaults(func=addFace)

    update_parser = subparsers.add_parser('update')
    update_parser.add_argument('name', help='name of the person to update')
    update_parser.add_argument('image', help='image of the person to update')
    update_parser.set_defaults(func=updateFace)

    delete_parser = subparsers.add_parser('delete')
    delete_parser.add_argument('name', help='name of the person to delete')
    delete_parser.set_defaults(func=deleteFace)

    return parser

if __name__ == '__main__':
    parser = argsParser()
    args = parser.parse_args()
    args.func(args)

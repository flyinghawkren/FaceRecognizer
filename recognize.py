#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rx.subjects import Subject

from FaceDetector import BaiduFaceDetector
from FaceRecognizer import BaiduFaceRecognizer
from Capture import VideoCapture

def main():
    subject = Subject()
    capture = VideoCapture(subject)

    def show_result(result):
        print(result)
        capture.setResult(result)

    def on_error(err):
        print('Error ocured:', err)


    detector = BaiduFaceDetector()
    recognizer = BaiduFaceRecognizer()

    newframe = subject.throttle_last(2000) \
        .map(lambda frame: detector.run(frame)) \
        .filter(lambda x: detector.successDetectFace(x)) \
        .map(lambda x: recognizer.run(x)) \
        .subscribe(show_result, on_error)

    capture.run()

if __name__ == '__main__':
    main()
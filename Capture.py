#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2

class VideoCapture(object):
    """docstring for VideoCapture"""
    def __init__(self, subject):
        super(VideoCapture, self).__init__()
        self._subject = subject

    def run(self):
        cap = cv2.VideoCapture(0)

        # 设置分辨率
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        fps = cap.get(cv2.CAP_PROP_FPS)

        frameIdx = 0

        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()
            frameIdx += 1
            if frameIdx == fps * 2:
                frameIdx = 0
                self._subject.on_next(frame)

            # Display the resulting frame
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()
        
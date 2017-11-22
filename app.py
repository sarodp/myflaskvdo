#!/usr/bin/env python
from importlib import import_module
import os
from flask import Flask, render_template, Response

#--import camera driver
#if os.environ.get('CAMERA'):
#    Camera = import_module('camera_' + os.environ['CAMERA']).Camera
#else:
#    from camera import Camera

#--Raspberry Pi camera module (requires picamera package)
# from camera_pi import Camera

#--Raspberry Pi pygame usb.camera 
from camera_pygame import Camera



app = Flask(__name__)


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen(xcamera):
    """Video streaming generator function."""
    
    while True:
        xframe = xcamera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + xframe + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    #app.run(host='0.0.0.0', threaded=True)
	app.run(host='192.168.1.24', port=5000, debug=True,threaded=True)

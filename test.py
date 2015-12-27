import picamera

camera = picamera.PiCamera()
camera.capture('image.jpg')
camera.start_preview()
#camera.stop_preview()

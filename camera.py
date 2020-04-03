import picamea
from subprocess import call

# Setup the camera such that it closes when we are done with it
Print("About to take a picture")
with picamera.Picamera() as camera:
	camera.resolution = (3280,2464)
	camera.capture("/home/pi/Desktop/cookie/newimage.jpg")
Print("Picture taken." )

def getTime():
	#Fetch the current time
	currentTime = datetime.now()
	return currentTime
# Setup the camera
with picamera.Picamera() as camera:
	#Start recording
	camera.start_recording("pythonVedio.h264")
	sleep(5)
	# Stop recording
	camera.stop_recording()
Print("We are going to convert the vedio")
# Define the command we want to execute.
command = "MP4Box" - add pythonVedio.h264 convertedVedio.mp4"
# Execute our command
call([command], shell=True)
# Vedio converted.
Print("Vedio converted.")

# Our timestamp's message
Print("About to timestamp our picture.")
timestampMessage = "Check out this message!"
# Specify the command we want to call
timestampCommand = "/usr/bin/convert " + fileName + " -pointsize 32 \
-fill red -annotate +700+500 '" + timestampMessage + "' " +fileName
# Execute our command
call([timestampCommand], shell=True)
print("Picture has been timestamped")

From picamera import PiCamera
From time import sleep
camera = PiCamera()
for i in range(5):
camera.start_preview()
sleep(5)
camera.cature(("/home/pi/Desktop/cookie/newimage.jpg"))
camera.stop_preview()








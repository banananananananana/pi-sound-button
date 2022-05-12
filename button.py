import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def ronja(channel):
  print("RONJA TRYKKEDE PÅ KNAPPEN!")
  exec(open("reandom.py").read())

def thor(channel):
  print("THOR TRYKKEDE PÅ KNAPPEN!")
  exec(open("captain.py").read())

GPIO.add_event_detect(15, GPIO.FALLING, callback=ronja, bouncetime=5000)
GPIO.add_event_detect(14, GPIO.FALLING, callback=thor, bouncetime=5000)

input("READY")

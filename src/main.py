from m5stack import *
from m5ui import *
from uiflow import *
import time
from easyIO import *

setScreenColor(0x000000)

contador = None
alert = None
total = None

label_contador = M5TextBox(93, 25, "30", lcd.FONT_DejaVu72, 0xFFFFFF, rotate=90)
label_total = M5TextBox(49, 159, "170", lcd.FONT_DejaVu18, 0xfbf96b, rotate=90)
line0 = M5Line(M5Line.PLINE, 25, 141, 84, 141, 0xFFFFFF)
line1 = M5Line(M5Line.PLINE, 47, 141, 106, 141, 0xffffff)
label_battery = M5TextBox(128, 206, "100", lcd.FONT_Default, 0xFFFFFF, rotate=90)

def update_contador():
  global contador, alert, total
  if contador <= total and contador > 0:
    contador = contador - 1
  else:
    alert = True

def update_total():
  global contador, alert, total
  contador = total
  alert = False

def update_display():
  global contador, alert, total
  label_contador.setText(str(contador))
  label_total.setText(str(total))
  if alert == True:
    active_alert()
  else:
    deactive_alert()

def active_alert():
  global contador, alert, total
  label_contador.setColor(0xff0000)
  for count in range(3):
    M5Led.on()
    speaker.tone(800, 200)
    wait_ms(80)
    M5Led.off()

def deactive_alert():
  global contador, alert, total
  label_contador.setColor(0xffffff)

def setup_device():
  global contador, alert, total
  speaker.setVolume(10)
  axp.setLcdBrightness(40)
  label_battery.setText(str((str((map_value((axp.getBatVoltage()), 3.7, 4.1, 0, 100))) + str('%'))))

setup_device()
contador = 21
total = 30
update_display()
while True:
  if btnB.isPressed():
    update_contador()
    update_display()
  if btnA.isPressed():
    update_total()
    update_display()
  wait_ms(2)

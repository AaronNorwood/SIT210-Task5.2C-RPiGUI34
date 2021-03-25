import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.core.window import Window
import RPi.GPIO as GPIO


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

blueLED = 40
greenLED = 38
redLED = 36

GPIO.setup(blueLED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(greenLED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(redLED, GPIO.OUT, initial=GPIO.LOW)

def toggleLED(ledPin):
    GPIO.output(ledPin, not GPIO.input(ledPin))

#def setLEDs(ledOn, ledOff1, ledOff2):
    #GPIO.output(ledOn, GPIO.HIGH)
    #GPIO.output(ledOff1, GPIO.LOW)
    #GPIO.output(ledOff2, GPIO.LOW)

#class toggleButton(FloatLayout):
    #pass

class GridLayout(GridLayout):
   
    def setLEDs(self, ledOn, ledOff1, ledOff2):
        GPIO.output(ledOn, GPIO.HIGH)
        GPIO.output(ledOff1, GPIO.LOW)
        GPIO.output(ledOff2, GPIO.LOW)
   
    def Exit(self):
        App.get_running_app().stop()
        Window.close()
   
class LEDToggleApp(App):
    def build(self):
        return GridLayout()

#class FloatLayoutApp(App):
 #   def build(self):
  #      return FloatLayout()
if __name__ == '__main__':
    LEDApp = LEDToggleApp()
    LEDApp.run()

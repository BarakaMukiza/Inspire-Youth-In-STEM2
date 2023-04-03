import machine
import time
from machine import Pin, I2C    
from ssd1306 import SSD1306_I2C
#import framebuf
from machine import Pin
from time import sleep
from dht import DHT22




interrupt_flag=0
interrupt_flag2=0
settings_button = Pin(5,Pin.IN,Pin.PULL_UP)
weather_button  = Pin(4,Pin.IN,Pin.PULL_UP)


WIDTH  = 128                                         
HEIGHT = 64                                            
i2c = I2C(0) 

print("I2C Address      : "+hex(i2c.scan()[0]).upper()) 
print("I2C Configuration: "+str(i2c))                  
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c) 


rtc = machine.RTC()
#setting time
rtc.datetime((2023, 3, 16, 11, 2, 0, 0, 0)) # set a specific date and
   

red_led =    machine.Pin(12, machine.Pin.OUT)
blue_led =   machine.Pin(13, machine.Pin.OUT)
yellow_led = machine.Pin(14, machine.Pin.OUT)

#button = Pin(4, Pin.IN)
red_button = machine.Pin(6, machine.Pin.IN, machine.Pin.PULL_UP)
blue_button = machine.Pin(6, machine.Pin.IN, machine.Pin.PULL_UP) 
yellow_button = machine.Pin(6, machine.Pin.IN, machine.Pin.PULL_UP) 


light_sensor = machine.ADC(machine.Pin(28))     # create ADC object on ADC pin
# creating a DHT object
dht = DHT22(Pin(18)) 
def callback(settings_button):
    global interrupt_flag
    interrupt_flag=1
settings_button.irq(trigger=Pin.IRQ_FALLING, handler=callback)

def callback(weather_button):
    global interrupt_flag2
    interrupt_flag2=1
weather_button.irq(trigger=Pin.IRQ_FALLING, handler=callback)

def home():
  oled.fill(0)
  timestamp=rtc.datetime()
  datestring="%04d-%02d-%02d "%(timestamp[0:3])
  timestring ="%02d:%02d:%02d"%(timestamp[4:7])
  oled.text("Smart Home",5,5)   
  oled.text(datestring,5,30)           
  oled.text(timestring,5,50)
  oled.show()       

def settings():
  oled.fill(0)
  oled.text("",5,5)   
  oled.text("Network :",5,15)           
  oled.text("UserName  :",5,35)       
  oled.text("Time :",5,45)
  oled.show()

def weather():
  oled.fill(0)
  # getting sensor readings
  dht.measure()
  temp = dht.temperature()
  hum = dht.humidity()
    # displaying values to the console
  print("Temperature: {}°C   Humidity: {:.0f}% ".format(temp, hum))  
  oled.text("Nairobi",10,0)   
  oled.text("Temp :",5,15) 
  oled.text(str(temp),60,15)           
  oled.text("Hum  :",5,35)       
  oled.text(str(hum),60,35) 
  oled.show()          
home()

#connected button to 3.3v
while True:
  if interrupt_flag is 1:  #button to react when you press it
        settings()
        sleep(5)
        interrupt_flag=0
  elif interrupt_flag is 0:
    home()
  
  if interrupt_flag2 is 1:
        weather()
        sleep(5)
        interrupt_flag2=0
  elif interrupt_flag2 is 0:
    home()

  light_value = light_sensor.read_u16()
  print("Light Intensity :",light_value)
  print("\n\n")
  print("Date ",rtc.datetime()) 
  print("\n\n")
  red_button_state = red_button.value()
  print("Button state", red_button_state) #high / low
  red_led.value(red_button_state)

  blue_button_state = blue_button.value()
  print("Button state", blue_button_state) #high / low
  blue_led.value(blue_button_state)

  yellow_button_state = yellow_button.value()
  print("Button state", yellow_button_state) #high / low
  yellow_led.value(yellow_button_state)
  
    # delay of 2 secs for the reading of the sensor
  #sleep(2)
    

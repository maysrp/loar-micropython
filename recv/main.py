from config import *
from machine import Pin, SPI,I2C
from sx127x import SX127x
from ssd1306 import SSD1306_I2C
device_spi = SPI(baudrate = 10000000, 
        polarity = 0, phase = 0, bits = 8, firstbit = SPI.MSB,
        sck = Pin(device_config['sck'], Pin.OUT, Pin.PULL_DOWN),
        mosi = Pin(device_config['mosi'], Pin.OUT, Pin.PULL_UP),
        miso = Pin(device_config['miso'], Pin.IN, Pin.PULL_UP))

lora = SX127x(device_spi, pins=device_config, parameters=lora_parameters)
i2c=I2C(0,sda=Pin(16), scl=Pin(17), freq=400000) 
oled = SSD1306_I2C(128, 64, i2c) 

# 接收数据
while True:
    if lora.received_packet():
        lora.blink_led()
        payload = lora.read_payload()
        print(payload) #信息
        oled.fill(0)
        oled.text(payload,0,0,1)
        oled.show()


# 发送数据
lora.println("sdfsdfsdf") #发送信息
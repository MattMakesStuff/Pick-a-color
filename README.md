# Pick-a-color
Color-picker changing neopixel leds on a raspberrypi

**Hardware requirements**
A computer with an sd card reader

**What I used**
|Description|Price | Where to buy|
|--|--|--|
| Raspberry Pi 3 | 42.99 | [https://www.amazon.com/CanaKit-Raspberry-Micro-Supply-Listed/dp/B01C6FFNY4](https://www.amazon.com/CanaKit-Raspberry-Micro-Supply-Listed/dp/B01C6FFNY4) |
|Leds | 20.88 | https://www.amazon.com/CHINLY-Individually-Addressable-Waterproof-waterproof/dp/B01LSF4Q00 |
|Breadboard | 8.99 | https://www.amazon.com/LampVPath-12Packs-solderless-breadboard-Arduino/dp/B01KKE602W |
|Jumper wires | 6.98 | https://www.amazon.com/Elegoo-EL-CP-004-Multicolored-Breadboard-arduino/dp/B01EV70C78 |
|Level shifter | 5.95 | https://www.amazon.com/Adafruit-Accessories-Quad-Level-Shifter-piece/dp/B00XW2L39K |
|Total| 85.79 | |

**Cheaper parts**
|Description|Price | Where to buy|
|--|--|--|
| Raspberry Pi Zero | 26.99 | https://www.amazon.com/Vilros-Raspberry-Starter-Power-Premium/dp/B0748MPQT4 |
|Leds | 10.88 | https://www.amazon.com/BTF-LIGHTING-60pixels-Individually-Addressable-Non-waterproof/dp/B01CDTED80 |
|Breadboard | 8.99 | https://www.amazon.com/LampVPath-12Packs-solderless-breadboard-Arduino/dp/B01KKE602W |
|Jumper wires | 6.98 | https://www.amazon.com/Elegoo-EL-CP-004-Multicolored-Breadboard-arduino/dp/B01EV70C78 |
|Level shifter | 5.95 | https://www.amazon.com/Adafruit-Accessories-Quad-Level-Shifter-piece/dp/B00XW2L39K |
|Total| 59.79 | |

**Software requirements**
 - Raspbian
 - Python
 - Neopixel library

**Setup Raspbian**
Install raspbian (Download [here](https://www.raspberrypi.org/downloads/raspbian/) ) onto sd card 
[Installation instructions](https://www.raspberrypi.org/documentation/installation/installing-images/README.md)

**Install neopixel library**

    sudo apt-get update
    sudo apt-get -y install build-essential python-dev git scons swig python-pip
    
    git clone https://github.com/jgarff/rpi_ws281x.git
    cd rpi_ws281x
    scons
    
    cd python
    sudo python setup.py install

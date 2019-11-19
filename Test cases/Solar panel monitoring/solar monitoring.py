from isotel.idm import gateway, monodaq
import pickle
from pathlib import Path
import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os


#
# # For quick access; remote ip adress; username and password is stored at little.secrets pickle. Note! Newer use donwloaded pickle. It can be hacked!
# little_secrets = pickle.load(open(str(Path.home()) + "/little.secrets", "rb" ) )
# remote_ip = little_secrets["remote_ip"]
# user = little_secrets["user"]
# passwd = little_secrets["password"]
#
# # connect to some remote host
# mdu = monodaq.MonoDAQ_U( gateway.Group('http://' + remote_ip + ':33000',
#                                         username=user,
#                                         password=passwd) )
#
#
# # HW setup  -->
# #   J type Thermocouple at pins 5 and 6
# #   2-chn relay wired like following
# #       -> Pin 12 Vcc +5VDC
# #       -> Pin 11 GND
# #       -> Pin 1 relay 1 enable
# #       -> Pin 3 relay 2 enable
# # Show hw setup picture
# img=mpimg.imread('https://github.com/Wenlin88/MonoDAQ-U-X/blob/master/Examples/HW_setup_1.png?raw=true')
# imgplot = plt.imshow(img)
# plt.axis('off')
# plt.show()
#
#
#
# mdu.reset()
# # Set configuration according HW setup
# mdu['ch.function.function0'] = "Digital Output"
# mdu['ch.function.function2'] = "Digital Output"
# mdu['ch.function.function4'] = "Thermocouple"
# mdu['ch.type.type4'] = "J"
# mdu['ch.function.function13'] = "Power Supply"
#
# # Set initial state for outputs
# mdu['ch.set.set0'] = "1" # Relay will pick with 0, so set let's start from unarmed state
# mdu['ch.set.set2'] = "1"
# mdu['ch.set.set13'] = "5.00"
#
#
# mdu.wait4ready()
# t_measured = mdu['ch.value.value4'] # Temperature measured from J Thermocouple
# print("Thermocouple temperature: " + t_measured + "°C")
#
# v_out_act = mdu['ch.value.value13'] # Actual output voltage
# i_out_act = mdu['ch.value.value12'] # ACtual output current
#
# # Some click clack with relays
# mdu['ch.set.set0'] = "0"
# mdu['ch.set.set2'] = "0"
# # Measure voltage and current when relays are armed
# time.sleep(2) # <-- Let relays to set
# v_out_act = mdu['ch.value.value13']
# i_out_act = mdu['ch.value.value12']
#
# print("Relay supply voltage is " + v_out_act + "V and current " + i_out_act + "mA")
#
#
#
# mdu['ch.set.set0'] = "1"
# mdu['ch.set.set2'] = "1"

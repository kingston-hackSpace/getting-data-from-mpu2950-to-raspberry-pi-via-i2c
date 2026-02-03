#script from the following source (with my anotations)
#https://forums.raspberrypi.com/viewtopic.php?t=263833
import time
import smbus

device = 0x68
who_am_i = 0x75
#these following adresses are specific to the mpu2950
pwr_mgm_1 = 0x6b
smp_div = 0x19
acc_config = 0x1c
acc_config2 = 0x1d
accX_H = 0x3b

i2c = smbus.SMBus(1)

def mpu9250_init():
    i2c.write_byte_data(device, pwr_mgm_1,0x00)#writes a single 8-bit byte to a specific register of an I2C device
    i2c.write_byte_data(device, smp_div,0x00)
    i2c.write_byte_data(device, acc_config ,0x18)
    i2c.write_byte_data(device, acc_config2 ,0x0a)
    
def read_mpu():
   
    raw = i2c.read_i2c_block_data(device, 0x3b,6)#read a contiguous block of data (up to 32 bytes) from a specific register of an I2C device
    ax = (float)((raw[0]<<8|raw[1])) / 2048
    ay = (float)((raw[2]<<8|raw[3])) / 2048
    az = (float)((raw[4]<<8|raw[5])) / 2048
    
    print("x:%.2f  y:%.2f  z:%.2f" %(ax,ay,az))#print the result
    
mpu9250_init()    

while 1:
   
    #i = i2c.read_byte_data(device, 0x75)        
    #print(hex(i))
    read_mpu()
    time.sleep(1)

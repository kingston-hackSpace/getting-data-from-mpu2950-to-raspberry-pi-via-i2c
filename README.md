<h1>How to get data to the raspberry pi via i2c</h1>

<p>This example uses a mpu2950 acceleromenter module and connects it to the raspberry pi using the fritzing diagram attached.

<p>1. Power up the raspberry pi</p>

<p>Bring up a terminal window from the icon in the top left of the menu bar</p>

<p>run the following comand:</p>

```sudo raspi-config```

<p>This will bring up the config menu. Go to Interface options->  I2C Enable loading of kernel module. Choose yes.</p>

<p>install the following dependencies...</p>

```sudo apt-get install -y python3-smbus i2c-tools```

<p>check that the i2c device is present on the board with this command...</p>

```sudo i2cdetect -y 1```

<p>to install the other dependencies you may have to install a virtual environment. Choose a location in the file system and install. Look here for guidance on how to do this...</p>

<link>https://learn.adafruit.com/python-virtual-environment-usage-on-raspberry-pi/basic-venv-usage</link></p>

<p>install the smbs library...</p>

```pip3 install smbus```

<p>load the 'accel_test.py' script to run the mpu2950</p>

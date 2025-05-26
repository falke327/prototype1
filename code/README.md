# Installation on Pi
Before using this script ensure that keyboard is installed on the Pi

```sudo pip3 install keyboard```

The keyboard module requires root access. Start this script with

```sudo python3 main.py```

## Information
The above mentioned keyboard module does not work over ssh. I have to find another solution.

We also have problems with the older RPi.GPIO. I have to switch to lgpio.
On the raspberry I have to

```
sudo apt update
sudo apt install python3-lgpio
```


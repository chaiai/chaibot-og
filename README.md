# ChaiBot

My own tweaks for NVIDIA JetBot to run on a cheap RC car from Walmart: [New Bright RC 4X4 1:15 Bronco Rock Crawler](https://www.walmart.com/ip/New-Bright-RC-4x4-1-15-Scale-Radio-Control-Bronco-Rock-Crawler-2-4GHz/352947836)

<img src="https://user-images.githubusercontent.com/81446209/117052457-bdfe9b00-ace5-11eb-8b8c-7c743470bf13.png" alt="image" width="400"/>

[Hardware setup coming soon!]

## Actual steps I followed:

1. Installed jetson-inference (with PyTorch/torchTRT/some pre-downloaded models)
2. Installed Jupyter and other packages from NVIDIA-AI-IOT/jetcard/install.sh
3. git clone https://github.com/chaiai/chaibot
4. Started Chaibot services:
  - chaibot_stats via utils/create_stats_service.py
  - chaibot_jupyter via utils/create_jupyter_service.py
5. Gave user permissions to I2C group: <code>sudo usermod -aG i2c $USER</code>
6. Updates to code/notebooks zipped and uploaded to chaibot/updates

### Not done yet:
- Editing the notebooks to match controls of new robot
  - **added ChaibotController.py for an easier navigation widget**
  - **trained avoidance model with torchTRT**
- XBox One controller teleoperation
- Ultrasonic/LiDAR sensors for distance
    - LiDAR can go in I2C bus 1 with the PiOLED
    - *take 1 was a failure*
- Arduino UNO with Sensor Shield v5 for servo motor control (and ultrasonic module)
    - needs seperate power supply if using more than 1-2 servos
- Have not attempted to use any object following or TRT models yet

# Pre-installation steps

1. Flash JetPack 4.5.1 image to SD card
2. Go through OEM installation with a monitor, mouse and keyboard attached (important for expanding SD card app directory from 14 GB to the full capacity of the SD card)
3. perform sudo apt update / sudo apt full-upgrade / sudo apt autoremove
4. git clone https://github.com/chaiai/chaibot.git

Once you are connected to your local network and have the IP address (ifconfig from Terminal of Jetson), you can do the following steps with the Jetson directly with the monitor attached, or SSH into your Nano via a suitable client (most OS, including Windows now, have SSH built in to their terminal/command prompt) via <code>ssh username@123.456.1.123 [IP address of the Jetson]</code>

# Bash script for installation

**NOTE: You need to edit the files and enter your password in the top of each of the scripts below to make the script run as I did.**

## Step 1: Install JetBot dependencies

This script is the first half of the JetBot repo's script to create an SD card image from scratch.

I added small tweaks, such as installing update Torch and Torchvision packages

<code>
cd chaibot

./scripts/sd_card_setup.sh
</code>

## Step 2: Install ChaiBot

<code>
cd chaibot
  
./scripts/create_chaibot.sh
</code>

## Connecting to ChaiBot

On another computer, enter the IP address of the Jetson followed by ":8888"

For example: 192.168.1.123:8888

Enter the password for the Jetson and you will have access to the Home directory

## Additional scripts from JetBot

- re-enable-gui.sh will turn the desktop back on if you connect to a display upon next boot.
- create_swap_file.sh will create the swap file with permissions
- configure_jetson.sh will set the power mode and disable the gui

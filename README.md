# ChaiBot

My own tweaks for NVIDIA JetBot to run on a cheap RC car from Walmart: [New Bright RC 4X4 1:15 Bronco Rock Crawler](https://www.walmart.com/ip/New-Bright-RC-4x4-1-15-Scale-Radio-Control-Bronco-Rock-Crawler-2-4GHz/352947836)

<img src="https://user-images.githubusercontent.com/81446209/117052457-bdfe9b00-ace5-11eb-8b8c-7c743470bf13.png" alt="image" width="400"/>

### Not done yet:
- Editing the notebooks to match controls of new robot
- Have not attempted to use any object following or TRT models yet
  -  May need to go back to torch 1.6.0 

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

## Additional scripts from JetBot

- re-enable-gui.sh will turn the desktop back on if you connect to a display upon next boot.
- create_swap_file.sh will create the swap file with permissions
- configure_jetson.sh will set the power mode and disable the gui

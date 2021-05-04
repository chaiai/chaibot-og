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



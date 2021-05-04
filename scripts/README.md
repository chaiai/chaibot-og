# Bash script for installation

## Step 1: Install JetBot dependencies

This script is the first half of the JetBot repo's script to create an SD card image from scratch.

I added small tweaks, such as installing update Torch and Torchvision packages

cd chaibot
./scripts/sd_card_setup.sh

## Step 2: Install ChaiBot

cd chaibot
./scripts/create_chaibot.sh

## Additional scripts from JetBot

- re-enable-gui.sh will turn the desktop back on if you connect to a display upon next boot.
- create_swap_file.sh will create the swap file with permissions
- configure_jetson.sh will set the power mode and disable the gui



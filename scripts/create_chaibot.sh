#!/bin/bash

set -e

password=''

# Record the time this script starts
date
# Get the full dir name of this script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Keep updating the existing sudo time stamp
sudo -v
while true; do sudo -n true; sleep 120; kill -0 "$$" || exit; done 2>/dev/null &

# install requirements for chaibot python module
cd
echo -e "\e[104m Install ChaiBot requirements \e[0m"
sudo apt install -y python3-smbus
cd ~/chaibot
sudo apt install -y cmake
sudo python3 setup.py install 

# Install chaibot services
echo -e "\e[104m Install ChaiBot services \e[0m"
cd chaibot/utils
python3 create_stats_service.py
sudo mv chaibot_stats.service /etc/systemd/system/chaibot_stats.service
sudo systemctl enable chaibot_stats
sudo systemctl start chaibot_stats
python3 create_jupyter_service.py
sudo mv chaibot_jupyter.service /etc/systemd/system/chaibot_jupyter.service
sudo systemctl enable chaibot_jupyter
sudo systemctl start chaibot_jupyter


# install python gst dependencies
echo -e "\e[104m Install Python GST camera requirements \e[0m"
sudo apt install -y \
    libwayland-egl1 \
    gstreamer1.0-plugins-bad \
    libgstreamer-plugins-bad1.0-0 \
    gstreamer1.0-plugins-good \
    python3-gst-1.0
    
# install zmq dependency (should actually already be resolved by jupyter)
sudo -H pip3 install pyzmq
    

# Optimize the system configuration to create more headroom
echo -e "\e[104m Turn off display and maximize power \e[0m"
sudo nvpmodel -m 0
sudo systemctl set-default multi-user
sudo systemctl disable nvzramconfig.service

# Copy JetBot notebooks to home directory
cp -r ~/chaibot/notebooks ~/Notebooks

echo -e "\e[42m All done! \e[0m"

#record the time this script ends
date

#########################################################################
# Most widgets come from the NVIDIA JetBot example Notebooks.
# My implementation creates a widget view for a Notebook with:
#
# 1. Camera instance (600x600 view)
# 2. Motor controls (set to 0.5 speed and without time calls, so the stop button 
#                    needs to be pressed to stop the robot)
# 3. Snapshot button (also creates a snapshot directory at chaibot/snapshots)
# 4. Heartbeat and Period sliders
#
# Call in Notebook via "from ChaibotController import Controller, camera"
# [(camera has to be imported in order to call camera.stop()]
#########################################################################

import os
import time
import traitlets
import ipywidgets.widgets as widgets
from uuid import uuid1
from IPython.display import display
from chaibot import Camera, bgr8_to_jpeg, Heartbeat, heartbeat

camera = Camera.instance(width=224, height=224)
image = widgets.Image(format='jpeg', width=800, height=800)  # this width and height doesn't necessarily have to match the camera
camera_link = traitlets.dlink((camera, 'value'), (image, 'value'), transform=bgr8_to_jpeg)

snapshot_dir = 'chaibot/snapshots'
try:
    os.makedirs(snapshot_dir)
except FileExistsError:
    print('Directories not created because they already exist')

from chaibot import Robot
robot = Robot()

# Heartbeat functions
heartbeat = Heartbeat()

def handle_heartbeat_status(change):
    if change['new'] == Heartbeat.Status.dead:
        robot.stop()

heartbeat.observe(handle_heartbeat_status, names='status')
period_slider = widgets.FloatSlider(description='period', min=0.001, max=0.5, step=0.01, value=0.5)
traitlets.dlink((period_slider, 'value'), (heartbeat, 'period'))


# Motor control buttons
button_layout = widgets.Layout(width='100px', height='80px', align_self='center')
stop_button = widgets.Button(description='stop', button_style='danger', layout=button_layout)
forward_button = widgets.Button(description='forward', layout=button_layout)
backward_button = widgets.Button(description='backward', layout=button_layout)
left_button = widgets.Button(description='left', layout=button_layout)
right_button = widgets.Button(description='right', layout=button_layout)
back_left_button = widgets.Button(description='back left', layout=button_layout)
back_right_button = widgets.Button(description='back right', layout=button_layout)

# Snapshot buttons
snapshot_button = widgets.Button(description='Snapshot', button_style='success', layout=button_layout)
snapshot_count = widgets.IntText(layout=button_layout, value=len(os.listdir(snapshot_dir)))

# display buttons
middle_box = widgets.HBox([left_button, stop_button, right_button], layout=widgets.Layout(align_self='center'))
bottom_box = widgets.HBox([back_left_button, backward_button, back_right_button], layout=widgets.Layout(align_self='center'))
controls_box = widgets.VBox([forward_button, middle_box, bottom_box])

# Motor control functions
def stop(change):
    robot.stop()
    
def step_forward(change):
    robot.forward(0.5)
    #time.sleep(0.5)
    #robot.stop()

def step_backward(change):
    robot.backward(0.5)
    #time.sleep(0.5)
    #robot.stop()

def step_left(change):
    robot.steer_left(0.5)
    #time.sleep(1.0)
    #robot.stop()

def step_right(change):
    robot.steer_right(0.5)
    #time.sleep(1.0)
    #robot.stop()
    
def back_left(change):
    robot.back_left(0.5)
    
def back_right(change):
    robot.back_right(0.5)

# Snapshot functions
def save_snapshot(directory):
    image_path = os.path.join(directory, str(uuid1()) + '.jpg')
    with open(image_path, 'wb') as f:
        f.write(image.value)
    
def take_snapshot():
    global snapshot_dir, snapshot_count
    save_snapshot(snapshot_dir)
    snapshot_count.value = len(os.listdir(snapshot_dir))


# link buttons to actions
stop_button.on_click(stop)
forward_button.on_click(step_forward)
backward_button.on_click(step_backward)
left_button.on_click(step_left)
right_button.on_click(step_right)
back_left_button.on_click(back_left)
back_right_button.on_click(back_right)
snapshot_button.on_click(lambda x: take_snapshot())


# Display all widgets when called
def Controller():
    display(image)
    display(controls_box)
    display(widgets.HBox([snapshot_count, snapshot_button]))
    display(period_slider, heartbeat.pulseout)
    

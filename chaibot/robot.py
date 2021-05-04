import time
import traitlets
from traitlets.config.configurable import SingletonConfigurable
from Adafruit_MotorHAT import Adafruit_MotorHAT
#from adafruit_motorkit import MotorKit
from .motor import Motor


class Robot(SingletonConfigurable):
    
    front_motor = traitlets.Instance(Motor)
    rear_motor = traitlets.Instance(Motor)
    steering_motor = traitlets.Instance(Motor)

    # config
    i2c_bus = traitlets.Integer(default_value=0).tag(config=True)
    front_motor_channel = traitlets.Integer(default_value=1).tag(config=True)
    front_motor_alpha = traitlets.Float(default_value=1.0).tag(config=True)
    rear_motor_channel = traitlets.Integer(default_value=2).tag(config=True)
    rear_motor_alpha = traitlets.Float(default_value=1.0).tag(config=True)
    steering_motor_channel = traitlets.Integer(default_value=3).tag(config=True)
    steering_motor_alpha = traitlets.Float(default_value=1.0).tag(config=True)
    
    def __init__(self, *args, **kwargs):
        super(Robot, self).__init__(*args, **kwargs)
        self.motor_driver = Adafruit_MotorHAT(i2c_bus=self.i2c_bus)
        self.front_motor = Motor(self.motor_driver, channel=self.front_motor_channel, alpha=self.front_motor_alpha)
        self.rear_motor = Motor(self.motor_driver, channel=self.rear_motor_channel, alpha=self.rear_motor_alpha)
        self.steering_motor = Motor(self.motor_driver, channel=self.steering_motor_channel, alpha=self.steering_motor_alpha)
        
    def set_motors(self, front_speed, rear_speed, steering_speed):
        self.front_motor.throttle = front_speed
        self.rear_motor.throttle = rear_speed
        self.steering_motor.steering = steering_speed
        
    def forward(self, speed=1.0, duration=None):
        self.front_motor.throttle = speed
        self.rear_motor.throttle = speed

    def backward(self, speed=1.0):
        self.front_motor.throttle = -speed
        self.rear_motor.throttle = -speed

    def left(self, speed=1.0):
        # Turns the wheels to the left but does not move forward
        # Speed = 1.0 is full left turn 
        self.steering_motor.steering = speed

    def right(self, speed=1.0):
        # Turns the wheels to the right but does not move forward
        # Speed = -1.0 is full right turn
        self.steering_motor.steering = -speed

    def steer_left(self, speed=1.0):
        # Turns wheels to the left and goes forward
        self.steering_motor.steering = speed
        self.front_motor.throttle = speed
        self.rear_motor.throttle = speed

    def steer_right(self, speed=1.0):
        # Turns wheels to the right and goes forward
        self.steering_motor.steering = -speed
        self.front_motor.throttle = speed
        self.rear_motor.throttle = speed

    def back_left(self, speed=1.0):
        # Turns wheels left and goes backwards
        self.steering_motor.steering = speed
        self.front_motor.throttle = -speed
        self.rear_motor.throttle = -speed

    def back_right(self, speed=1.0):
        # Turns wheels right and goes backwards
        self.steering_motor.steering = -speed
        self.front_motor.throttle = -speed
        self.rear_motor.throttle = -speed

    def stop(self):
        self.front_motor.throttle = 0
        self.rear_motor.throttle = 0
        self.steering_motor.steering = 0
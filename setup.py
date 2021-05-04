import glob
import subprocess
from setuptools import setup, find_packages, Extension


def build_libs():
    subprocess.call(['cmake', '.'])
    subprocess.call(['make'])
    

build_libs()


setup(
    name='chaibot',
    version='2',
    description='An implementation of NVIDIAs JetBot by Reid Yonkers',
    packages=find_packages(),
    install_requires=[
        'Adafruit_MotorHAT',
        'adafruit_motorkit',
        'Adafruit-SSD1306',
    ],
    package_data={'chaibot': ['ssd_tensorrt/*.so']},
)
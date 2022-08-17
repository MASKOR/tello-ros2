from setuptools import setup

import os
from glob import glob


package_name = 'tello'

setup(
    name='tello',
    version='0.1.0',
    packages=['tello'],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/tello']),
        ('share/tello', ['package.xml', 'resource/ost.txt', 'resource/ost.yaml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tentone','Patrick Wiesen',
    maintainer_email='tentone@outlook.com','wiesen@fh-aachen.de',
    description='DJI Tello control package for ROS 2',
    license='MIT',
    tests_require=[],
    entry_points={
        'console_scripts': [
            'tello_node = tello.tello_node:main'
        ],
    },
)

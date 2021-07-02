  
from setuptools import setup

setup(
    name='synth_notify',
    version='0.0.1',
    description='Notifies discord webhook with a meme from r/fpga',
    url='https://github.com/nickbeckwith/synthy_notifier_boi',
    author='Nicholas Beckwith',
    author_email='nickbeck@seas.upenn.edu',
    packages=[
        'synth_notify'
    ],
    zip_safe=False,
    install_requires=[
        'discord_webhook',
        'argparse'
    ],
    license='MIT',
    entry_points = {
        'console_scripts': ['synth-notify=synth_notify.command_line:main'],
    }
)
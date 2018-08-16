# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 03:50:08 2018

@author: nitin
"""

# Creating file setup.py
from setuptools import setup

setup(
      name='mti_test',    # This is the name of your PyPI-package.
      version='0.2',                          # Update the version number for new releases
      scripts=['MTIAssignment.py']                  # The name of your scipt, and also the command you'll be using for calling it
)
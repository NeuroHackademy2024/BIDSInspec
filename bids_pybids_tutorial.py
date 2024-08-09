# Project: BIDSInspec
## Objective: Complete the pybids tutorial
# Modified: August 8, 2024 @ 9:08 PM by N.O.

# Implementation via pybids
## Must first complete pybids tutorial to understand the package

# Install pybids via conda
# pip install pybids

# Set up
import os
import bids

# Loading BIDS datasets
from os.path import join
from bids import BIDSLayout
from bids.tests import get_test_data_path
layout = BIDSLayout(join(get_test_data_path(), 'synthetic'))



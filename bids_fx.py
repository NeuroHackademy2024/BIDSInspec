# Project: BIDSInspec
## Objective: Create a function that can query the BIDS directory
# Modified: August 8, 2024 @ 9:08 PM by N.O.

# Implementation via pybids
## Complete pybids tutorial

# Install pybids via conda
## pip install pybids

# Loading BIDS datasets
from bids import BIDSLayout
from bids.tests import get_test_data_path
import os

# Here we're using an example BIDS dataset that's bundled with the pybids tests
data_path = os.path.join(get_test_data_path(), '7t_trt')

# Initialize the layout
layout = BIDSLayout(data_path)

# Print some basic information about the layout
layout



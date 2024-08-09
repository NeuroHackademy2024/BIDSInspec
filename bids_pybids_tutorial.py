# Project: BIDSInspec
## Objective: Complete the pybids tutorial
# Modified: August 8, 2024 @ 9:08 PM by N.O.

# Implementation via pybids
## Must first complete pybids tutorial to understand the package

# Install bids
# pip install bids
# Install pybids
## pip install pybids

# Import
from os.path import join
from bids import BIDSLayout
from bids.tests import get_test_data_path
layout = BIDSLayout(join(get_test_data_path(), 'synthetic'))

# View data
print(layout)
# How many subjects are in the dataset
print(layout.get_subjects())
# How many sessions are in the dataset
print(layout.get_sessions())
# List the types of tasks available
print(layout.get_tasks())

# Extract metadata
# get task timing information for a given fMRI scan # cannot run since bids-dataset does not have NIfTI files
# f = layout.get(task='nback', run=1, extension='nii.gz')[0].filename
#print(layout.get_events(f))

# get metadata from json files # cannot run since bids-dataset does not have NIfTI files
# f = layout.get(task='nback', run=1, extension='nii.gz')[0].filename
# print(layout.get_metadata(f))

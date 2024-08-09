# Project: BIDSInspec
## Objective: Select BIDS directory from bids-examples.git
# Modified: August 8, 2024 @ 9:08 PM by N.O.

## bids-examples.git repository was cloned to local

### Set up Git Branch
# check which branch I am in
git branch
# make new branch
git checkout - b query
# ensure correct branch
git branch

### Move directory ds114 to BIDSInspec
mv /Users/nancy/neurohack24/bids-examples/ds114 /Users/nancy/neurohack24/BIDSInspec

### BIDS validation
# since all raw files within the ds114 dataset are empty, the bids-validator must be 
# configured to not report empty data files as errors
# running command line version start # followed install outlined in github
#https://github.com/bids-standard/bids-validator?tab=readme-ov-file#quickstart
bids-validator ds114 --config.ignore=99 --ignoreNiftiHeaders
## Result: ds114 has 3 warnings ; 1. tabular file has columns not in data dictionary, 2. missing README, 3. no authors within dataset_description.json
    # Summary: 174 files, 103.21KB, 10 subjects, 2 sessions
    # Available tasks:  finger_foot_lips, covert_verb_generation, overt_word_repetition, line_bisection, overt_verb_generation
    # Available modalities: MRI

### Save this file

### Commit to github repo
git status # check what changes need to be commited 
git add . # add the changes to working directory
git commit -m "branch set up and bids validator test" # commit to repo                                                               
                                    
# done
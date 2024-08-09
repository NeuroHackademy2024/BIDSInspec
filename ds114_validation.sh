# Project: BIDSInspec
## Objective: Select BIDS directory from bids-examples.git

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

                                                                        
                                    








# using Docker we can complete the BIDS validator
Docker run -ti --rm -v /Users/nancy/neurohack24/BIDSInspec/ds114:/data:robids/validator /data





### Git Push Steps
Step 0: make new branch
	git checkout -b <branchName>
Step 1: make changes (edits, new file, etc)
Step 2: stage changes for a commit
	git add <filePath>
	git add .
Step 3: commit changes
	git commit -m “messageHere”


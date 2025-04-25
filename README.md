# Thoughtful.ai Platform Tech Screen

## What's been submitted
This project contains two python files - `main.py` which contains my source code for the `sort` function as described in the tech screen spec, and `tests.py` that is a lightweight test file for the `sort` function.

## What I would have done with more time 
I allocated the 30 min to working on this project, but with more time there are a couple items for improvement:

1. Pull constants from `main.py` into their own config file that can be referenced from multiple files (assuming a growing project
would include more business logic that uses these as inputs)
2. I took my best guess at types of input validation needed, but I'd want to hear from the team if we should also validate
other things (e.g. that input values are in a certain range if it's common for incorrect units to be entered)
3. Use a more robust testing framework (like pytest) -- I wanted you all to be able to run this without needing additional dependencies so I kept it simple


## How to run tests
- Make sure your Python version is 3.9 or higher
- From the command line, directly run the test file `python3 tests.py`
# remitly
Method reads JSON file. Then checks if input file has field *Resource* with value "*" in AWS::IAM::Role Policy standard.
## Installation
First clone the project repository:
```
git clone https://github.com/mpodmokly/remitly.git
```
Go to main directory:
```
cd remitly
```
Run the method with example file:
```
python main.py
```
## Running with custom file
Import function in your file:
```
from find_asterisk import find_asterisk
```
Function `find_asterisk` takes only one argument which is input file name. You can run it as follows:
```
find_asterisk("filename.json")
```
## Tests
For testing run the following command in main directory:
```
python -m unittest tests/test.py
```

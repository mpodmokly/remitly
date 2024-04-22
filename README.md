# remitly
Method reads JSON file. Then checks if input file is compatible with AWS::IAM::Role Policy standard and field *Resource* has value "*".
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
## Tests
For testing run the following command in main directory:
```
python -m unittest tests/test.py
```

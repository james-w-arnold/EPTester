## Endpoint Tester (eptester)
A very simple performance testing script used to evalute the average response speed  of an endpoint for a given number of runs.

### Requirements:
- Python 3
- pipenv (https://docs.pipenv.org/)

### Installation
- Clone the repository
- Install the requirements using pipenv: pipenv install
- Use the pipenv shell that is created: pipenv shell
- Run the eptester.py file: python eptester.py [url] [-r]

### Usage
url - The url you want to test
-r - The number of times you want to call the endpoint (default 100)

Example:
python eptester.py https://www.github.com -r 10


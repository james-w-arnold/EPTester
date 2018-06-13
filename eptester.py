import argparse
import requests
from statistics import mean

def run_request(url):
    response = requests.get(url)
    return response.elapsed.total_seconds()

def main():

    parser = argparse.ArgumentParser(description='Test and report on the speed on an endpoint')
    parser.add_argument('url', help='The target url for testing')
    parser.add_argument('-r', dest='runs', type=int, default=100, help='Change the number of requests sent (default 100)')
    args = parser.parse_args()

    average = mean([run_request(args.url) for i in range(0, args.runs)])
    print("{}ms for {} runs".format(str(average), str(args.runs)))

if __name__ == '__main__':
    main()

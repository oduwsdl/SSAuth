# -*- coding: utf-8 -*-

import sys
import requests

def check_username(username):
    return requests.get('https://projects.propublica.org/politwoops/user/' + username).status_code != 404

def main(argv):
    if(len(sys.argv) != 2):
        print("Incorrect number of arguments; please provide one username")
        sys.exit(1)
    
    if(check_username(str(sys.argv[1]))):
        print(sys.argv[1] + ' has deleted tweets archived on politwoops.')
    else:
        print(sys.argv[1] + ' does not have deleted tweets archived on politwoops.')


if __name__ == "__main__":
    main(sys.argv[1:])
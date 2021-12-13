from dotenv import dotenv_values
import argparse
import os
import requests

if os.path.isfile('.env.local'):
    config = dotenv_values('.env.local')
elif os.path.isfile('.env'):
    config = dotenv_values('.env')
else:
    print('No .env file found.')
    exit(0)

parser = argparse.ArgumentParser()
parser.add_argument('--username')
parser.add_argument('--password')
args = parser.parse_args()

if args.username == None:
    print('Missing username argument')
    exit(1)
if args.password == None:
    print('Missing password argument')
    exit(1)

API_POST_LOGIN = config['API_POST_LOGIN']
EMAIL = args.username
PASSWORD = args.password
LANGUAGE = 'FR'

def main():
    credentials = post_get_credentials()['result']
    print('JWT:', credentials['TOKEN'])
    print('SCHOOL_ID:', credentials['SCHOOL_ID'])
    print('STUDENT_ID:', credentials['ID'])


def post_get_credentials():
    res = requests.post(API_POST_LOGIN, data={
        'EMAIL': EMAIL,
        'PASSWORD': PASSWORD,
        'LANGUAGE': LANGUAGE
    })

    if res.status_code == 200:
        response = res.json()
        if response['status'] == 'success':
            return res.json()
        
    
    print(f'Error: {res.status_code=}, {res.text=}')
    exit(1)

if __name__ == '__main__':
    main()

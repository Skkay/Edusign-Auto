from dotenv import dotenv_values
import os
import requests

if os.path.isfile('.env.local'):
    config = dotenv_values('.env.local')
elif os.path.isfile('.env'):
    config = dotenv_values('.env')
else:
    print('No .env file found.')
    exit(0)

API_GET_THREE_MONTHS_COURSES = config['API_GET_THREE_MONTHS_COURSES']
API_POST_SET_STUDENT_PRESENT = config['API_POST_SET_STUDENT_PRESENT']
JWT = config['JWT']
SCHOOL_ID = config['SCHOOL_ID']
STUDENT_ID = config['STUDENT_ID']
BASE64_SIGNATURE = config['BASE64_SIGNATURE']

def main():
    last_courses = get_last_three_months_courses()
    for course in last_courses['result']:
        if course['STUDENT_PRESENCE'] == False:
            success = post_set_student_present(course['ID'])

            if success:
                print('Successfully signed for course {course_name} ({course_id})'.format(course_name=course['NAME'], course_id=course['ID']))


def get_last_three_months_courses():
    res = requests.get(API_GET_THREE_MONTHS_COURSES, headers={'authorization': 'Bearer ' + JWT})

    if (res.status_code == 200):
        return res.json()
    
    print(f'Error: {res.status_code=}, {res.text=}')
    exit(1)

def post_set_student_present(course_id):
    res = requests.post(f'{API_POST_SET_STUDENT_PRESENT}/{course_id}', data={
        'schoolId': SCHOOL_ID,
        'studentId': STUDENT_ID,
        'base64Signature': 'data:image/png;base64,' + BASE64_SIGNATURE
    })

    if res.status_code >= 200 and res.status_code <= 299:
        return True
    
    print(f'Error: {res.status_code=}, {course_id=}, {res.text=}')
    return False


if __name__ == '__main__':
    main()
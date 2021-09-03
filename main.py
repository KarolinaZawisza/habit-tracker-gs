import requests
from user_data import UserData
import datetime as dt

NUT_APP_ID = '0f90a5c4'
NUT_APP_KEY = '45296b5de703bf034c0ba3da25a28297'
NUT_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'

SHEETY_GET = 'https://api.sheety.co/916caf070298948fcad5db9c85a2358c/myWorkouts/workouts'
SHEETY_POST = 'https://api.sheety.co/916caf070298948fcad5db9c85a2358c/myWorkouts/workouts'

header = {
    'x-app-id': NUT_APP_ID,
    'x-app-key': NUT_APP_KEY
}

def register_exercise():
    query = input('What did you do today? ')

    params = {
        'query': query,
        'gender': 'female',
        'weight_kg': 76.7,
        'height_cm': 169,
        'age': 23
    }

    response = requests.post(url=NUT_ENDPOINT, data=params, headers=header).json()['exercises'][0]

    ud = UserData(
        dt.datetime.now().strftime('%d/%m/%Y'),
        dt.datetime.now().strftime('%H:%M:%S'),
        response['user_input'],
        response['duration_min'],
        response['nf_calories']
    )

    return ud

def add_exercise():
    exercise = register_exercise()
    parameters = {
        'workout': {
            'date': exercise.date,
            'time': exercise.time,
            'exercise': exercise.exercise.title(),
            'duration': exercise.duration,
            'calories': exercise.cal
        }
    }
    requests.post(url=SHEETY_POST, json=parameters)

def delete_exercise(object_id):
    requests.delete(url=f"https://api.sheety.co/916caf070298948fcad5db9c85a2358c/myWorkouts/workouts/{object_id}")
    print(f'Deleted exercise with index {object_id}')


add_exercise()

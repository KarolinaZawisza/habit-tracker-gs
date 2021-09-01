import requests
from user_data import UserData
import datetime as dt

APP_ID = '0f90a5c4'
APP_KEY = '45296b5de703bf034c0ba3da25a28297'
endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

header = {
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY
}

# query = input('What did you do today? ')

params = {
    'query': 'running for 20 minutes',
    'gender': 'female',
    'weight_kg': 76.7,
    'height_cm': 169,
    'age': 23
}

response = requests.post(url=endpoint, data=params, headers=header).json()['exercises'][0]
ud = UserData(
    dt.datetime.now().strftime('%d/%m/%Y'),
    dt.datetime.now().strftime('%H:%M:%S'),
    response['user_input'],
    response['duration_min'],
    response['nf_calories']
)
print(ud.time)

import os
import requests
from dotenv import load_dotenv

# url = 'https://api.sheety.co/ecffe46261a242b806d42fe8e31d4976/emails/email'
load_dotenv()

response = requests.get(os.getenv('SHEETY_URL'))

if response.status_code == 200:
    information = response.json()['email']
    # Do something with the data
    emails = [info['email'] for info in information]
    print(emails)
else:
    print(f"Failed to retrieve data: {response.status_code}")


# url = 'https://api.sheety.co/ecffe46261a242b806d42fe8e31d4976/emails/email/2'
# body = {
#     "email": {
#         # Add your data here
#     }
# }
#
# response = requests.put(url, json=body)
#
# if response.status_code == 200:
#     data = response.json()
#     # Do something with the data
#     print(data['Email'])
# else:
#     print(f"Failed to update data: {response.status_code}")
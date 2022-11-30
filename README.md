# vidme
Vidme is group video calling web-app which makes the use Agora Web SDK to let the users create a room and invite their friends to it to form a video room.
, used Django as backend.

## Description
A Group video calling application using the Agora Web SDK with a Django backend.

## How to use this source code
### 1 - Clone repo
git clone https://github.com/divanov11/mychat
### 2 - Install requirements
cd mychat
pip install -r requirements.txt
### 3 - Update Agora credentals
In order to use this project you will need to replace the agora credentials in views.py and streams.js.

Create an account at agora.io and create an app. Once you create your app, you will want to copy the appid & appCertificate to update views.py and streams.js.

views.py
def getToken(request):
    appId = "YOUR APP ID"
    appCertificate = "YOUR APPS CERTIFICATE"
    ......
streams.js
....
const APP_ID = 'YOUR APP ID'
....
### 4 - Start server
python manage.py runserver
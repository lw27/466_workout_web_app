# *** PLEASE READ! IMPORTANT: in order to make it work, you need to go to 
# https://console.developers.google.com/ and create a OAuth client ID credential;
# download the .json file and renamd it as "credentials.json" then put it in the working directory.
# OR you can download the one I put on Github. ***

from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/calendar'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store, flags) \
        if flags else tools.run_flow(flow, store)
CAL = build('calendar', 'v3', http=creds.authorize(Http()))

GMT_OFF = '-07:00'
EVENT = {
    'summary': 'Reminder example: "Do Workouts!"',
    'start': {'dateTime': '2019-04-25T19:00:00%s' % GMT_OFF},
    'end':   {'dateTime': '2019-04-25T20:00:00%s' % GMT_OFF},
}

e = CAL.events().insert(calendarId='primary',
        sendNotifications=True, body=EVENT).execute()

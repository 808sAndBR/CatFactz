import requests
import json

phone = 'reciever_phone_number'

#how many seconds to wait between texts (you will error out after 3 if sleeping less than 60 seconds)
sleep_seconds = 300

#number of texts to send (you will max out at 75 total texts per day)
amount = 5

r = requests.get('http://catfacts-api.appspot.com/api/facts?number=' + str(amount))

for fact in r.json()['facts']:
    sleep(sleep_seconds)
    t = requests.post('http://textbelt.com/text',data = {'number': phone,'message': fact})


'''
Thanks to http://catfacts-api.appspot.com/ for the facts
'''
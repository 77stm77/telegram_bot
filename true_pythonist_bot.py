#!/usr/bin/python

import requests
import tk


token=tk.token

consturl='https://api.telegram.org/bot' + token + '/'

global last_update_id
last_update_id=0

def get_updates():
 url=consturl + 'getupdates'
 answ=requests.get(url)
 return answ.json()

def get_message():
 data=get_updates()
 current_update_id=data['result'][-1]['update_id']
 chat_id=data['result'][-1]['message']['chat']['id']
 text=data['result'][-1]['message']['text']
 message={'chat_id': chat_id, 'text': text, 'current_update_id': current_update_id}
 return message

def send_message(chat_id, text):
 url=consturl + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
 requests.get(url)


def main():

 while True:
  answ=get_message()
  chat_id=answ['chat_id']
  text=answ['text']
  current_update_id=answ['current_update_id']

  global last_update_id
  if last_update_id != current_update_id:
   last_update_id=current_update_id
   send_message(chat_id, text)
  else:
   continue


if __name__ == '__main__':
 main()

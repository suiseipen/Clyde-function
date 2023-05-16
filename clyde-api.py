import json
import requests
import time

def send(token,message,channel_id): 
    header = {
        "authorization" : token
    }
    payload = {
        "content": "@Clyde " + message
    }
    message = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages",headers=header,json=payload)

def get_reply(token,message,channel_id,limit = 6):
	url = f'https://discord.com/api/v9/channels/{channel_id}/messages?limit={limit}'
	headers= {
		"authorization" : token
		}
	response = requests.get(
		url=url,
		headers = headers,
		timeout=30,
		)
	for i in range(limit):
		try:
			if json.loads(response.text)[i]["referenced_message"]["content"] == "@Clyde " + message:
				return json.loads(response.text)[i]["content"]
		except:
			pass

def talk(name,token,message,channel_id,wait= 3,limit = 6):
	message = message + f"私の名前は{name}です。返信の際は{name}と呼んでください"
	send(token,message,channel_id)
	time.sleep(wait)
	return get_reply(token,message,channel_id,limit)
	

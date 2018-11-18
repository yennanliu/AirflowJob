# python 3 
import yaml
import os


try:
	with open('.creds.yml') as f:
		config = yaml.load(f)
except:
	with open('../../.creds.yml') as f:
		config = yaml.load(f)


slack_api_token = config['slack_api']['token']

def get_slack_api_secret():
	#print (' slack_api_token = ', slack_api_token)
	return slack_api_token
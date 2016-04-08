import requests

class DeBot(object):
	
	
	def __init__(self, api_key):
		self.api_key = api_key	
		self._api_endpoint = 'http://cs.unm.edu/~chavoshi/debot/api.php'

	def check_user(self, screen_name):
		r = requests.post(self._api_endpoint, data={'api_key':self.api_key, 'srv_type':'1', 'user_name':screen_name})
		return r.text
		
	def get_bots_date_range(self, from_date, to_date):
		r = requests.post(self._api_endpoint, data={'api_key':self.api_key, 'srv_type':'2', 'date_1':from_date, 'date_2':to_date})
		return r.text
		
	
			
		

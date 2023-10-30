import requests
import json

def get_fuel_data():
	host = 'https://developer.nrel.gov'
	endpoint = '/api/alt-fuel-stations/v1'

	params = {
		'api_key': '3WqvBCf2Tc6AhOTaK38fKoUNyz3POjS6R6NwHb7S',
		'format': 'json',
		'status': 'all', # or, one of E available P planned T temporarily unavailable 
		'fuel_type' : 'ELEC',
		'access': 'all', # or public or private
		'ev_network': 'all',
		'ev_charging_level': 'all',
		'ev_connector_type': 'all',
		# 'state': '', # eg, CA or NY
		# 'zip': '',
		'country': 'all', # could be US or CA
		'limit': 'all' # up to 200, or all
	}

	desired_fields = [
				'station_name',
				'open_date',
				'id',
				'date_last_confirmed',
				'expected_date',
				'status_code',
				'updated_at',
				'facility_type',
				'city',
				'street_address',
				'country',
				# 'ev_charging_level',
				# 'ev_connector_type',
				'ev_network'
	]

	response = json.loads(requests.get(f'{host}{endpoint}', params).content)
	# print(response['total_results'])
	print('~'.join([field for field in desired_fields]))
	for station in response['fuel_stations']:
		print('~'.join([str(station[field]) for field in desired_fields]))
		# for field in desired_fields:
			# print(f'\t{field}: {station[field]}')
		# print()

def get_policy_data():

	host = 'https://developer.nrel.gov'
	base_url = '/api/battery-policies'
	format = 'json'
	endpoint = base_url + f'/v1/policies.{format}'

	params = {
		'api_key': '3WqvBCf2Tc6AhOTaK38fKoUNyz3POjS6R6NwHb7S',
		'limit': 10,
		'topic': 'EVS'
	}

	desired_fields = [
		'jurisdiction_type',
		'jurisdiction',
		'state',
		'agency',
		'date_enacted'
		'record_type',
		'title',
		'status',
		'status_date',
		'description',
		'date_enacted',
		'date_amended',
		'date_expired',
		'date_archived',
		'date_repealed',
		'significant_update'
	]
	response = json.loads(requests.get(f'{host}{endpoint}', params).content)
	print(response['total_results'])
	print('~'.join([field for field in desired_fields]))
	for policy in response['policies']:
		print('~'.join([str(policy[field]) for field in desired_fields]))

if __name__ == '__main__':
	get_policy_data()

import requests
import json
import sys
import re

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
	print(response['total_results'], file=sys.stderr)
	print('\t'.join([field for field in desired_fields]))
	for station in response['fuel_stations']:
		print('\t'.join([
			re.sub(
				'\t',
				r'\\t',
				str(station[field])
			)
			for field in desired_fields])
		)

def get_battery_policy_data():

	host = 'https://developer.nrel.gov'
	base_url = '/api/battery-policies'
	format = 'json'
	endpoint = base_url + f'/v1/policies.{format}'

	params = {
		'api_key': '3WqvBCf2Tc6AhOTaK38fKoUNyz3POjS6R6NwHb7S',
		'limit': 100,
		'topic': 'EVS'
	}

	desired_fields = [
		'id',
		'jurisdiction_type',
		'record_type',
		'states',
		'agencies',
		'date_enacted',
		'record_type',
		'title',
		'status',
		'status_date',
		'date_enacted',
		'date_amended',
		'date_expired',
		'date_archived',
		'date_repealed',
		'significant_update',
		'description',
	]
	response = json.loads(requests.get(f'{host}{endpoint}', params).content)
	print(response['metadata']['resultset']['count'], file=sys.stderr)
	print('\t'.join([field for field in desired_fields]))
	for policy in response['result']:
		print('\t'.join([re.sub(r'\r\n', r'\\n', str(policy[field])) for field in desired_fields]))


def get_transportation_policy_data():

	host = 'https://developer.nrel.gov'
	base_url = '/api/transportation-incentives-laws'
	format = 'json'
	endpoint = base_url + f'/v1.{format}'

	params = {
		'api_key': '3WqvBCf2Tc6AhOTaK38fKoUNyz3POjS6R6NwHb7S',
		'limit': all,
		'technology': 'ELEC'
	}

	desired_fields = [
		'id',
		'title',
		'state',
		'agency',
		'type',
		'types',
		'categories',
		'status',
		'status_date',
		'enacted_date',
		'amended_date',
		'significant_update_date',
		'text'
	]
	response = json.loads(requests.get(f'{host}{endpoint}', params).content)
	print(response['metadata']['count'], file=sys.stderr)
	print('\t'.join([field for field in desired_fields]))
	for policy in response['result']:
		line = '\t'.join([
				re.sub(
					r'\r\n',
					r'\\n',
					str(policy[field])
				) for field in desired_fields
		])
		line = re.sub('\n', '', line)
		print(line)

if __name__ == '__main__':
	# get_fuel_data()
	get_transportation_policy_data()

from django.shortcuts import render
from django.http import HttpResponse
import json

from aero_scraper import scraper

def index(request):
	if request.method == 'GET':
		query_dict = request.GET

		in_day = query_dict.get('in_day', None)
		if in_day == None:
			in_date = None
		else:
			in_date = (in_day, query_dict['in_month'], query_dict['in_year'])

		response_dict = scraper.getBestPrices(
				query_dict['airline'],
				query_dict['from_city'],
				query_dict['to_city'],
				(query_dict['out_day'], query_dict['out_month'], query_dict['out_year']),
				query_dict['adults'],
				in_date,
				query_dict.get('children', 0),
				query_dict.get('infants', 0),
			)

		return HttpResponse(json.dumps(response_dict), content_type='application/json')

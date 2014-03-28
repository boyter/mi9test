from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from name.models import Parser

import json

@csrf_exempt
def index(request):
	json_data = None
	try:
		json_data = json.loads(request.body)
	except:
		error = {"error": 
					"Could not decode request: JSON parsing failed" }
		return HttpResponse(json.dumps(error),
                        content_type="application/json",
                        status=400)
	
	parser = Parser()
	result = parser.parse_json(json_data)
	
	return HttpResponse(json.dumps(result),
                        content_type="application/json")

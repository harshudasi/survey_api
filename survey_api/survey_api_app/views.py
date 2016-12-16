from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from pymongo import MongoClient
import json
from collections import OrderedDict

from models import UserDetails,SurveyDetails,get_mobile_brands_model,get_mobile_brands_count_model
from serializers import UserSerializer
# Create your views here.


db = MongoClient('localhost',27017)
dbconn = db.survey_api

@api_view(['GET'])
def get_mobile_brands(request,age_range,family_monthly_income):
	print "in get mobile brands %s,%s" %(age_range,family_monthly_income)
	mobile_brand_list = []
	result = get_mobile_brands_model(age_range,family_monthly_income)
	for data in result:
		mobile_brand = UserDetails(data['_id'],data['mobile_brand'])
		print mobile_brand
		mobile_brand_list.append(mobile_brand)
	print mobile_brand_list

	serialized = UserSerializer(mobile_brand_list,many=True)
	print serialized.data 
	# return HttpResponse(json.dumps({"result":result}))
	return Response(serialized.data)

@api_view(['GET'])
def get_mobile_brands_counts(request,age_range,family_monthly_income):
	print "in get mobile brands counts %s,%s" %(age_range,family_monthly_income)
	mobile_brand_list = []
	samsung_count,nokia_count,micromax_count,lava_count = get_mobile_brands_count_model(age_range,family_monthly_income)
	mobile_brand_count_dict = {'samsung':samsung_count,
								'nokia':nokia_count,
								'micromax':micromax_count,
								'lava':lava_count}

	sorted_count_list = sorted(mobile_brand_count_dict.items(),key=lambda x:x[1],reverse=True)
	mobile_brand_count_dict = OrderedDict()
	for i in sorted_count_list:
		mobile_brand_count_dict[i[0]] = i[1]
	result = get_mobile_brands_model(age_range,family_monthly_income)
	for data in result:
		mobile_brand = UserDetails(data['_id'],data['mobile_brand'])
		mobile_brand_list.append(mobile_brand)
	return Response(mobile_brand_count_dict)
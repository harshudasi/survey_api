from __future__ import unicode_literals

from django.db import models

from pymongo import MongoClient


# Create your models here.
db = MongoClient('localhost',27017)
dbconn = db.survey_api


class UserDetails(object):
	def __init__(self,id,mobile_brand,name):
		self.id = id
		self.name = name
		self.mobile_brand = mobile_brand


class SurveyDetails(object):
	def __init__(self,id,surveyor_name,interview_date):
		self.id = id
		self.surveyor_name = surveyor_name
		self.interview_date = interview_date

def get_mobile_brands_model(age_range,family_income_range):
	data = dbconn.user_data.find({"age_range":age_range,
		"family_income_range":family_income_range})
	return data


def get_mobile_brands_count_model(age_range,family_income_range):
	result = dbconn.user_data.find({"age_range":age_range,
		"family_income_range":family_income_range})
	samsung_count = 0
	nokia_count = 0
	micromax_count = 0
	lava_count = 0

	for data in result:
		if data['mobile_brand'] == 'Samsung':
			samsung_count += 1
		if data['mobile_brand'] == 'Lava':
			lava_count += 1
		if data['mobile_brand'] == 'Nokia':
			nokia_count += 1
		if data['mobile_brand'] == 'Micromax':
			micromax_count += 1

	return samsung_count,nokia_count,micromax_count,lava_count
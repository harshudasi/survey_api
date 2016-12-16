from __future__ import unicode_literals

from django.db import models

from pymongo import MongoClient


# Create your models here.
db = MongoClient('localhost',27017)
dbconn = db.survey_api

# class UserDetails(object):
# 	def __init__(self,id,state,city,geography,name,address,
# 	phone_no,family_members_count,gender,age_range,
# 	family_income_range,caste,occupation,monthly_recharge,
# 	data_usage,hospital,laptop,school,fb_account,
# 	whatsapp_account,email_id,mobile_brand,mobile_network):
# 		self.id = id
# 		self.state = state
# 		self.city = city
# 		self.geography = geography
# 		self.name = name
# 		self.address = address
# 		self.phone_no = phone_no
# 		self.family_members_count = family_members_count
# 		self.gender = gender
# 		self.age_range = age_range
# 		self.family_income_range = family_income_range
# 		self.caste = caste
# 		self.occupation = occupation
# 		self.monthly_recharge = monthly_recharge
# 		self.data_usage = data_usage
# 		self.hospital = hospital
# 		self.laptop = laptop
# 		self.school = school
# 		self.fb_account = fb_account
# 		self.whatsapp_account = whatsapp_account
# 		self.email_id = email_id
# 		self.mobile_brand = mobile_brand
# 		self.mobile_network = mobile_network


class UserDetails(object):
	def __init__(self,id,mobile_brand):
		self.id = id
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
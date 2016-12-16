from pymongo import MongoClient

dbconn = MongoClient('localhost',27017).survey_api

age_range = ['12to17','18to25','26to35','36to50','50to60','60plus']
monthly_income_range = ['BPL','5000to10000','10000to20000','20000to30000'
						,'30000plus']
mobile_brand = ['Samsung','Nokia','Lava','Micromax']
name = 0
j = 0
k = 0
l = 0
for i in range(0,600):
	name += 1
	print i
	user_data = {
		'name':str(i),
		'address':'random',
		'age_range':age_range[k],
		'family_income_range':monthly_income_range[j],
		'mobile_brand':mobile_brand[l]
	}
	print user_data
	j += 1
	k += 1
	l += 1
	print i,j,k,l
	if i % 6 == 0:
		k = 0
		print i
	if j >= 5:
		j = 0
	if l >= 4:
		l = 0
	dbconn.user_data.insert(user_data)
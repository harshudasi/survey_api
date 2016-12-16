from rest_framework import serializers
from models import UserDetails,SurveyDetails

age_range_choices = [('12-17','1'),('18-25','2'),('26-35','3'),
						('36-50','4'),('51-60','5'),('60+','6')]
family_income_range_choices = [('BPL','1'),('5000-10000','2'),
				('10000-20000','3'),('20000-30000','4'),('30000+','5')]


class UserSerializer(serializers.Serializer):
	id = serializers.CharField(required=True, max_length=50)
	state = serializers.CharField(required=False, max_length=50)
	city = serializers.CharField(required=False, max_length=50)
	geography = serializers.CharField(required=False, max_length=50)
	name = serializers.CharField(required=False, max_length=50)
	address = serializers.CharField(required=False, max_length=50)
	phone_no = serializers.IntegerField(required=False,
			 min_value=0000000000,max_value=9999999999)
	family_members_count = serializers.IntegerField(required=False,
			 min_value=None,max_value=None)
	age_range = serializers.ChoiceField(required=False, 
					choices=age_range_choices,
					allow_blank=False,allow_null=False)
	gender = serializers.CharField(required=False, max_length=50)
	family_income_range = serializers.ChoiceField(required=False, 
					choices=family_income_range_choices,
					allow_blank=False,allow_null=False)
	caste = serializers.CharField(required=False, max_length=50)
	occupation = serializers.CharField(required=False, max_length=50)
	monthly_recharge = serializers.FloatField(required=False,
					max_value=None,min_value=None)
	data_usage = serializers.CharField(required=False, max_length=50)
	hospital = serializers.CharField(required=False, max_length=50)
	laptop = serializers.CharField(required=False, max_length=50)
	school = serializers.CharField(required=False, max_length=50)
	fb_account = serializers.CharField(required=False, max_length=50)
	whatsapp_account = serializers.CharField(required=False, max_length=50)
	email_id = serializers.EmailField(required=False,
					max_length=None,min_length=None,allow_blank=True)
	mobile_brand = serializers.CharField(required=True, max_length=50)
	mobile_network = serializers.CharField(required=False, max_length=50)

	def restore_object(self, attrs, instance=None):
		if instance:
			instance.id = attrs.get('id',instance.id)
			instance.state = attrs.get('state',instance.state)
			instance.city = attrs.get('city',instance.city)
			instance.geography = attrs.get('geography',instance.geography)
			instance.name = attrs.get('name',instance.name)
			instance.address = attrs.get('address',instance.address)
			instance.phone_no = attrs.get('phone_no',instance.phone_no)
			instance.family_members_count = attrs.get('family_members_count',
											instance.family_members_count)
			instance.age_range = attrs.get('age_range',instance.age_range)
			instance.gender = attrs.get('gender',instance.gender)
			instance.family_income_range = attrs.get('family_income_range',
											instance.family_income_range)
			instance.caste = attrs.get('caste',instance,caste)
			instance.occupation = attrs.get('occupation',instance.occupation)
			instance.monthly_recharge = attrs.get('monthly_recharge',
										instance.monthly_recharge)
			instance.data_usage = attrs.get('data_usage',instance.data_usage)
			instance.hospital = attrs.get('hospital',instance.hospital)
			instance.laptop = attrs.get('laptop',instance.laptop)
			instance.school = attrs.get('school',instance.school)
			instance.fb_account = attrs.get('fb_account',instance.fb_account)
			instance.whatsapp_account = attrs.get('whatsapp_account',
										instance.whatsapp_account)
			instance.email_id = attrs.get('email_id',instance.email_id)
			instance.mobile_brand = attrs.get('mobile_brand',instance.mobile_brand)
			instance.mobile_network = attrs.get('mobile_network',instance.mobile_network)
			return instance
		return UserDetails(attrs.get('id'),attrs.get('state'),attrs.get('city'),
							attrs.get('geography'),attrs.get('name'),attrs.get('address'),
							attrs.get('phone_no'),attrs.get('family_members_count'),
							attrs.get('age_range'),attrs.get('gender'),attrs.get('caste'),
							attrs.get('family_income_range'),attrs.get('occupation'),
							attrs.get('data_usage'),attrs.get('hospital'),
							attrs.get('laptop'),attrs.get('school'),attrs.get('fb_account'),
							attrs.get('whatsapp_account'),attrs.get('email_id'),
							attrs.get('mobile_brand'),attrs.get('mobile_network'))		
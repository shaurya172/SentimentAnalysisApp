from rest_framework import serializers
from . models import sentiment

class sentimentSerializers(serializers.ModelSerializer):
	class Meta:
		model=sentiment
		fields='__all__'
		managed = True
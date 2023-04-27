from rest_framework import serializers
from .models import ProdCultivations, ProdSolutions


class ProdCultivationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdCultivations
        fields = '__all__'


class ProdSolutionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdSolutions
        fields = '__all__'

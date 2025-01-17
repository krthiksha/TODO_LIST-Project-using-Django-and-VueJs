from rest_framework import serializers  
from .models import Task , Category  ## import db -- task

# converts complex data (models) into JSON (sent over internet)

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields =  '__all__'

class TaskSerializer(serializers.ModelSerializer):
    # category FK refer to task --one to many relation
    category=CategorySerializer()
    class Meta:
        model = Task
        fields = '__all__'
        
        


        
        


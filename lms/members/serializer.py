# serializers.py
from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(StudentSerializer, self).__init__(*args, **kwargs)
        request = self.context['request']

        # If it's a login operation, exclude 'password' field
        if request.path == '/api/login/' and 'phone' in request.data and 'password' in request.data:
            self.fields.pop('password', None)

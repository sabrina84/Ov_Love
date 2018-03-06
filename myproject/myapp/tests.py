from django.test import TestCase

# Create your tests here.
from myproject.myapp.models import UserInfo

UserInfo.objects.filter(username = 'Nowrin').delete()
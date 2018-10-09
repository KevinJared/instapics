from django.test import TestCase
from .models import *
# Create your tests here.

class Profiletest(TestCase):
    numusers=10
    def setUp(self):
        self.tempprofiles = []
        for i in range(self.numusers):
            tmp=Profile()
            tmp.save()
            self.tempprofiles.append(tmp)

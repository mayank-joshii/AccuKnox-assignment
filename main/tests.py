from django.test import TestCase
import threading
from django.test import TestCase
from main.models import TestingModel

class SignalTestCase(TestCase):

    def test_signal_behavior(self):
        print("Caller Thread ID:", threading.get_ident())

        try:
            TestingModel.objects.create(name="accuknox")
        except Exception as e:
            print("Exception caught:", e)

        print("Object count:", TestingModel.objects.count())



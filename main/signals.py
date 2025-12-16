import time 
import threading
from django.db.models.signals import post_save
from django.db import transaction
from django.dispatch import receiver
from .models import TestingModel

@receiver(post_save, sender=TestingModel)
def test_signal(sender, instance, **kwargs):
    print("Signal START")
    
    #Q1 code--> synchronous execution
    time.sleep(3)
    print("Signal END after 3 seconds")

    #  Q2 code --> same thread
    print("Signal Thread ID:", threading.get_ident())

    # Q3 code --> same DB transaction
    print("Inside signal, raising exception to rollback")
    raise Exception("Rollback triggered from signal")
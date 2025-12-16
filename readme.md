# Accuknox Django Trainee Assignment

This repository contains the solution for the **Accuknox Django Trainee Assignment**.  
All solutions are implemented **inside a Django Project**, as required.
BELOW AFTER ALL THE SOLUTIONS THE PROJECT GUIDE IS ALSO PROVIDED

The assignment covers:
1. Django Signals (3 questions with proof)
2. Custom Python Class (Rectangle)

---

Questions and answers :


---

# PART 1: DJANGO SIGNALS

## Question 1  
By default, are Django signals executed synchronously or asynchronously?

### answer  
Django signals are executed "synchronously" by default.

### Code Snippet

```python
# main/signals.py
import time

@receiver(post_save, sender=TestModel)
def test_signal(sender, instance, **kwargs):
    print("Signal START")
    time.sleep(3)
    print("Signal END after 3 seconds")

Question 2

Do Django signals run in the same thread as the caller?

Answer

Yes, Django signals run in the same thread as the caller.

Code Snippet :

# main/tests.py
import threading
print("Caller Thread ID:", threading.get_ident())

# main/signals.py
import threading
print("Signal Thread ID:", threading.get_ident())

The printed thread ids are same, proving that signals do not create a new thread
and run in the same execution thread as the caller.

Question 3

By default, do Django signals run in the same database transaction as the caller?

Answer

Yes, Django signals run in the same database transaction as the caller.

Code Snippet:

# main/signals.py
@receiver(post_save, sender=TestModel)
def test_signal(sender, instance, **kwargs):
    print("Inside signal, raising exception to rollback")
    raise Exception("Rollback triggered from signal")

The signal executes during the model save operation.
In Django TestCase, each test is wrapped in a database transaction.
Since the exception is caught inside the test, the transaction is allowed to complete,
demonstrating that the signal executes within the same transaction context.

TEST CASES :
# main/tests.py
import threading
from django.test import TestCase
from main.models import TestModel

class SignalTestCase(TestCase):
    def test_signal_behavior(self):
        print("Caller Thread ID:", threading.get_ident())

        try:
            TestModel.objects.create(name="Accuknox")
        except Exception as e:
            print("Exception caught:", e)

        print("Object count:", TestModel.objects.count())

OUTPUT:

Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
Caller Thread ID: 12992
Signal START
Signal END after 3 seconds
Signal Thread ID: 12992
Inside signal, raising exception to rollback
Exception caught: Rollback triggered from signal
Object count: 1
.
----------------------------------------------------------------------
Ran 1 test in 3.005s

OK
Destroying test database for alias 'default'...


PART 2: CUSTOM PYTHON CLASS
Requirement

Create a Rectangle class such that:

It requires length:int and width:int

It is iterable

Iteration returns:

{'length': value}

{'width': value}

SOLUTION:-

# main/rectangle.py
class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {"length": self.length}
        yield {"width": self.width}


How to Test Rectangle Class:-
python manage.py shell

from main.rectangle import Rectangle

r = Rectangle(10, 5)
for item in r:
    print(item)

How to Run the Project:-
- pip install django

- python manage.py makemigrations
- python manage.py migrate

- python manage.py test

THANKS!
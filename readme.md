# Accuknox Django Trainee Assignment

This repository contains the solution for the **Accuknox Django Trainee Assignment**.  
All solutions are implemented **inside a Django Project**, as required.

## Assignment Overview

The assignment covers:
1. Django Signals (3 questions with proof)
2. Custom Python Class (Rectangle)

---

# PART 1: DJANGO SIGNALS

## Question 1: Synchronous vs Asynchronous Execution

**By default, are Django signals executed synchronously or asynchronously?**

### Answer

Django signals are executed **synchronously** by default.

### Code Snippet

```python
# main/signals.py
import time

@receiver(post_save, sender=TestModel)
def test_signal(sender, instance, **kwargs):
    print("Signal START")
    time.sleep(3)
    print("Signal END after 3 seconds")
```

---

## Question 2: Same Thread Execution

**Do Django signals run in the same thread as the caller?**

### Answer

Yes, Django signals run in the same thread as the caller.

### Code Snippet

```python
# main/tests.py
import threading
print("Caller Thread ID:", threading.get_ident())

# main/signals.py
import threading
print("Signal Thread ID:", threading.get_ident())
```

The printed thread IDs are the same, proving that signals do not create a new thread and run in the same execution thread as the caller.

---

## Question 3: Database Transaction Context

**By default, do Django signals run in the same database transaction as the caller?**

### Answer

Yes, Django signals run in the same database transaction as the caller.

### Code Snippet

```python
# main/signals.py
@receiver(post_save, sender=TestModel)
def test_signal(sender, instance, **kwargs):
    print("Inside signal, raising exception to rollback")
    raise Exception("Rollback triggered from signal")
```

The signal executes during the model save operation. In Django TestCase, each test is wrapped in a database transaction. Since the exception is caught inside the test, the transaction is allowed to complete, demonstrating that the signal executes within the same transaction context.

### Test Cases

```python
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
```

### Output

```
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
```

---

# PART 2: CUSTOM PYTHON CLASS

## Requirement

Create a Rectangle class such that:
- It requires `length: int` and `width: int`
- It is iterable
- Iteration returns:
  - `{'length': value}`
  - `{'width': value}`

## Solution

```python
# main/rectangle.py
class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {"length": self.length}
        yield {"width": self.width}
```

---

## How to Test Rectangle Class

```bash
python manage.py shell
```

```python
from main.rectangle import Rectangle

r = Rectangle(10, 5)
for item in r:
    print(item)
```

---

## How to Run the Project

1. Install dependencies:
   ```bash
   pip install django
   ```

2. Set up the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. Run tests:
   ```bash
   python manage.py test
   ```

---

Thank you!
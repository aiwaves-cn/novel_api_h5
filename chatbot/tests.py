import time

from django.test import TestCase

# Create your tests here.
# import datetime
# scheduler.add_job(job, 'date', run_date='2020-10-20 17:50:01', args=['1'])

import time

# print(time.strftime())


now = time.localtime()
later = time.localtime(time.mktime(now) + 60)
format = "%Y-%m-%d %H:%M:%S"
print(time.strftime(format, later))
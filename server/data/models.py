from django.db import models
from datetime import datetime, timedelta
import pytz
import random

from django.db.models.base import Model

# Create your models here.
class Model1(models.Model):
    time = models.DateTimeField()
    user_id = models.IntegerField()
    steps = models.IntegerField()
    
    def __str__(self):
        return "{} | {} | {} | {}".format(self.id, self.user_id, self.steps, self.time)
    
    def create(count=1):
        obj_list = []
        userid = random.randint(0, 100)
        
        for i in range(count):
            obj = Model1()
            obj.time = (datetime.now() + timedelta(minutes=1) * i).astimezone(pytz.utc)
            obj.user_id = userid
            obj.steps = random.randint(0, 100)
            obj_list.append(obj)
        
        Model1.objects.bulk_create(obj_list)
        
        return obj_list
    
    def jump(count=1):
        obj_list = Model1.create(count)
        
        id_list = [x.id for x in obj_list]
        
        Model1.objects.filter(id__in=id_list).delete()
    
    def info():
        last_id = Model1.objects.order_by('-id').first().id
        count = Model1.objects.all().count()
        
        return (last_id, count)
    
    def sim(count=1, ratio=22, silent=False):
        start_time = datetime.now()
        Model1.jump(count*ratio)
        Model1.create(count)
        end_time = datetime.now()
        time_gap = end_time - start_time
        msg = "elapsed: {}ms".format(time_gap.microseconds)
        if not silent:
            print(msg)
        return msg
        
        
    def go(limit=2100000000):
        
        while True:
            count = random.randint(0, 200000)
            msg = Model1.sim(count, True)
            (l, c) = Model1.info()
            print("step: {}, last_id: {}, count: {}, {}".format(count, l, c, msg))
            if l > limit:
                break
            
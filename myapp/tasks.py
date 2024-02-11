from celery import shared_task
from time import sleep

@shared_task    ##(name="addtion_task")here you can also give this 
def sub(x,y):
    sleep(10)
    return x-y
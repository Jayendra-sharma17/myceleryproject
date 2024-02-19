from django.shortcuts import render
from myceleryproject.celery import add
from myapp.tasks import sub

from celery.result import AsyncResult
# Create your views here.
# enqueue task using delay
def index(request):
    print("results")
    result1=add.delay(10,20) 
    print("result1",result1)
    result2=sub.delay(80,20) 
    print("result2",result2)
    
    return render(request,"myapp/home.html")

# enqueue task using apply_async()
# def index(request):
#     print("results")
#     result1=add.apply_async(args=[10,20]) 
#     print("result1",result1)
#     result2=sub.apply_async(args=[40,10]) 
#     print("result2",result2)
#     return render(request,"myapp/home.html")

#display the addtion value after the task execution

def index(request):
    result=add.delay(10,30)
    
    return render(request,"myapp/home.html",{'result':result})

def check_result(request,task_id):
    #retrieve the task result using the task_id

    result=AsyncResult(task_id)
    # print("ready",result.ready())
    # print("successfull",result.successful())
    # print("failed",result.failed())
    # print("get",result.get()) isko add nhi krna h kyuki fir yee result ko block kr deta h or fir yee asysnchronous execution kehlaega
    return render(request,'myapp/result.html',{'result':result})
def about(request):
    return render(request,'myapp/about.html')

def contact(request):
    return render(request,'myapp/contact.html')
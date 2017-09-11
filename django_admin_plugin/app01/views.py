from django.shortcuts import render,redirect,HttpResponse,reverse
# Create your views here.
from app01 import models
def test(request):
    
    return render(request,'test.html')

def test1(request):
    url=reverse('custom:app01_app02userinfo_changelist')
    print(url)
    print('.m')
    # return render(request,'test.html')

def popup(request):
    user_info_list=models.App02Userinfo.objects.all()
    return render(request,'popup.html',{'user_info':user_info_list})

def popup_open(request):
    if request.method=='GET':
        return render(request, 'popup_open.html')
    else:
        popid=request.GET.get('popup')
        if popid:
            name=request.POST.get('name')
            obj=models.App02Userinfo.objects.create(name=name)
            return render(request,'popup_result.html',{'id':obj.pk,'name':name,'popid':popid})

        else:
            name=request.POST.get('name')
            models.App02Userinfo.objects.create(name=name)
            return HttpResponse('所有用户列表')




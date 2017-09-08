from django.shortcuts import render,redirect,HttpResponse,reverse
# Create your views here.
def test(request):
    
    return render(request,'test.html')

def test1(request):
    url=reverse('custom:app01_app02userinfo_changelist')
    print(url)
    print('.m')
    # return render(request,'test.html')









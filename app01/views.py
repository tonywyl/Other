from django.shortcuts import render,redirect,HttpResponse


from django.forms import ModelForm
from django.forms import Form,widgets
from django.forms import Form
from django.forms import fields as fi


from app01 import models

# Create your views here.
##ModelForm 的使用
class lookForm(ModelForm):
    user=fi.CharField(label='用户名')
    email=fi.EmailField()

    class Meta:
        model=models.UserInfo
        fields="__all__"
        error_messages={
            'user':{'required':'用户名不能为空'},
            'email':{'required':'邮箱不能为空','invalid':'邮箱格式错误'}

        }
        labels={
            'user':'用户名',
            'email':"邮箱",
        }


def look1(request):
    """
    查看用户与组信息
    :param request: 
    :return: 
    """

    if request.method=="GET":
        form=lookForm()
        context={
            'form':form,
        }
        return render(request,'look.html',context)
    else:
        form=lookForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponse('......')

#Form  的使用
class TestForm(Form):
    user=fi.CharField(label='用户名')
    email=fi.EmailField(label='邮箱')
    ug=fi.ChoiceField(
        widget=widgets.Select,
        choices=[]
    )
    def __init__(self,*args,**kwargs):
        super(TestForm,self).__init__(*args,**kwargs)
        self.fields['ug'].choices=models.UserGroup.objects.values_list('id','title')
def test(request):
    if request.method=='GET':
        form=TestForm()

        context={
            'form':form,
        }
        return render(request,'test.html',context)
    else:
        form=TestForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            ug=form.cleaned_data.pop('ug')
            print(ug)
            models.UserInfo.objects.create(**form.cleaned_data) #Form 在保存数据时需要将字段都一一对应才能写入数据库
            ug_obj=models.UserGroup.objects.filter(id=ug).first()

            return HttpResponse('....')


def edit(request,nid):
    obj=models.UserInfo.objects.filter(id=nid).first()
    if request.method=='GET':
        form=lookForm(instance=obj)
        context={
            'form':form,
        }

        return render(request,'edit.html',context)

    else:
        form=lookForm(instance=obj,data=request.POST,files=request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponse('.........')
























from django.shortcuts import HttpResponse,render,redirect
from django.urls import reverse
"""
1、数据列表页面，定制显示列
    示例一：
    v1.site.register(Model,)  ，默认只显示对象列表
    
    示例二：
    class SubClass(BaseCustom):
        list_display=[]
    v1.site.register(Model,SubClass) 按照list_display 中指定的字段显示
    而这个字段可以 是字符串，也可以是函数，
        如果是字符串需要是数据库的列名，
        如果是函数，需要遵循规则
            def comb(self,obj=None,is_header=False):
                if is_header:
                    return '某列'
                else:
                    return '%s-%s'(obj.username,obj.email)
                    
"""


class BaseCustom(object):
    # list_display = ['id','name']
    list_display = "__all__"

    add_or_edit_model_form=None
    def __init__(self,model_class,site):

        self.model_class=model_class
        self.site=site
        self.request=None

        self.app_label=model_class._meta.app_label
        self.model_name=model_class._meta.model_name

        self.list_url=None
    def get_add_or_edit_model_form(self):
        if self.add_or_edit_model_form:
            return self.add_or_edit_model_form
        else:
            from django.forms import ModelForm,widgets,fields

            custome=fields.CharField(widget=widgets.Input())
            _m=type('Meta',(object,),{'model':self.model_class,'fields':"__all__",
                                      'labels':{'username':'用户名','email':'邮箱','ug':'用户组','ur':'角色','name':'用户名'},
                                      'widgets':{'username':widgets.Input(attrs={'class':'form-control'}),
                                                 'email':widgets.Input(attrs={'class':'form-control'}),
                                                 'name':widgets.Input(attrs={'class':'form-control'}),
                                                 'ug':widgets.Select(attrs={'class':'form-control'}),
                                                 'ur':widgets.Select(attrs={'class':'form-control'}),
                                                 },
                                      'error_messages':{'__all__':'不对',
                                                        'username':{'required':'不能为空'},'email':{'required':'输入邮箱'}}
                                      })

            MyModelForm=type('MyModelForm',(ModelForm,),{'Meta':_m})
        # class MyModelForm(ModelForm):
        #     class Meta:
        #         modul=self.model_class
        #         fields="__all__"
        return MyModelForm
    @property
    def urls(self):
        from django.conf.urls import url,include
        info=self.model_class._meta.app_label,self.model_class._meta.model_name
        urlpatterns=[
            url(r'^$',self.changelist_view,name='%s_%s_changelist'%info),
            url(r'^add/$',self.add_view,name='%s_%s_add'%info),
            url(r'^(.+)/delete/$',self.delete_view,name='%s_%s_delete'%info),
            url(r'^(.+)/change/$',self.change_view,name='%s_%s_change'%info),

        ]
        return urlpatterns

    def changelist_view(self,request):
        """
        查看列表
        :param request:
        :return:
        """
        #生成页面上的添加按钮：
        #需要的元素: namespace:app_label ,model_name  reverse
        #self.site.namespace
        #self.model_class._meta.app_label



        from django.http.request import QueryDict
        # print(request.GET.urlencode())

        param_dict=QueryDict(mutable=True)

        if request.GET:
            param_dict['_changelistfilter']=request.GET.urlencode()

        # print(param_dict.urlencode())

        base_add_url=reverse("{2}:{0}_{1}_add".format(self.app_label,self.model_name,self.site.namespace))

        add_url="{0}?{1}".format(base_add_url,param_dict.urlencode())

        self.request=request

        result_list=self.model_class.objects.all()

        context={
            'result_list':result_list,
            'list_display':self.list_display,
            'display_change':self,
            'add_url':add_url
        }

        return render(request,'custum/change_list.html',context)

    def add_view(self,request):
        """
        添加数据
        :param request:
        :return:
        """

        # print(request.GET('_changelistfilter'))
        if request.method=='GET':

            model_form_obj=self.get_add_or_edit_model_form()()
        else:
            model_form_obj=self.get_add_or_edit_model_form()(data=request.POST,files=request.FILES)
            if model_form_obj.is_valid():
                model_form_obj.save()
                #添加成功，跳转页面
                #/custom/app01/userinfo/+request.GET.get('_changelistfileter')
                base_list_url = reverse("{2}:{0}_{1}_changelist".format(self.app_label, self.model_name, self.site.namespace))
                # print(request.GET.get('_changelistfilter'),'0000')
                self.list_url = "{0}?{1}".format(base_list_url, request.GET.get('_changelistfilter'))
                return redirect(self.list_url)


        context={
            'form':model_form_obj,
        }
        from django.forms.boundfield import BoundField
        from django.forms.models import ModelFormMetaclass
        from django.forms.models import ModelMultipleChoiceField
        from django.db.models.query import QuerySet

        for item in model_form_obj: #提示显示中文
            # print(item.label) #这样也可以拿到每个INPUT框的中文
            #为多选和下拉框 加一个popup

            print(item.field)



        return render(request,'custum/add.html',context)
    def delete_view(self,request,pk):
        """
        :param reqeust:
        :return:
        """
        print(request.GET.get('_changelist'),'------')
        info=self.model_class._meta.app_label,self.model_class._meta.model_name
        data="%s_%s_del"%info
        self.model_class.objects.filter(id=pk).delete()
        base_list_url = reverse("{2}:{0}_{1}_changelist".format(self.app_label, self.model_name, self.site.namespace))
        self.list_url = "{0}?{1}".format(base_list_url, request.GET.get('_changelistfilter'))
        return redirect(self.list_url)

    def change_view(self,request,pk):

        obj=self.model_class.objects.filter(pk=pk).first()
        if not obj:
            return HttpResponse('id不存在 ')

        if request.method=='GET':
            model_form_obj = self.get_add_or_edit_model_form()(instance=obj)
        else:
            model_form_obj=self.get_add_or_edit_model_form()(data=request.POST,instance=obj) #没有instance 则表示增加，有表示修改

            if model_form_obj.is_valid:
                model_form_obj.save()
            base_list_url = reverse(
                "{2}:{0}_{1}_changelist".format(self.app_label, self.model_name, self.site.namespace))
            self.list_url = "{0}?{1}".format(base_list_url, request.GET.get('_changelistfilter'))
            return redirect(self.list_url)
            
        context={
            'form':model_form_obj
        }
        return render(request,'custum/edit.html',context)
    
class Custom(object):
    
    def __init__(self):
        
        self._registry={}
        
        self.namespace='custom'
        
        self.app_name='custom'

    def register(self,model_class,BaseClass=BaseCustom): #注册方法如admin.site.register(models.Role) model_clss类也就是表的名称，
        """_registry
        {
          _registry[model.Role]:obj
        }
        """

        self._registry[model_class]=BaseClass(model_class,self)
        print(self._registry,self,'----')
        """
        app名称models类名：BaseCustom 类封装了 app名称models类名,Custum对象
        {<class 'app02.models.Role'>: <app03.service.v1.BaseCustom object at 0x106149c18>, 
        <class 'app01.models.App02Userinfo'>: <app03.service.v1.BaseCustom object at 0x1061499b0>}
        {<class 'app02.models.Role'>: <app03.service.v1.BaseCustom object at 0x106149c18>, 
        <class 'app01.models.App02Userinfo'>: <app03.service.v1.BaseCustom object at 0x1061499b0>,
         <class 'app02.models.test1'>: <app03.service.v1.BaseCustom object at 0x106149940>}
         
        """


    def get_urls(self):
        from django.conf.urls import url,include
        ret=[
            # url(r'login/',self.login,name='login'),
            # url(r'logout/',self.logout,name='logout'),

        ]

        for model_cls,admin_obj in self._registry.items():
            print(model_cls,model_cls._meta.app_label,'---',model_cls._meta.model_name)
                            #app名字                          #模块名字
            app_labe=model_cls._meta.app_label
            model_name=model_cls._meta.model_name
            ret.append(url(r'%s/%s/'%(app_labe,model_name), include(admin_obj.urls))) #反生成,当每个APP的URL进来时，每个APP都 有
            #自己的增删改查。

        return ret

    def login(self,request):
        return HttpResponse('login')
    def logout(self,request):
        return HttpResponse('logout')

    @property
    def urls(self):
        return self.get_urls(),self.app_name,self.namespace


site=Custom()
print('cusmtom app02')


from app03.service import v1
from app02 import models
from django.utils.safestring import mark_safe
class display_oprate(v1.BaseCustom):
    def func(self, obj=None,is_header=False):
        if is_header:
            return '操作'
        else:
            """
            显示操作字段
            """
            from django.urls import reverse
            name = "{namespace}:{appname}_{modelname}_change".format(namespace=self.site.namespace,
                                                                     appname=self.model_class._meta.app_label,
                                                                     modelname=self.model_class._meta.model_name)
            url = reverse(name, args=(obj.pk,))  # reverse{namespace:}
            return mark_safe("<a href='{0}'>编辑</a>".format(url))

    def checkbox(self, obj=None,is_header=False):
        if is_header:
            return mark_safe("<input type='checkbox'/>")
        else:
            tag = '<input type="checkbox" value="{0}" />'.format(obj.pk)
            return mark_safe(tag)

    list_display = [checkbox, 'id', 'username','email', func]

class Display_userinfo(v1.BaseCustom):
    list_display=['id','username','email']

class Display_Role(v1.BaseCustom):
    def func(self, obj=None,is_header=False):
        """
        显示操作字段
        """
        if is_header:
            return '操作'
        else:
            """
            显示操作字段
            """
            from django.urls import reverse
            name = "{namespace}:{appname}_{modelname}_change".format(namespace=self.site.namespace,
                                                                     appname=self.model_class._meta.app_label,
                                                                     modelname=self.model_class._meta.model_name)
            url = reverse(name, args=(obj.pk,))  # reverse{namespace:}
            return mark_safe("<a href='{0}'>编辑</a>".format(url))

    def checkbox(self, obj=None,is_header=False):
        if is_header:
            return mark_safe("<input type='checkbox'/>")
        else:
            tag = '<input type="checkbox" value="{0}" />'.format(obj.pk)
            return mark_safe(tag)

    list_display = [checkbox, 'id', 'name', func]

class Display_test1(v1.BaseCustom):
    def func(self,obj=None,is_header=False):
        """
        显示操作字段
        """
        if is_header:
            return '操作'
        else:
            """
            显示操作字段
            """
            from django.urls import reverse
            name = "{namespace}:{appname}_{modelname}_change".format(namespace=self.site.namespace,
                                                                     appname=self.model_class._meta.app_label,
                                                                     modelname=self.model_class._meta.model_name)
            url = reverse(name, args=(obj.pk,))  # reverse{namespace:}
            from django.http.request import QueryDict
            param_dict = QueryDict(mutable=True)
            if self.request.GET:
                param_dict['_changelistfilter'] = self.request.GET.urlencode()

            return mark_safe("<a href='{0}'>编辑</a>".format(url))

    def checkbox(self,obj=None,is_header=False):
        if is_header:
            return mark_safe("<input type='checkbox'/>")
        else:
            tag = '<input type="checkbox" value="{0}" />'.format(obj.pk)
            return mark_safe(tag)
    list_display = [checkbox,'id','title',func]

v1.site.register(models.UserInfo,display_oprate)
v1.site.register(models.Role,Display_Role)
v1.site.register(models.test1,Display_test1)

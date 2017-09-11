print('cusmtom app02')


from app03.service import v1
from app02 import models
from django.utils.safestring import mark_safe
from django.urls import reverse


class display_oprate(v1.BaseCustom):

    def func(self, obj=None,is_header=False):
        if is_header:
            return mark_safe('<th>操作</th>')
        else:
            """
            显示操作字段
            """
            from django.http.request import QueryDict
            param_dict = QueryDict(mutable=True)

            if self.request.GET:
                param_dict['_changelistfilter'] = self.request.GET.urlencode()
                param_dict['_delete']=self.request.GET.urlencode()

            base_edit_url = reverse("{2}:{0}_{1}_change".format(self.app_label, self.model_name, self.site.namespace),args=(obj.pk,))
            base_del_url = reverse("{2}:{0}_{1}_delete".format(self.app_label, self.model_name, self.site.namespace),args=(obj.pk,))
            # reverse{namespace:}
            edit_url="{0}?{1}".format(base_edit_url,param_dict.urlencode())
            del_url="{0}?{1}".format(base_del_url,param_dict.urlencode())
            return mark_safe("<td><a href='{0}' class='btn btn-default'>编辑</a>&nbsp;&nbsp;<a href='{1}' class='btn btn-default'>删除</a></td>".format(edit_url,del_url))

    def checkbox(self, obj=None,is_header=False):
        if is_header:
            return mark_safe('选项')
            # return mark_safe("<input type='checkbox'/>")
        else:
            tag = '<input type="checkbox" value="{0}" />'.format(obj.pk)
            return mark_safe(tag)

    def comb(self,obj=None,is_header=False):
        if is_header:
            return mark_safe('地域')
        else:
            return "%s-%s"%(obj.username,obj.email)

    list_display = [checkbox, 'id', 'username','email',comb,func]

class Display_userinfo(v1.BaseCustom):
    list_display=['id','username','email']

class Display_Role(v1.BaseCustom):
    def func(self, obj=None,is_header=False):
        """
        显示操作字段
        """
        if is_header:
            return mark_safe('<th>操作</th>')
        else:
            """
            显示操作字段
            """
            from django.http.request import QueryDict
            param_dict = QueryDict(mutable=True)

            if self.request.GET:
                param_dict['_changelistfilter'] = self.request.GET.urlencode()
                param_dict['_delete']=self.request.GET.urlencode()

            base_edit_url = reverse("{2}:{0}_{1}_change".format(self.app_label, self.model_name, self.site.namespace),args=(obj.pk,))
            base_del_url = reverse("{2}:{0}_{1}_delete".format(self.app_label, self.model_name, self.site.namespace),args=(obj.pk,))
            # reverse{namespace:}
            edit_url="{0}?{1}".format(base_edit_url,param_dict.urlencode())
            del_url="{0}?{1}".format(base_del_url,param_dict.urlencode())
            return mark_safe("<td><a href='{0}' class='btn btn-default'>编辑</a>&nbsp;&nbsp;<a href='{1}' class='btn btn-default'>删除</a></td>".format(edit_url,del_url))

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
            return mark_safe('<th>操作</th>')
        else:
            """
            显示操作字段
            """
            from django.http.request import QueryDict
            param_dict = QueryDict(mutable=True)

            if self.request.GET:
                param_dict['_changelistfilter'] = self.request.GET.urlencode()
                param_dict['_delete']=self.request.GET.urlencode()

            base_edit_url = reverse("{2}:{0}_{1}_change".format(self.app_label, self.model_name, self.site.namespace),args=(obj.pk,))
            base_del_url = reverse("{2}:{0}_{1}_delete".format(self.app_label, self.model_name, self.site.namespace),args=(obj.pk,))
            # reverse{namespace:}
            edit_url="{0}?{1}".format(base_edit_url,param_dict.urlencode())
            del_url="{0}?{1}".format(base_del_url,param_dict.urlencode())
            return mark_safe("<td><a href='{0}' class='btn btn-default'>编辑</a>&nbsp;&nbsp;<a href='{1}' class='btn btn-default'>删除</a></td>".format(edit_url,del_url))
    def checkbox(self,obj=None,is_header=False):
        if is_header:
            return mark_safe("<input type='checkbox'/>")
        else:
            tag = '<input type="checkbox" value="{0}" />'.format(obj.pk)
            return mark_safe(tag)




    list_display = [checkbox,'id','title',func]

class Display_group(v1.BaseCustom):
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
            from django.http.request import QueryDict
            param_dict = QueryDict(mutable=True)

            if self.request.GET:
                param_dict['_changelistfilter'] = self.request.GET.urlencode()

            base_edit_url = reverse("{2}:{0}_{1}_change".format(self.app_label, self.model_name, self.site.namespace),
                                    args=(obj.pk,))
            # reverse{namespace:}
            edit_url = "{0}?{1}".format(base_edit_url, param_dict.urlencode())
            return mark_safe("<a href='{0}'>编辑</a>".format(edit_url))

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
v1.site.register(models.UserGroup,Display_group)
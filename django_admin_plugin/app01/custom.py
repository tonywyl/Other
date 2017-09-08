print('custom app01')

from app03.service import v1
from app01 import models
from django.utils.safestring import mark_safe
class display_oprate(v1.BaseCustom):
    def display_change(self,obj):
        """
        显示操作字段
        """
        from django.urls import reverse
        name="{namespace}:{appname}_{modelname}".format(namespace=self.site.namespace,appname=self.model_class._meta.app_label,modelname=self.model_class._meta.model_name)
        url=reverse(name,args=(obj.pk))# reverse{namespace:}
        return mark_safe("<a href='{id}'>编辑</a>").format(id=url)
    def checkbox(self,obj):
        tag='<input type="checkbox" value="{0}">'.format(obj.pk)
        return mark_safe(tag)
    list_display = [checkbox,'id','name',display_change]
class display(v1.BaseCustom):
    list_display=['id','name']

v1.site.register(models.App02Userinfo,display)






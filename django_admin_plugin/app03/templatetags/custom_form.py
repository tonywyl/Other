from django.forms.models import ModelChoiceField
from django.template import Library

from django.urls import reverse
from app03.service import v1
register=Library()
@register.inclusion_tag('custum/add_templatetag.html')#add_edit_form.html 取值
def show_add_edit_form(form):
    form_list=[]
    for item in form:
        row={'is_popup':False,'item':None,'popup_url':None}
        if isinstance(item.field,ModelChoiceField) and item.field.queryset.model in v1.site._registry:
            targe_app_label=item.field.queryset.model._meta.app_label

            target_model_name=item.field.queryset.model._meta.model_name

            url_name="{0}:{1}_{2}_add".format(v1.site.namespace,targe_app_label,target_model_name)
            target_url=reverse(url_name)
            row['is_popup']=True

            row['popup_url']=target_url
            row['item']=item
        else:
            row['item']=item

        form_list.append(row)
    return {'form':form_list}








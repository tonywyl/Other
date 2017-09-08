from django.template import Library
from types import FunctionType
register=Library()

def inner(result_list,list_display,display_change):
    print(result_list,'===') #<QuerySet [<UserInfo: UserInfo object>, <UserInfo: UserInfo object>]>
    for i in result_list:
        print([str(i)],'------')

    for row in result_list:
        if list_display=='__all__':
            yield [str(row),] #['UserInfo object']
        else:
        # yield [getattr(row,name) for name in list_display]
            yield [name(display_change,obj=row) if isinstance(name,FunctionType) else getattr(row,name) for name in list_display]


def table_head(list_display,display_change):

    for item in list_display:
        if isinstance(item, FunctionType):
            # head_list.append(item.__name__.title())
            yield item(display_change, is_header=True)
        else:
            yield display_change.model_class._meta.get_field(item).verbose_name
            # item 类型  "username"  "email" "id"


@register.inclusion_tag('custum/md.html')#表示要导入一个HTML模板,下面的返回值表示给这个模板使用
def func(result_list,list_display,display_change):

    v=inner(result_list,list_display,display_change)
    
    
    h=table_head(list_display,display_change)

    return {'name':v,'name2':h}





















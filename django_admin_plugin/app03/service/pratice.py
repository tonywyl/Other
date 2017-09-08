from django.forms import ModelForm


class MyModelForm(ModelForm):
    class Meta:
        modul = self.model_class
        fields = "__all__"


class_name='MYmodelform'
class_bases=(object,)
class_dict={}
exec








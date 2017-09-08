from django.apps import AppConfig


class App01Config(AppConfig):
    name = 'app01'
    def ready(self):
        """
        当程序运行时，django会找每个APP的apps.py的ready 方法
        :return:
        """
        super(App01Config,self).ready()
        from django.utils.module_loading import autodiscover_modules
        autodiscover_modules('custom')
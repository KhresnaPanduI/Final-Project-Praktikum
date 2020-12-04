from django.apps import AppConfig


class AkunConfig(AppConfig):
    name = 'akun'
    def ready(self):
    	import akun.signals
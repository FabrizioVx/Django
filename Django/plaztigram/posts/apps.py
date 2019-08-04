#DECLARA TODA LA CONFIGURACION DE NUESTRA APP EN CASO SEA REUTILEZABLE O SE PUEDE RECONFIGURAR
#POST APLICATION
from django.apps import AppConfig


class PostsConfig(AppConfig):
    name = 'posts'
    varbose_name = 'Posts'
    

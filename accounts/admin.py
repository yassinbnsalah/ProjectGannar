from django.contrib import admin

from .models import Client 
# Register your models here.
admin.site.register(Client)

from .models import Demmande 
# Register your models here.
admin.site.register(Demmande)


from .models import Request_Role 
# Register your models here.
admin.site.register(Request_Role)

from .models import Ouvrier 
# Register your models here.
admin.site.register(Ouvrier)
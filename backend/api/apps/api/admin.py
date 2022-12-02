from django.contrib import admin
from .models.silos import Silos
from .models.logs import Logs
from .models.liquids import Liquids


admin.site.register(Liquids)
admin.site.register(Logs)
admin.site.register(Silos)

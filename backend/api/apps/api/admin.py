from django.contrib import admin
from .models.silos import Silos
from .models.zones import Zones
from .models.actions import Actions
from .models.liquids import Liquids


admin.site.register(Liquids)
admin.site.register(Zones)
admin.site.register(Silos)
admin.site.register(Actions)

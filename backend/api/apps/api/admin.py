from django.contrib import admin
from .models import Silos, Logs, Liquids, SensorsInSilos, Sizes,\
    LiquidProperties, Properties, SensorsTypology, MeasureUnits, SensorsTypes


admin.site.register(Liquids)
admin.site.register(Logs)
admin.site.register(Silos)
admin.site.register(SensorsInSilos)
admin.site.register(Sizes)
admin.site.register(SensorsTypes)
admin.site.register(LiquidProperties)
admin.site.register(Properties)
admin.site.register(SensorsTypology)
admin.site.register(MeasureUnits)

from django.contrib import admin

from compeapp.models import administrator, competition, event, hackathon, scholar
admin.site.register(administrator)
admin.site.register(scholar)
admin.site.register(hackathon)
admin.site.register(competition)
admin.site.register(event)
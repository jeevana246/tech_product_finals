from django.contrib import admin

from compeapp.models import administrator, hackathon, scholar
admin.site.register(administrator)
admin.site.register(scholar)
admin.site.register(hackathon)
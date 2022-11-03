from django.contrib import admin
from EID.models import UserProfileInfo,Docstatus,adhardocument,passportdocument,dldocument,pancarddocument,voteriddocument,rationcarddocument,buspassdocument
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Docstatus)
admin.site.register(adhardocument)
admin.site.register(passportdocument)
admin.site.register(dldocument)
admin.site.register(pancarddocument)
admin.site.register(voteriddocument)
admin.site.register(rationcarddocument)
admin.site.register(buspassdocument)

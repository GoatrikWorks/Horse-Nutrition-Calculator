from django.contrib import admin
# from first_app.models import AccessRecord, Topic, Webpage
# # Register your models here.
# admin.site.register(AccessRecord)
# admin.site.register(Topic)
# admin.site.register(Webpage)
from AppTwo.models import UserProfileInfo

admin.site.register(UserProfileInfo)

from django.contrib import admin

from account.models import *

admin.site.site_header = "XX系统"

admin.site.register(User)



from django.contrib import admin
from my_website_app.models import Services, Portfolio, About, Languages


# Register your models here.

admin.site.register(Services)
admin.site.register(Portfolio)
admin.site.register(About)
admin.site.register(Languages)
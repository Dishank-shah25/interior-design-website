from django.contrib import admin
from .views import *
from  .models import *
# Register your models here.
class showtimedelivery(admin.ModelAdmin):
    list_display = ["email","message"]
admin.site.register(timedelivery,showtimedelivery)

class showcompletefeeting(admin.ModelAdmin):
    list_display = ["email","message"]
admin.site.register(complete_fitting,showcompletefeeting)

class showcontact(admin.ModelAdmin):
    list_display = ['name','email','phone','subject','message']
admin.site.register(contact_us,showcontact)

class showimages(admin.ModelAdmin):
    list_display = ['title','description','photo']
    search_fields = ['title','description']
admin.site.register(Service,showimages)

class showgimage(admin.ModelAdmin):
    list_display = ['title','gphoto']
    search_fields = ['title']
admin.site.register(gimage,showgimage)

class showblogimage(admin.ModelAdmin):
    list_display = ['bphoto','title','description']
    search_fields = ['title','description']
    list_per_page = 5
admin.site.register(blogimage,showblogimage)

@admin.register(productCategory)
class showProductCate(admin.ModelAdmin):
    list_display = ['name', 'categoryphoto']

@admin.register(product)
class showProductCate(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'description', 'materialType', 'color', 'qty', 'productphoto', 'status']

class showpcategory(admin.ModelAdmin):
    list_display = ['name','pphoto']
admin.site.register(Pcategory,showpcategory)

class showshopdetials(admin.ModelAdmin):
    list_display = ['category','name','productimage','materialType','color','price','description','qty','status']
admin.site.register(sdetials,showshopdetials)





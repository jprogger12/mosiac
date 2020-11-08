from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('category', 'about', 'get_image')
    list_filter = ('category__name', 'about')
    search_fields = ('category__name', 'about')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.img.url}" width="100" height =auto>')

    get_image.short_description = "rasm"


admin.site.register(ContactInfomation)
admin.site.register(Message)


class PersonContactInline(admin.TabularInline):
    model = TeamPersonContact
    extra = 1


@admin.register(TeamPerson)
class TeamPersonAdmin(admin.ModelAdmin):
    list_display = ('fullName', 'profession', 'about', 'get_image')
    list_filter = ('fullName', 'profession')
    search_fields = ('fullName', 'profession')
    inlines = [PersonContactInline]
    save_on_top = True

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.img.url}" width="100" height =auto>')

    get_image.short_description = "rasm"


# admin.site.register(TeamPerson)
# admin.site.register(TeamPersonContact)
admin.site.register(Category)

admin.site.register(Customer)
admin.site.register(About)


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


@admin.register(BlogLetter)
class BlogLetterAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'user', 'get_image')
    list_filter = ('title', 'slug', 'user')
    search_fields = ('fullName', 'profession')
    inlines = [CommentInline]
    save_on_top = True
    save_as = True

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.img.url}" width="100" height =auto>')

    get_image.short_description = "rasm"


# admin.site.register(BlogLetter)
admin.site.register(OurService)
admin.site.register(HomeHeader)
admin.site.register(EmailSend)

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import (
    Keyword,
    Biography,
    Sponsor,
    Publisher,
    EducationLevel,
    Language,
    LicenseType,
    genre_audio_video,

)

from django.contrib.auth.models import User
from django.utils.html import format_html

# For re-arranging user section in admin panel


class UserAdmin(admin.ModelAdmin):
    search_fields = (
        'username',
        'first_name',
        'last_name',
    )
    list_display = ['username', 'first_name','last_name','email','date_joined' ]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
    )
    list_display = ['sponsor_name_', 'edit_link', ]

    def sponsor_name_(self, obj):
        return obj.name

    def edit_link(self, obj):
        return format_html("<a href='{url}'>Edit</a>", url=obj.get_admin_url())



@admin.register(LicenseType)
class LicenseTypeAdmin(admin.ModelAdmin):
    search_fields = (
        'license',
    )

@admin.register(Keyword)
class KeyWordAdmin(ImportExportModelAdmin):
    search_fields = (
        'keyword',
    )
    pass


@admin.register(genre_audio_video)
class genre_audio_videoAdmin(admin.ModelAdmin):
    search_fields = (
        'custom_genre',
    )
    pass

@admin.register(Biography)
class BiographyAdmin(admin.ModelAdmin):
    exclude = [
        'first_name',
        'middle_name',
        'last_name',
    ]

    list_display = ['author', 'edit_link']
    search_fields = (
        'name',
    )

    def author(self,obj):
        return format_html('<a href="%s">%s</a>' % (obj.get_absolute_url(), obj.getName))

    def edit_link(self, obj):
        return format_html("<a href='{url}'>Edit</a>", url=obj.get_admin_url())


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    search_fields = (
        'publisher_name',
    )
    list_display = ['Publisher_name', 'edit_link']

    def Publisher_name(self, obj):
        return format_html('<a href="%s">%s</a>' % (obj.get_absolute_url(), obj.publisher_name))

    def edit_link(self, obj):
        return format_html("<a href='{url}'>Edit</a>", url=obj.get_admin_url())

@admin.register(EducationLevel)
class EducationLevelAdmin(admin.ModelAdmin):
    pass

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    search_fields = (
        'language',
    )

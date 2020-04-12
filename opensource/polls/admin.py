from django.contrib import admin

from .models import Question, Choice, Test

admin.site.site_header = "Admin Panel"
admin.site.site_title = "Admin Panel"
admin.site.index_title = "Welcome to the admin panel"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    
class QuestionInLine(admin.TabularInline):
    model = Question
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Total votes',{'fields': ['total_votes']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse'] })
                 ]
    inlines = [ChoiceInline]
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_filter = ['test']
    list_display = ('question_text', 'test')
    fieldsets = [(None, {'fields': ['question_text','test']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse'] }), 
                 ]
    inlines = [ChoiceInline]

class TestAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['test_text']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse'] }), 
                 ]
    inlines = [QuestionInLine]






# admin.site.register(Question)
admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
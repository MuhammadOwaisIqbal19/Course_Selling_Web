

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Purchase,VideoProgress,Quiz,Question,QuizAttempt,QuizAccess,NextVideoAccess


class PurchaseAdmin(admin.ModelAdmin):
    pass


# class LocationAdmin(admin.ModelAdmin):
#     pass


admin.site.register(Purchase,PurchaseAdmin)

class VideoProgressAdmin(admin.ModelAdmin):
    pass

admin.site.register(VideoProgress,VideoProgressAdmin)


class QuizAdmin(admin.ModelAdmin):
    pass

admin.site.register(Quiz,QuizAdmin)


class QuestionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Question,QuestionAdmin)


class QuizAttemptAdmin(admin.ModelAdmin):
    pass

admin.site.register(QuizAttempt,QuizAttemptAdmin)


class QuizAccessAdmin(admin.ModelAdmin):
    pass

admin.site.register(QuizAccess,QuizAccessAdmin)



class NextVideoAccessAdmin(admin.ModelAdmin):
    pass

admin.site.register(NextVideoAccess,NextVideoAccessAdmin)
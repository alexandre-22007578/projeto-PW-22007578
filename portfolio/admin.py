from django.contrib import admin

# Register your models here.
from .models import Post
from .models import Quizz
from .models import Projetos
from .models import Pessoas
from .models import Cadeira
from .models import Tecnologias

admin.site.register(Post)
admin.site.register(Quizz)
admin.site.register(Projetos)
admin.site.register(Pessoas)
admin.site.register(Cadeira)
admin.site.register(Tecnologias)

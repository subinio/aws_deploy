from django.contrib import admin
from .models import Cs
from .models import Fs
from .models import Os
from .models import Dong
from .models import Childuser
from .models import Parentuser


admin.site.register(Cs)
admin.site.register(Childuser)
admin.site.register(Parentuser)
admin.site.register(Fs)
admin.site.register(Os)
admin.site.register(Dong)
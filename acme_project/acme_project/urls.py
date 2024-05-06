# acme_project/urls.py
# Импортируем настройки проекта.
from django.conf import settings
# Импортируем функцию, позволяющую серверу разработки отдавать файлы.
from django.conf.urls.static import static
from django.contrib import admin

# классы для создания пользователей прямо в урлс
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import include, path, reverse_lazy

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('birthday/', include('birthday.urls')),
    # Подключаем urls.py приложения для работы с пользователями.
    path('auth/', include('django.contrib.auth.urls')),
    # сразу в path, перадаем в аргументы в метод as_view, для создания
    # пользователей без необходимости писать новый CBV в views.py
    path(
        'auth/registration/',
        CreateView.as_view(
            # указываем форму
            template_name='registration/registration_form.html',
            # встроенный класс для создания пользователей
            form_class=UserCreationForm,
            # путь для редиректа после аутентификации
            success_url=reverse_lazy('pages:homepage'),
        ),
        name='registration',
    ),
    # В конце добавляем к списку вызов функции static.
]

handler404 = 'core.views.page_not_found'

if settings.DEBUG:
    import debug_toolbar
# Добавить к списку urlpatterns список адресов из приложения debug_toolbar:
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
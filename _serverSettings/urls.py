from django.urls import path
from login import views
from vsl import views as views_vsl
from mines import views  as views_mines
from django.conf import settings
from django.conf.urls.static import static
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
from home import views as views_homepage
from double import views as views_double
from pressell import views as views_pressell
from aviatrix import views as views_aviatrix
from notfound import views as views_404


urlpatterns = [
  # URLS DEFAULT
  path('', views.user_login, name='welcome'),
  path('vsl/', views_vsl.vsl, name='vsl'),
  path('logout', LogoutView.as_view(next_page=reverse_lazy('user_login')), name='logout'),
  path('login/', views.user_login, name='user_login'),
  path('mines/', views_mines.mines, name='mines'),
  path('nostar/', views.nostar, name='nostar'),
  path('star/', views.star, name='star'),
  path('webhooks', views.webhook, name='webhook'),
  path('double/', views_double.double_view, name="double" ),
  path("pressell/", views_pressell.pressell, name="pressell"),
  path("pressell-pixel/", views_pressell.pressell_pixel, name="pressell-pixel"),
  path('homepage/', views_homepage.homepage, name='homepage'),
  path('aviatrix/', views_aviatrix.aviatrix, name='aviatrix'),
  path('<path:undefined_path>', views.notfound, name='404')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


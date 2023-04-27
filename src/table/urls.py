from django.urls import path, include
from .views import homepage, prod_spec, about, \
    prod_series_equip, graphik_all, \
    prod_series, graphik_cur, graphik_result, \
    equipment_func, current_cultivation, current_solution, \
    ProdCultivationsViewSet, ProdSolutionsViewSet, plug
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register(r'ProdCultivations', ProdCultivationsViewSet)
router.register(r'ProdSolutions', ProdSolutionsViewSet)

urlpatterns = [
    path('reg/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    # path('', plug, name='plug'),
    path("", homepage, name="homepage"),
    path("<int:pk>/", prod_spec, name="prod_spec"),
    path("about/", about, name="about"),
    path("<name_spec>/",
         prod_series_equip, name="prod_series_equip"),
    path("name_spec1/<name_seria>/",
         graphik_all, name="graphik_all"),
    path("name_spec/<name_seria>/",
         prod_series, name="prod_series"),
    path("name_spec/name_seria/<name_seria>/",
         graphik_cur, name="graphik_cur"),
    path("name_spec3/name_seria3/<name_spec>/",
         graphik_result, name="graphik_result"),
    path("spec/<name_current_equipment>/",
         equipment_func, name="equipment_func"),
    path("spec1/name_seria1/<name_of_cultivation>/",
         current_cultivation, name="current_cultivation"),
    path("spec2/name_seria2/<name_of_solution>/",
         current_solution, name="current_solution"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

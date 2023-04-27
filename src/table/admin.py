from django.contrib import admin


from table.models import Product, ProdSeria, \
    Equipment, ProdEquipment, Solution, ProdSolutions, Cultivation, \
    ProdCultivations, ProdSpec

admin.site.register(Product)


@admin.register(ProdSpec)
class ProdSpecAdmin(admin.ModelAdmin):
    list_display = ('name_spec', 'product')
    list_display_links = ('name_spec',)
    list_filter = ('product',)


@admin.register(ProdSeria)
class ProdSeriaAdmin(admin.ModelAdmin):
    list_display = ('name_seria', 'total_result', 'prod_spec')
    list_display_links = ('name_seria',)
    search_fields = ('name_seria',)
    list_filter = ('name_seria',)


admin.site.register(Equipment)


@admin.register(ProdEquipment)
class ProdEquipmentAdmin(admin.ModelAdmin):
    list_display = ('name_equip', 'firm')
    list_display_links = ('name_equip',)
    list_filter = ('firm',)


@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    list_display = ('name_of_solution', 'prod_ser_sol')
    list_display_links = ('name_of_solution', 'prod_ser_sol')
    list_filter = ('prod_ser_sol',)


@admin.register(ProdSolutions)
class ProdSolutionsAdmin(admin.ModelAdmin):
    list_display = ('solution', 'target', 'solution_seria', 'quantity')
    list_display_links = ('solution',)
    list_filter = ('solution__prod_ser_sol__name_seria',)


# class ProdCultivationInline(admin.TabularInline):
#     model = ProdCultivations
@admin.register(Cultivation)
class CultivationAdmin(admin.ModelAdmin):

    list_display_links = ('name_of_cultivation',)
    # inlines = [ProdCultivationInline]
    list_display = ('name_of_cultivation', 'prod_ser_cult')
    list_filter = ('prod_ser_cult',)


@admin.register(ProdCultivations)
class ProdCultivationsAdmin(admin.ModelAdmin):
    list_display = ('cultivation', 'seria_filter', 'date')
    list_filter = ('cultivation__prod_ser_cult__name_seria',)
    fieldsets = (
        ('Info', {'fields': ('date', 'cultivation')}),
        ('Values', {
            'fields': (
              ('concentration_up_to', 'concentration_after'),
              ('viability_up_to', 'viability_after'), 'ph',
              ('glucose', 'lactose')
                 )}),
    )

    def seria_filter(self, obj):
        return ProdSeria.objects.get(
            cultivation__name_of_cultivation__contains=obj)

    seria_filter.short_description = 'Seria'

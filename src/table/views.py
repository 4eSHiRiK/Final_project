from django.shortcuts import render
import matplotlib.pyplot as plt
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from .models import ProdSolutions, ProdCultivations, \
    Product, ProdSpec, ProdSeria, Equipment, ProdEquipment, Solution, \
    Cultivation
from .serializers import ProdSolutionsSerializer, ProdCultivationsSerializer


def plug(request):
    return render(request, 'plug.html')


def homepage(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'homepage.html', context)


def prod_spec(request, pk):
    product = Product.objects.get(pk=pk)
    specs = ProdSpec.objects.filter(product=product)
    context = {
        'product': product,
        'specs': specs,
    }
    return render(request, 'prod_spec.html', context)


def prod_series_equip(request, name_spec):
    spec = ProdSpec.objects.get(name_spec=name_spec)
    series = ProdSeria.objects.filter(
        prod_spec__name_spec__contains=name_spec
    )
    equipment = Equipment.objects.filter(
        prod_spec__name_spec__contains=name_spec
    )
    context = {
        'name_spec': name_spec,
        'series': series,
        'equipment': equipment,
        'spec': spec,
    }
    return render(request, 'prod_seria_equip.html', context)


def equipment_func(request, name_current_equipment):
    equipment = ProdEquipment.objects.get(
        name_equip__name_current_equipment__contains=name_current_equipment
    )
    context = {
        'equipment': equipment,
        'name_current_equipment': name_current_equipment,
    }
    return render(request, 'equipment.html', context)


def prod_series(request, name_seria):
    seria = ProdSeria.objects.get(name_seria=name_seria)
    prod_solution = Solution.objects.filter(
        prod_ser_sol__name_seria__contains=name_seria
    )
    prod_cultivation = Cultivation.objects.filter(
        prod_ser_cult__name_seria__contains=name_seria
    )
    context = {
        'prod_solution': prod_solution,
        'prod_cultivation': prod_cultivation,
        'name_seria': name_seria,
        'seria': seria,
    }
    return render(request, 'prod_series.html', context)


def graphik_all(request, name_seria):  # prod_spec

    # data_list = ProdCultivations.objects.filter(
    # cultivation__prod_ser_cult__prod_spec__name_spec__contains=name_seria)
    save_lst_range_1 = Cultivation.objects.filter(
        prod_ser_cult__prod_spec__name_spec__contains=name_seria)  # prod_spec
    save_lst_range_2 = ProdSeria.objects.filter(
        prod_spec__name_spec__contains=name_seria)
    save_lst = [0 for x in range(int(len(save_lst_range_1) /
                                     len(save_lst_range_2)))]
    fin_lst = []
    count = 0
    all_data = ProdSeria.objects.filter(
        prod_spec__name_spec__contains=name_seria)  # prod_spec
    fig, ax = plt.subplots()

    for elem1 in all_data:
        cur_data = ProdCultivations.objects.filter(
            cultivation__prod_ser_cult__name_seria=elem1
        )
        count += 1
        all_lst_c_up_to = []

        for i, elem_2 in enumerate(cur_data):
            all_lst_c_up_to.append(elem_2.concentration_up_to)
            plt.text(i-0.05, elem_2.concentration_up_to+0.3,
                     elem_2.concentration_up_to)
            save_lst[i] += elem_2.concentration_up_to
        ax.plot(all_lst_c_up_to, linewidth=0.1+count,
                marker='d', linestyle='dashed', label=elem_2.cultivation,
                color=(0+count/20, 0, 0))

    for i, elem_3 in enumerate(save_lst):
        fin_lst.append(elem_3/count)
        plt.text(i - 0.05, elem_3/count + 0.3, elem_3/count)

    ax.plot(fin_lst, color='red', linewidth=3, linestyle='--', label='average')
    # ax.scatter(all_st_c_after, all_lst_c_up_to, s=50, facecolor='g',
    # edgecolor='k')
    ax.set(xlabel='Stadia', ylabel='Value', title='Average statistics')
    plt.legend(loc='upper left')
    ax.grid()

    plt.savefig('table/static/matplotlib/graphik_all.png')

    context = {
        'fin_lst': fin_lst,
        'count': count,
        'name_seria': name_seria,
        'all_data': all_data,
        'save_lst': save_lst,
        }

    return render(request, 'graphik_all.html', context)


def graphik_result(request, name_spec):
    name_lst = []
    result_lst = []
    fig, ax = plt.subplots()
    result_data = ProdSeria.objects.filter(
        prod_spec__name_spec__contains=name_spec)
    for i, elem in enumerate(result_data):
        result_lst.append(int(elem.total_result))
        name_lst.append(elem.name_seria)
        plt.text(i, float(elem.total_result), '%d' % float(elem.total_result),
                 ha='center')
    ax.bar(name_lst, result_lst)
    ax.set(xlabel='Seria', ylabel='Total value, thousand doses',
           title='Seria release')
    plt.savefig('table/static/matplotlib/graphik_result.png')

    context = {
        'name_spec': name_spec,
        'name_lst': name_lst,
        'result_lst': result_lst,
        'result_data': result_data,
    }

    return render(request, 'graphik_result.html', context)


def graphik_cur(request, name_seria):
    lst_c_up_to = []
    lst_c_after = []
    lst_v_up_to = []
    lst_v_after = []
    lst_ph = []
    lst_glu = []
    lst_lact = []
    date_lst = []
    oper_lst = []
    fig, ax = plt.subplots(figsize=(15, 7), layout='constrained')
    data = ProdCultivations.objects.filter(
        cultivation__prod_ser_cult__name_seria__contains=name_seria)
    for i, elem in enumerate(data):
        lst_c_up_to.append(elem.concentration_up_to)
        lst_c_after.append(elem.concentration_after)
        lst_v_up_to.append(elem.viability_up_to)
        lst_v_after.append(elem.viability_after)
        lst_ph.append(elem.ph)
        lst_glu.append(elem.glucose)
        lst_lact.append(elem.lactose)
        date_lst.append(elem.date)
        oper_lst.append(elem.cultivation.name_of_cultivation)
        plt.text(elem.date, elem.concentration_up_to, elem.concentration_up_to)
    ax.plot(date_lst, lst_c_up_to, marker='d')
    # ax.bar(date_lst, lst_c_up_to)
    ax.set(xlabel='Date', ylabel='Concentration up to',
           title='Seria statistic')
    # cdf = mpl.dates.ConciseDateFormatter(ax.xaxis.get_major_locator())
    # ax.xaxis.set_major_formatter(cdf)
    # ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
    # ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
    # ax.xaxis.set_major_locator(mpl.dates.DayLocator())
    # ax.xaxis.set_minor_locator(mpl.dates.DayLocator())
    for label in ax.get_xticklabels(which='major'):
        label.set(rotation=30, horizontalalignment='right')
    ax.grid()
    plt.savefig('table/static/matplotlib/graphik_cur.png')

    context = {
        'name_seria': name_seria,
        'data': data,
        'lst_c_up_to': lst_c_up_to,
        'lst_c_after': lst_c_after,
        'lst_v_up_to': lst_v_up_to,
        'lst_v_after': lst_v_after,
        'lst_ph': lst_ph,
        'lst_glu': lst_glu,
        'lst_lact': lst_lact,
        'date_lst': date_lst,
        'oper_lst': oper_lst,
    }

    return render(request, 'graphik_cur.html', context)


def current_cultivation(request, name_of_cultivation):
    cur_cultivation = ProdCultivations.objects.get(
        cultivation__name_of_cultivation__contains=name_of_cultivation
    )
    context = {
        'cur_cultivation': cur_cultivation,
        'name_of_cultivation': name_of_cultivation,
    }
    return render(request, 'current_cultivation.html', context)


def current_solution(request, name_of_solution):
    cur_solution = ProdSolutions.objects.get(
        solution__name_of_solution__contains=name_of_solution
    )
    context = {
        'cur_solution': cur_solution,
        'name_of_solution': name_of_solution,
    }
    return render(request, 'current_solution.html', context)


class ProdCultivationsViewSet(viewsets.ModelViewSet):
    queryset = ProdCultivations.objects.all()
    serializer_class = ProdCultivationsSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ['cultivation__prod_ser_cult__name_seria']


class ProdSolutionsViewSet(viewsets.ModelViewSet):
    queryset = ProdSolutions.objects.all()
    serializer_class = ProdSolutionsSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['solution_seria']


def about(request):
    return render(request, 'about.html')

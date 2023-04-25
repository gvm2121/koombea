from django.core.paginator import Paginator
from django.conf import settings


def get_paginator(total,request,paginacion=settings.TOTAL_PAGINAS):
    page = request.GET.get("page")
    paginator = Paginator(total, paginacion)
    datos = paginator.get_page(page)
    numeros = []
    if len(datos)>= paginacion:
        for ultima in range(1,datos.paginator.num_pages):
            numeros.append(ultima)
        numeros.append(ultima+1)
    return [datos,numeros,page]

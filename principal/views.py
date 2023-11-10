from django.shortcuts import render

# Create your views here.
from principal.models import Empresa
def lista_bebidas(request):
    category_list = Empresa.objects.all()
    context = {'lista': category_list}
    return render(request, 'empresa.html', context)


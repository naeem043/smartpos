from django.shortcuts import render
from .models import MenuInfo
# Create your views here.
def index(request):
    menu_list = MenuInfo.objects.all().order_by('menu_order')
    context = {'menu_list':menu_list}
    return render(request,'pos/index.html',context )
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Brands, Catalog, Stores, Suppliers, AliOrdersProductList, AliProducts, AliOrders
from .forms import BrandForm, SupplierForm, StoresForm, CatalogForm, LoginForm, UserRegForm, OrderInfoForm
from django.contrib.auth import authenticate, login, logout, views
from django.contrib.auth.decorators import login_required
from .servicesCRM import serviceAli, check_funcs, orderAliInfo
from django.core.paginator import Paginator
from services.cdek_services import CdekAPI, CdekOrder


# пункты отправления посылок
SOURCE_CITIES = {'selectTarifSaratov':'SAR4', 'selectTarifKazan':'KZN37',
                 'selectTarifChelny': 'NCHL6'}
# сдэк
Account='0372b3fff5d6707cd1633469403952df'
Secure_password='afc14015cce5555ce582bf97b963d2d2'

# Create your views here.
class BrandsView(ListView):
    pass
    # model = Brands
    # context_object_name = 'brands'
    # template_name = 'crmApp/brands/brands_list.html'

class BrandDelete(DeleteView):
    model = Brands
    context_object_name = 'brand'
    template_name = 'brands/brands_delete.html'
    success_url = reverse_lazy('crm:brand_list')

class CatalogView(ListView):
    model=Catalog
    context_object_name = 'catalog_items'
    template_name = 'catalogModels/catalog_models_list.html'

class BrandDetail(DetailView):
    model=Brands
    context_object_name = 'brand'
    template_name='brands/brand_detail.html'

class CatalogModelDetail(DetailView):
    model = Catalog
    context_object_name = 'item'
    template_name = 'catalogModels/catalog_model.html'

class StoresList(ListView):
    model=Stores
    context_object_name = 'store'
    template_name = 'stores/store_list.html'

def store_add(request):
    if request.method=='POST':
        form = StoresForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crm:store_list')
    else:
        form=StoresForm()
        return render(request, 'stores/store_add.html', context={'form': form})

def store_delete(request, slug):
    item=Stores.objects.get(slug=slug)
    if request.method=='POST':
        item.delete()
        return redirect('crm:store_list')
    else:
        return render(request, 'stores/store_delete.html', context={'item':item})

class StoreItem(DetailView):
    model = Stores
    context_object_name = 'item'
    template_name = 'stores/store_details.html'

class BrandAdd(CreateView):
    form_class = BrandForm
    template_name = 'brands/brand_add.html'
    def form_valid(self, form):
        Brands.objects.create(**form.cleaned_data)
        return redirect('crm:brand_list')

def supplier_list(request):
    supp_list=Suppliers.objects.all()
    return render(request, 'suppliers/suppliers_list.html', context={'supp_list': supp_list})

def supplier_details(request, slug):
    supp_detail=Suppliers.objects.get(slug=slug)
    return render(request, 'suppliers/supplier_detail.html', context={'supp_detail': supp_detail})

def supplier_add(request):

    if request.method=='POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            Suppliers.objects.create(**form.cleaned_data)
            return redirect('crm:suppliers_list')
    else:
        form = SupplierForm()
        return render(request, 'suppliers/supplier_add.html', context={'form': form})

class SupplierDelete(DeleteView):
    model=Suppliers
    context_object_name = 'item'
    template_name = 'suppliers/supplier_delete.html'
    success_url = reverse_lazy('crm:suppliers_list')

class CataloModelDelete(DeleteView):
    model = Catalog
    context_object_name = 'item'
    template_name = 'catalogModels/catalog_model_delete.html'
    success_url = reverse_lazy('crm:catalog_list')

def catalogModels_add(request):

    if request.method=='POST':
        form = CatalogForm(request.POST)
        if form.is_valid():
            new_obj=form.save()
            return redirect(new_obj)
    else:
        form = CatalogForm()
        return render(request, 'catalogModels/catalog_model_add.html', context={'form': form})

class BrandEdit(UpdateView):
    model = Brands
    context_object_name = 'brand'
    template_name = 'crmApp/brands/brand_edit.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('crm:brand_list')

def supplierEdit(request, slug):
    obj=Suppliers.objects.get(slug=slug)
    if request.method=='POST':
        form=SupplierForm(request.POST)
        if form.is_valid():
            obj.name=form.cleaned_data['name']
            obj.slug=form.cleaned_data['slug']
            newobj=obj.save()
            return redirect('crm:suppliers_list')
    else:
        form = SupplierForm({'name': obj.name, 'slug': obj.slug})
        return render(request, 'suppliers/supplier_edit.html', context={'form': form})

def catalogModelEdit(request, slug):
    obj=Catalog.objects.get(slug=slug)
    if request.method=='POST':
        form=CatalogForm(request.POST, instance=obj)
        if form.is_valid():
            update_obj=form.save()
            return redirect(update_obj)

    else:
        form=CatalogForm(instance=obj)
        return render(request, 'catalogModels/catalog_model_edit.html', context={'form': form})

class StoreEdit(UpdateView):
    model = Stores
    context_object_name = 'item'
    template_name = 'crmApp/stores/stores_edit.html'
    fields = ['catalog_item', 'quantity', 'wholesale_price', 'supplier', 'slug']
    success_url = reverse_lazy('crm:store_list')


# def userLogin(request):
#     if request.method=='POST':
#         form=LoginForm(request.POST)
#         if form.is_valid():
#             username=form.cleaned_data['username']
#             psw=form.cleaned_data['password']
#             user=authenticate(request, username=username, password=psw)
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     url=request.GET.get('next','')
#                     return redirect(settings.LOGIN_REDIRECT_URL if url=='' else url)
#                 else:
#                     return HttpResponse('Юзер не активен')
#             else:
#                 return HttpResponse('Облом')
#         else: return HttpResponse(form.errors)
#     else:
#         form=LoginForm()
#         return render(request, 'registration/login.html', context={'form':form})
#
# def userLogout(request):
#     logout(request)
#     return HttpResponse('разлогинился')


@login_required
def dashboard(request):
    return render(request,'dashboard/dashboard.html')

@login_required
def dashboard2(request):
    return render(request,'dashboard/dashboard2.html')

def userNew(request):
    if request.method=='POST':
        form=UserRegForm(request.POST)
        if form.is_valid():
            new_user=form.save()
            login(request, new_user)
            return render(request, 'registration/newUserDone.html')
    else:
        form=UserRegForm()
    return render(request, 'registration/newUser.html', context={'form':form})

def pressButImportOrders(request):
    a=serviceAli()
    # a.updateGroupList()
    #a.updateProducts(1)
    a.updateOrderList(1)
    return redirect('crm:dashboard')

class ProductsList(ListView):
    model=AliProducts
    context_object_name = 'productsList'
    template_name = 'products-list/products_list.html'


def productInfoDetail(request, id):
    try:
        product_detail = AliProducts.objects.get(product_id=id)
        a=serviceAli()
        productDetailInfo=a.getProduct(id)

    except Exception as err:
        print(f' ошибка: {err}')
        return redirect('crm:products_list')

    return render(request, context={'product_info':product_detail, 'product_detail_info':productDetailInfo}, template_name='products-list/product_info.html')


# class OrdersList(ListView):
#     model=AliOrders
#     context_object_name = 'ordersList'
#     template_name = 'orders/orders_list.html'


def orderList(request):
    orders = AliOrders.objects.order_by('-gmt_create')
    paginator = Paginator(orders, 20, orphans=5, allow_empty_first_page=True)
    if 'page' in request.GET:
        page_num=request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    context = {'page': page, 'data':page.object_list}
    return render(request, 'orders/orders_list.html', context)

@check_funcs
def OrderInfoDetail(request, id):
    def list_of_choises(): # делаем списки для выбора ПВЗ в выпадающем меню
        for i in SOURCE_CITIES:
            form.fields[i].choices=list(map(lambda x: (x['info']['id'], x['info']['name'] + ' - ' + x['result']['price']),
                       orderDetailInfo.cdek_tarifes[i]))
        form.fields['selectPVZ'].choices = list(map(lambda x: (x['code'], x['location']['address']), orderDetailInfo.cdek_pvz))
    ali = serviceAli()
    orderDetailInfo=orderAliInfo(id)
    # print(orderDetailInfo)
    # orderDetailInfo = ali.getOrder(id)
    if request.method=='GET':
        form = OrderInfoForm(initial={'recieverFIO':orderDetailInfo.FIO, 'insurance':0})
        return render(request, context={'order_info': orderDetailInfo, 'form': form},
                      template_name='orders/order_info.html')
    else:
        form=OrderInfoForm(request.POST)
        list_of_choises()
        if form.is_valid:
            cdek = CdekAPI(client_id=Account, client_secret=Secure_password)
            d = dict()
            selectedShippingFrom=form.data['selectShippingFrom']
            selectedTariffCode=form.data[selectedShippingFrom]
            d['tariff_code'] =selectedTariffCode
            d['name'] = form.data['recieverFIO']
            d['delivery_point'] =form.data['selectPVZ']
            d['phone'] = orderDetailInfo.phoneNumber
            d['packages'] = orderDetailInfo.product_list(form.data['insurance'])
            d['number'] = orderDetailInfo.order_id
            d['shipment_point']=SOURCE_CITIES[form.data['selectShippingFrom']]
            newO = CdekOrder(**d)
            result = cdek.new_order(newO)
            print(result)
            return render(request, context={'order_info': orderDetailInfo, 'form': form},
                      template_name='orders/order_info.html')



# def createCdekOrder(request,id):
#     a=CdekAPI(client_id=Account, client_secret=Secure_password)
#     b=serviceAli()
#     orderInfo=b.getOrder(id)
#     d=dict()
#     d['tariff_code']=orderInfo.cdek_tarifes['fromSaratov'][0]['info']['id']
#     d['name']=orderInfo.FIO
#     d['delivery_point']=orderInfo.cdek_pvz[0]['code']
#     d['phone']=orderInfo.phoneNumber
#     d['packages']=orderInfo.product_list
#     d['number']=orderInfo.order_id
#
#     newO=CdekOrder(**d)
#     result=a.new_order(newO)
#     print(result)
#
#     return redirect('crm:order_info', id)
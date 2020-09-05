from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Brands, Catalog, Stores, Suppliers
from .forms import BrandForm, SupplierForm, StoresForm, CatalogForm, LoginForm, UserRegForm
from django.contrib.auth import authenticate, login, logout, views
from django.contrib.auth.decorators import login_required
from MyCRM import settings

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
    return redirect('crm:dashboard')

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DeleteView, DetailView, UpdateView
from .forms import ClientForm, ClientModelForm
from .models import Category, Product, ClientModel, Client
from django.http import Http404, HttpResponse
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView,View


class HomePageView(ListView):
    model = Product
    template_name = "shop/home.html"
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['products_list'] = Product.published.all().order_by('-published_time')

        context['home_product'] = \
        Product.published.all().filter(category__name='Uy mahsuloti').order_by("-published_time")[0]
        context['good_product'] = \
        Product.published.all().filter(category__name='Davolovchi mahsulot').order_by("-published_time")[0]
        context['clever_watch'] = \
        Product.published.all().filter(category__name='Aqli soat').order_by("-published_time")[0]
        context['cars_product'] = \
        Product.published.all().filter(category__name='Mashina mahsuloti').order_by("-published_time")[0]
        context['present_product'] = \
        Product.published.all().filter(category__name="Sovg'a").order_by("-published_time")[0]



        return context


def product_detail(request, product):

    product=get_object_or_404(Product, slug=product, status=Product.Status.Published)
    # comments=product.comments.filter(active=True)
    clients=product.clients.filter(status="YC")
    new_comment=None
    if request.method=="POST":
        comment_form=ClientForm(request.POST)
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.product=product
            new_comment.save()
            comment_form=ClientForm()
    else:
        comment_form=ClientForm()




    context={
            'product' : product,
            'clients' : clients,
            # 'comments' : comments,
            'comment_form' : comment_form,
            'new_comment' : new_comment,
        }

    return render(request, 'crud/detail.html', context)

class CategoryPageView(ListView):
    model = Product
    template_name = "shop/category_full.html"
    context_object_name = 'categories'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['products_list'] = Product.published.all().order_by('-published_time')
        context['product']=Product.objects.get(Product, status=Product.Status.Published, )
        context['home_product'] = \
        Product.published.all().filter(category__name='Uy mahsuloti').order_by("-published_time")[0]
        context['good_product'] = \
        Product.published.all().filter(category__name='Davolovchi mahsulot').order_by("-published_time")[0]
        context['clever_watch'] = \
        Product.published.all().filter(category__name='Aqli soat').order_by("-published_time")[0]
        context['cars_product'] = \
        Product.published.all().filter(category__name='Mashina mahsuloti').order_by("-published_time")[0]
        context['present_product'] = \
        Product.published.all().filter(category__name="Sovg'a").order_by("-published_time")[0]



        return context

def categoryview(request, category_id):
    products = Product.objects.filter(category=category_id)
    categories=Category.objects.all()
    context={
        'products': products,
        'categories':categories
    }


    render(request, 'shop/category_full.html', context)

class ContactPageView(CreateView):
    model = ClientModel
    form_class = ClientModelForm
    template_name = 'crud/create.html'




# def ContactPageView(request):
#     form=ClientModelForm(request.POST or None)
#     print(request.POST)
#     print(form)
#     if request.method=="POST":
#         form.save()
#         return HttpResponse("malumot kiritildi")
#     context={
#         'form':form
#     }

    # return render(request, 'crud/create.html', context)
# class Product_detail(TemplateView):
#     template_name = 'crud/detail.html'

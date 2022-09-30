from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from goods.models import Painting
from .forms import PaintingCreateForm


"""def main_page(request):
    return render(request, "goods/main.html")"""


class MainPageView(TemplateView):
    template_name = "goods/main.html"


"""class PaintingsListView(ListView):
    template_name = "goods/shop.html"
    model = Painting
    context_object_name = "paintings"""


def paintings_shop_view(request):
    title = request.GET.get("title")
    theme = request.GET.get("theme")
    order = request.GET.get("order")
    if order is None or order == "" or order == "ASC":
        order = "price"
    elif order == "DSC":
        order = "-price"
    if title is None:
        title = ""
    if theme is None:
        theme = ""
    if theme == "":  
        paintings = Painting.objects.filter(name__icontains=title).order_by(order)
    else:
        paintings = Painting.objects.filter(name__icontains=title, subject=theme).order_by(order)
    ctx = {
        "paintings": paintings, "title": title
    }
    return render(request, "goods/shop.html",ctx )


"""def painting_detail_view(request, slug):
    painting = Painting.objects.get(slug=slug)
    return render(request, "goods/detail.html", {"painting": painting})"""

class PaintingDetailView(DetailView):
    template_name = "goods/detail.html"
    model = Painting
    context_object_name = "painting"


def painting_create_view(request):
    if request.method == "POST":
        form = PaintingCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("shop")
    else:
        form = PaintingCreateForm()
    ctx = {
        "form": form
        }
    return render(request, "goods/create.html", ctx)
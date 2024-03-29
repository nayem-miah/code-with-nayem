from django.shortcuts import render, redirect, get_object_or_404
from header.models import Top_header, Header
from footer.models import Top_footer1, Top_footer2, Top_footer4, Top_footer3
from about.models import Client
from .models import *


def portfolio(request):
    template = 'portfolio.html'
    top_header = Top_header.objects.order_by()
    header = Header.objects.order_by()
    top_footer1 = Top_footer1.objects.order_by()
    top_footer2 = Top_footer2.objects.order_by()
    top_footer3 = Top_footer3.objects.order_by()
    top_footer4 = Top_footer4.objects.order_by()
    client = Client.objects.order_by()
    all_cat = Category.objects.all()

    cat = request.GET.get('categ')

    print(cat)

    if cat == None:

        portfolio = Portfolio.objects.all()

    else:
        portfolio = Portfolio.objects.filter(catagory__name=cat)

    context = {
        'top_headerdata': top_header,
        'headerdata': header,
        'footer1': top_footer1,
        'footer2': top_footer2,
        'footer3': top_footer3,
        'footer4': top_footer4,
        'clientdata': client,
        'portfolio': portfolio,
        'category': all_cat,

    }
    return render(request, template_name=template, context=context)


def details(request, pk, title):

    template = 'portfolio-details.html'
    top_header = Top_header.objects.order_by()
    header = Header.objects.order_by()
    top_footer1 = Top_footer1.objects.order_by()
    top_footer2 = Top_footer2.objects.order_by()
    top_footer3 = Top_footer3.objects.order_by()
    top_footer4 = Top_footer4.objects.order_by()
    portfolio = Portfolio.objects.all()
    post = get_object_or_404(portfolio, id=pk, title=title)

    context = {
        'top_headerdata': top_header,
        'headerdata': header,
        'footer1': top_footer1,
        'footer2': top_footer2,
        'footer3': top_footer3,
        'footer4': top_footer4,
        'post': post,
    }

    return render(request, template_name=template, context=context)

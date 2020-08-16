from django.shortcuts import render, redirect
from .forms import Help_requestForm
from .models import Help_request
from django.core.paginator import Paginator


# Create your views here.


def main(request):
    return render(request, 'index.html')


def help_form(request):
    if request.method == 'POST':
        form = Help_requestForm(request.POST)
        if form.is_valid():
            form.save()
            if form.cleaned_data['help_type']=='need_help':
                return redirect('requests_list')
            else:
                return redirect('offers_list')
    else:
        form = Help_requestForm
    return render(request, 'help_form.html', {'form': form})


def requests_list(request):
    requests_data = Help_request.objects.filter(help_type='need_help')
    paginator = Paginator(requests_data, 20)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''
    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'requests_data': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
    }
    return render(request, 'requests.html', context=context)


def offers_list(request):
    offers_data = Help_request.objects.filter(help_type='can_help')
    paginator = Paginator(offers_data, 20)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''
    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'offers_data': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
    }

    return render(request, 'offers.html', context=context)
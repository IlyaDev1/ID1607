from django.shortcuts import render
from .models import Links


def index(request):
    correct_links = Links.objects.all()
    wrong_links = Links.objects.order_by('?')
    nums = [i for i in range(1, 25)]
    wrong_links = zip(nums, wrong_links)
    print(request.GET.get('answer') == 'true')

    data = {
        'correct_links': correct_links,
        'wrong_links': wrong_links,
        'answer': request.GET.get('answer') == 'true'
    }

    return render(request, 'index.html', context=data)

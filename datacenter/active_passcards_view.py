from django.shortcuts import render

from datacenter.models import Passcard


def active_passcards_view(request):
    all_passcards = Passcard.objects.all()
    context = {
        'active_passcards': all_passcards.filter(is_active=True),
    }
    return render(request, 'active_passcards.html', context)

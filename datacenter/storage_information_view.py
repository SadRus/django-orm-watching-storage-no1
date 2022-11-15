from django.shortcuts import get_object_or_404
from django.shortcuts import render

from datacenter.models import Visit
from .models import get_duration, format_duration


def storage_information_view(request):
    not_leaved_visitors = Visit.objects.filter(leaved_at__isnull=True)
    get_object_or_404(not_leaved_visitors)

    non_closed_visits = []
    for visit in not_leaved_visitors:
        duration = get_duration(visit)
        non_closed_visits.append(
            {
                'who_entered': visit.passcard,
                'entered_at': visit.entered_at,
                'duration': format_duration(duration)
            }
        )
        
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)

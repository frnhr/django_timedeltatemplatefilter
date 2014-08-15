from datetime import timedelta
from django.shortcuts import render_to_response

# Create your views here.
from django.template import RequestContext


def home(request):
    return render_to_response(
        'home.html',
        {
            'dt': timedelta(seconds=4 * 3600 + 3 * 60 + 21),  # 4h3m21s
            'dt2': timedelta(seconds=7 * 365 * 24 * 3600 + 65 * 24 * 3600 + 4 * 3600 + 3 * 60 + 21),  # 5y 4h3m21s
        },
        RequestContext(request)
    )


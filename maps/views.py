from django.shortcuts import render


def maps_view(request):
    return render(request, 'maps/maps.html')
from datetime import date
from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from card.models import Card


class IndexView(View):
    def get(self, request):
        cards = Card.objects.all()

        context = {
            'cards': cards,
        }

        return render(request, 'index.html', context)


class CardView(View):
    def get(self, request, card_id):
        card = Card.objects.get(id=card_id)

        context = {
            'card': card,
        }

        return render(request, 'card.html', context)


class GenerateCardView(View):
    def get(self, request):
        series = Card.generate_string(4)
        number = Card.generate_string(12)

        while Card.objects.filter(series=series, number=number).exists():
            series = Card.generate_string(4)
            number = Card.generate_string(12)

        Card.objects.create(
            series=series,
            number=number,
            release_date=date.today(),
            end_date=date.today(),
        )

        return redirect('/')


class SearchView(View):
    def get(self, request):
        query = request.GET.get('query')
        
        cards = Card.objects.filter(
            Q(series__icontains=query) |
            Q(number__icontains=query) |
            Q(release_date__icontains=query) |
            Q(end_date__icontains=query) |
            Q(status__icontains=query)
        )

        context = {
            'cards': cards,
        }

        return render(request, 'search.html', context)
    
    

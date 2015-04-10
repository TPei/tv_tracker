from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.forms.models import modelform_factory
from django.db.models import Q
from django.forms import Textarea
from shows.models import *


def index(request):
    shows = Show.objects.all()
    template = loader.get_template('shows/index.html')
    context = RequestContext(request, {'shows': shows})
    return HttpResponse(template.render(context))


def search(request):
    shows = Show.objects.none()
    qs = ""
    if request.method == 'GET' and 'q' in request.GET:
        query = request.GET['q']
        qs = query
        if query is not None:
            if query == "*":
                shows = Show.objects.all()
            else:
                query = query.split()
                for word in query:
                    and_query = Show.objects.none()

                    # zum suchen mit UND-Verknüpfung
                    if '+' in word:
                        word = word.split('+')
                        and_query = Show.objects.all()
                        for w in word:
                            and_query = and_query & Show.objects.filter(Q(tags__name__iexact=w))
                        word = '/'

                    shows = shows | \
                             Show.objects.filter(Q(tags__name__iexact=word) | Q(name__icontains=word)).distinct() | \
                             and_query.distinct()
                for show in shows:
                    show.rating = show.rating()
    template = loader.get_template('shows/search.html')
    context = RequestContext(request, {'shows': shows, 'qs': qs, })
    return HttpResponse(template.render(context))


def show(request, show_id):
    show = get_object_or_404(Show, pk=show_id)
    RatingForm = modelform_factory(Rating, exclude=('id', 'show', ))
    form = RatingForm(request.POST or None)
    if form.is_valid():
        rating = form.save(commit=False)
        rating.show = show
        rating.save()
        return HttpResponseRedirect(reverse('show', args=(show_id,)))
    else:
        tags = show.tags.all()
        ratings = Rating.objects.filter(show=show_id)
        template = loader.get_template('shows/show.html')
        context = RequestContext(request, {'show': show, 'tags': tags, 'rating': show.rating(), 'rating_count': show.rating_count(), 'ratings': ratings, 'form': form, })
        return HttpResponse(template.render(context))


def add(request):
    ShowForm = modelform_factory(Show, exclude=('id',), widgets={'description': Textarea()})
    form = ShowForm(request.POST or None)
    if form.is_valid():
        new_show = form.save()
        return HttpResponseRedirect(reverse('show', args=(new_show.id,)))
    else:
        template = loader.get_template('shows/add.html')
        context = RequestContext(request, {'form': form})
        return HttpResponse(template.render(context))
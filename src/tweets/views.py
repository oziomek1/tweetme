from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.http import  HttpResponseRedirect
from django.urls import reverse_lazy
from django.db.models import Q
from django.views import View

from .forms import TweetModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin
from .models import Tweet

# Create your views here.


class RetweetView(View):
    def get(self, request, pk, *args, **kwargs):
        tweet = get_object_or_404(Tweet, pk=pk)
        if request.user.is_authenticated:
            new_tweet = Tweet.objects.retweet(request.user, tweet)
            return HttpResponseRedirect('/')
        return HttpResponseRedirect(tweet.get_absolute_url())


# Create
class TweetCreateView(FormUserNeededMixin, generic.CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'


# Retrieve
class TweetDetailView(generic.DetailView):
    queryset = Tweet.objects.all()


class TweetListView(LoginRequiredMixin, generic.ListView):
    queryset = Tweet.objects.all()

    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()
        # print(self.request.GET)
        query = self.request.GET.get('q', None)
        if query is not None:
            qs = qs.filter(
                    Q(title__icontains=query) |
                    Q(text__icontains=query) |
                    Q(user__username__icontains=query)
                    )
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TweetListView, self).get_context_data(**kwargs)
        context['create_form'] = TweetModelForm()
        context['create_url'] = reverse_lazy('tweet:create')
        return context

# def tweet_detail_view(request, id=1):
#     obj = Tweet.objects.get(id=id)  # GET from DB
#     print(obj)
#     context = {
#         "object": obj
#     }
#     return render(request, 'tweets/detail_view.html', context)
#
# def tweet_list_view(request):
#     queryset = Tweet.objects.all()
#     for obj in queryset:
#         print(obj.title)
#     context = {
#         "object_list": queryset
#     }
#     return render(request, 'tweets/list_view.html', context)


# Update
class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, generic.UpdateView):
    form_class = TweetModelForm
    template_name = 'tweets/update_view.html'
    queryset = Tweet.objects.all()
    # success_url = '/tweet/'


# Delete
class TweetDeleteView(generic.DeleteView):
    model = Tweet
    success_url = reverse_lazy('tweet:list')
    template_name = 'tweets/delete_confirm.html'

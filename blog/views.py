from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Count
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    RedirectView,
)
from .models import Post, Movie
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

class UpdateSeatsAPI(APIView):
    def get(self, request, pk, format=None):
        post = get_object_or_404(Post, id=self.request.GET.get('post_id'))
        url_ = post.get_absolute_url()
        post.seats_taken = self.request.GET.get('seats_taken')
        post.save()
        data = {
            'seats_taken': self.request.GET.get('seats_taken'),
        }
        return Response(data)

class PostListView(ListView):
    model = Movie
    template_name = 'blog/home.html'
    context_object_name = 'movies'
    ordering = ['id']

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        movies = Movie.objects.all()
        movie_count = 0
        showtimes = Post.objects.order_by('date')
        for movie in movies:
            movie_count += 1
        context['movie_count'] = movie_count
        context['showtimes'] = showtimes
        return context

class PostDetailView(DetailView, UpdateView):
    model = Post
    fields = ['seats_taken']

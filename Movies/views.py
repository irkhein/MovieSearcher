from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.views.generic import View
from .models import Movie, Person, Casting, Role
from .forms import UserForm, UserLoginForm


# Index View
class IndexView(generic.ListView):
    template_name = 'Movies/index.html'
    context_object_name = 'all_movies'
    paginate_by = 12

    def get_queryset(self):
        return Movie.objects.all()


class MovieDetailView(generic.DetailView):
    model = Movie
    template_name = 'Movies/movie.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = super().get_object()
        if obj is not None:
            context['rate'] = obj.rate()

        context['actor_list'] = self.get_person_list(obj.id, 1)
        context['director_list'] = self.get_person_list(obj.id, 2)

        return context

    @staticmethod
    def get_person_list(movie_id, role_id):
        persons = Casting.objects.filter(movie_id=movie_id, role_id=role_id)
        return persons


class MovieCreate(CreateView):
    model = Movie
    fields = ['name', 'year', 'genre', 'director', 'description', 'movie_picture', 'trailer_url']


class MovieUpdate(UpdateView):
    model = Movie
    fields = ['name', 'year', 'genre', 'director', 'description', 'movie_picture']


class MovieDelete(DeleteView):
    model = Movie
    success_url = reverse_lazy('Movies:index')


def like_movie(request, item_id):
    # try:
    #    movie_item = Movie.objects.get(id=item_id)
    # except Movie.DoesNotExist:
    #    raise Http404("Movie does not exist")
    movie_item = get_object_or_404(Movie, id=item_id)
    movie_item.like += 1
    movie_item.save()

    return redirect('Movies:movie', pk=movie_item.id)


def dislike_movie(request, item_id):

    movie_item = get_object_or_404(Movie, id=item_id)
    movie_item.dislike -= 1
    movie_item.save()

    return redirect('Movies:movie', pk=movie_item.id)


# User create
class UserFormView(View):
    form_class = UserForm
    template_name = 'Movies/registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            # User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns user object if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                #if user.is_active():
                login(request, user)
                return redirect('Movies:index')

        return render(request, self.template_name, {'form': form})


# User login
class UserLoginFormView(View):
    form_class = UserLoginForm
    template_name = 'Movies/registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        #if form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        # returns user object if credentials are correct
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('Movies:index')

        return render(request, self.template_name, {'form': form})


# User logout
class UserLogoutView(View):
    success_url = reverse_lazy('Movies:index')
    template_name = 'Movies/logout.html'

    def post(self, request):
        logout(request)
        return redirect(self.success_url)

    def get(self, request):
        return render(request, self.template_name)
    # HttpResponseRedirect('')  # return render(request, 'Movies/index.html') HttpResponseRedirect('Movies:index')


# Person views
class PersonDetailView(generic.DetailView):
    model = Person
    template_name = 'Movies/person.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = super().get_object()
        if obj is not None:
            context['rate'] = obj.rate()

        # role.id = 1 - actor, role.id = 2 - director
        movie_list = Casting.objects.filter(person_id=obj.id, role_id=1)
        context['movie_list'] = movie_list
        return context


def like_person(request, item_id):
    item = get_object_or_404(Person, id=item_id)
    item.like += 1
    item.save()

    return redirect('Movies:person', pk=item_id)


def dislike_person(request, item_id):
    item = get_object_or_404(Person, id=item_id)
    item.like -= 1
    item.save()

    return redirect('Movies:person', pk=item_id)


# Person list view
class PersonListView(generic.ListView):
    template_name = 'Movies/person_list.html'
    context_object_name = 'person_list'

    def get_queryset(self):
        return Casting.objects.filter(movie_id=self.kwargs['pk'], role_id=1)















from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,DeleteView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Note
from .forms import NotesForm
# Create your views here.


class NotesListView(LoginRequiredMixin,ListView):
    model = Note
    context_object_name = "notes"
    template_name = 'notes/notes_list.html'
    login_url = '/login'

    def get_queryset(self):
        return self.request.user.notes.all()


class NotesDetailsView(DetailView):
    model = Note
    context_object_name = "note"
    template_name = 'notes/notes_detail.html'

class NotesCreateView(LoginRequiredMixin,CreateView):
    model = Note
    template_name = 'notes/notes_form.html'
    # fields = ['title','text']
    success_url = '/notes'
    form_class = NotesForm

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url)



class NotesUpdateView(LoginRequiredMixin,UpdateView):
    model = Note
    template_name = 'notes/notes_form.html'
    success_url = '/notes'
    form_class = NotesForm

# def list(request):
#     notes = Note.objects.all()

#     return render(request,'notes/notes_list.html',{"notes":notes})


# def detail(request,pk):
#     note = Note.objects.get(pk=pk)
#     return render(request,'notes/notes_detail.html',{"note":note})
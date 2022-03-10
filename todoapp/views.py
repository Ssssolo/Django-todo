from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .forms import AdaugareForm, EditareForm
from .models import Todo
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
class Index(ListView):
    template_name = "todoapp/index.html"
    paginate_by = 10

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            lista = ''
        else:
            lista = Todo.objects.filter(autor=self.request.user).order_by('-prioritate', '-data_creare')
        return lista

@login_required
def adaugare(request):
    form = AdaugareForm(request.POST or None)
    context = {
        'form': form,
    }

    # Verificam daca request-ul este de tip POST
    if request.method == 'POST':
        # Verificam daca formularul este valid
        if form.is_valid():
            user = User.objects.get(id=request.user.id)
            obj = form.save(commit= False)
            obj.autor = user
            obj.save()
            
            messages.success(request, "Notita dvs. a fost adaugata cu succes!")
            return redirect('index')

    return render(request, 'todoapp/adaugare.html', context)

@login_required
def editare(request, id):
    # Preluam datele corespunzatoare pentru id-ul primit prin parametrul id din URL
    obj = get_object_or_404(Todo, id=id)
    # Memoram datele actuale ale obiectului cu id=id
    initial_data = {
        'titlu': obj.titlu,
        'descriere': obj.descriere,
        'completat': obj.completat,
        'data_creare': obj.data_creare,
    }

    # Transmitem datele actuale catre formular pentru a le afisa ca fiind default
    form = EditareForm(request.POST or None, instance = obj, initial = initial_data)
    # Verificam daca request-ul este de tip POST
    if request.method == 'POST':
        # Verificam daca formularul este valid
        if form.is_valid():
            obj = form.save(commit= False)
            obj.save()
            
            messages.success(request, "Ai editat cu succes aceasta actiune!")

            context= {
                'form': form
            }
            return render(request, 'todoapp/editare.html', context)
        else:
            context = {
                'form': form,
                'error': 'A aparut o eroare!'
            }
            return render(request, 'todoapp/editare.html', context)
    context = {
        'form': form,
    }
    return render(request, 'todoapp/editare.html', context)

@login_required
def clonare(request, id):
    obj = get_object_or_404(Todo, id=id)
    obj.id = None
    obj.save()
    messages.info(request, "Notita cu titlul \"" + obj.titlu + "\" a fost clonata cu succes!")

    return redirect('index')

@login_required
def prioritate(request, id):
    obj = get_object_or_404(Todo, id=id)

    if obj.prioritate == False:
        obj.prioritate = True
        messages.info(request, "Notita cu titlul \"" + obj.titlu +"\" a fost setata ca avand prioritate!")
    else:
        obj.prioritate = False
        messages.warning(request, "Notita cu titlul \"" + obj.titlu +"\" a fost stearsa ca avand prioritate!")
   
    obj.save() 
    return redirect('index')

@login_required
def completare(request, id):
    obj = get_object_or_404(Todo, id=id)

    if obj.completat == False:
        obj.completat = True
        messages.success(request, "Notita cu titlul \"" + obj.titlu +"\" a fost marcata ca fiind completata!")
    else:
        obj.completat = False
        messages.warning(request, "Notita cu titlul \"" + obj.titlu +"\" a fost marcata ca fiind necompletata!")
    
    obj.save()
    return redirect('index')

@login_required
def sterge(request, id):
    obj = get_object_or_404(Todo, id=id)
    obj.delete()
    messages.info(request, "Ati sters cu succes notita \""+ obj.titlu + "\"!")

    return redirect('index')
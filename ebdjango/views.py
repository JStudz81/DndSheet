from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Character
import math
import json
from .forms import CharForm, CharUpdateForm

def index(request):
    chars = Character.objects.all()
    context = {
        'chars': chars
    }
    return render(request, 'index.html', context)

def character(request, character_id):
    char = get_object_or_404(Character, pk=character_id)

    prof_list = [
        'Acrobatics',
        'Animal Handling',
        'Arcana',
        'Athletics',
        'Deception',
        'History',
        'Insight',
        'Intimidation',
        'Investigation',
        'Medicine',
        'Nature',
        'Perception',
        'Performance',
        'Persuasion',
        'Religion',
        'Sleight of Hand',
        'Stealth',
        'Survival'
    ]

    if request.method == 'GET':
        context = {
            'char': char,
            'str_mod': __abilityMod(char.strength),
            'dex_mod': __abilityMod(char.dexterity),
            'con_mod': __abilityMod(char.constitution),
            'int_mod': __abilityMod(char.intelligence),
            'wis_mod': __abilityMod(char.wisdom),
            'chr_mod': __abilityMod(char.charisma),
            'proficiencies': char.proficiencies,
            'prof_list': prof_list,
            'form': CharUpdateForm(initial={'health': char.health})
        }
        return render(request, 'char.html', context)

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CharUpdateForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            char.health = form.cleaned_data['health']

            char.save()

            return HttpResponseRedirect('/' + character_id)


def createChar (request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CharForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            profs = form.cleaned_data['proficiencies']


            char = Character(
                char_name=form.cleaned_data['char_name'],
                player_name=form.cleaned_data['player_name'],
                max_health=form.cleaned_data['max_health'],
                health=form.cleaned_data['max_health'],
                strength=form.cleaned_data['strength'],
                dexterity=form.cleaned_data['dexterity'],
                constitution=form.cleaned_data['constitution'],
                intelligence=form.cleaned_data['intelligence'],
                wisdom=form.cleaned_data['wisdom'],
                charisma=form.cleaned_data['charisma'],
                proficiencies=json.dumps(profs)
            )

            char.save()

            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CharForm()

    return render(request, 'createChar.html', {'form': form})


def __abilityMod(attr):
    num = math.floor(.5*attr - 5)
    if num >= 0:
        return '+' + str(num)
    else:
        return '-' + str(-num)

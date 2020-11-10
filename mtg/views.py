import pdb
from django.shortcuts import render, redirect, get_object_or_404

from .models import Player, Match, Turn
from .forms import PlayerUpdateForm, MatchCreateForm, TurnCreateForm

def home(request):
    return render(request, 'mtg/home.html')

def PlayerView(request):
    players = Player.objects.all()
    return render(request, 'mtg/players.html', {'players':players})

def PlayerInfo(request, id):
    players = Player.objects.get(id=id)
    return render(request, 'mtg/player_info.html', {'Player':players})

def PlayerUpdate(request, id):
    players = Player.objects.get(id=id)
    if request.method == 'POST':
        p_form = PlayerUpdateForm(request.POST,request.FILES, instance=players)

        if p_form.is_valid():
            p_form.save()
            return redirect('players')

    else:
        form = PlayerUpdateForm(instance=players)
        return render(request, 'mtg/player-edit.html', {'p_form':form})



def PlayerCreate(request):
    if request.method == 'POST':
        p_form = PlayerUpdateForm(request.POST)

        if p_form.is_valid():
            p_form.save()
            return redirect('players')

    else:
        form = PlayerUpdateForm()
        return render(request, 'mtg/player-create.html', {'p_form':form})

def PlayerDelete(request, id):
    obj = get_object_or_404(Player, id = id) 
  
  
    if request.method =="POST": 
        obj.is_active=False
        obj.save()
        return redirect('players')
    
    return render(request, "mtg/player_delete.html") 

def MatchView(request):
    matches = Match.objects.all()
    return render(request, 'mtg/matches.html', {'matches':matches})

def MatchCreate(request):
    if request.method == 'POST':
        m_form = MatchCreateForm(request.POST)

        if m_form.is_valid():
            player_1 = m_form.cleaned_data['player_1']
            player_2 = m_form.cleaned_data['player_2']
            if player_1 == player_2:
                return render(request, 'mtg/match-create.html', {'m_form':m_form})


            m_form.save()
            return redirect('matches')

    else:
        form = MatchCreateForm()
        return render(request, 'mtg/match-create.html', {'m_form':form})


def MatchDelete(request, id):
    obj = get_object_or_404(Match, id = id) 
  
  
    if request.method =="POST": 
        obj.is_active=False
        obj.save()
        return redirect('matches')
    
    return render(request, "mtg/match-delete.html") 

def MatchUpdate(request, id):
    match = Match.objects.get(id=id)
    if request.method == 'POST':
        m_form = MatchCreateForm(request.POST, instance=match)

        if m_form.is_valid():
            m_form.save()
            return redirect('matches')

    else:
        matches = Match.objects.all()
        status = match.status_2
        if status == "finished":
            return render(request, 'mtg/matches.html', {'matches':matches})
        form = MatchCreateForm(instance=match)
        return render(request, 'mtg/match-edit.html', {'m_form':form})


def TurnView(request, id):
    turns = Turn.objects.filter(match=id)
    return render(request, 'mtg/turns.html', {'turns':turns})


def TurnCreate(request):
    if request.method == 'POST':
        t_form = TurnCreateForm(request.POST)

        if t_form.is_valid():
            t_form.save()
            return redirect('matches')

    else:
        form = TurnCreateForm()
        return render(request, 'mtg/turn-create.html', {'t_form':form})


def TurnUpdate(request, id):
    turn = Turn.objects.get(id=id)
    if request.method == 'POST':
        t_form = TurnCreateForm(request.POST, instance=turn)

        if t_form.is_valid():
            t_form.save()
            return redirect('matches')

    else:
        form = TurnCreateForm(instance=turn)
        return render(request, 'mtg/turn-edit.html', {'t_form':form})
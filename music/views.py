from django.shortcuts import render, get_object_or_404
from .models import Albumn,Song
# Create your views here.

def index(request):
    all_albumns = Albumn.objects.all()
    context = {'all_albumns':all_albumns,}
    return render(request,'music/index.html',context)

def detail(request, album_id):
    # album = Albumm.objects.get(pk=album_id)
    album = get_object_or_404(Albumn, pk=album_id)
    #print(album)
    return render(request,'music/detail.html',{'album':album})

def favourite(request, album_id):
    album = get_object_or_404(Albumn, pk=album_id)
    #print(album_id)
    #print(album)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
        #print(selected_song)
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album':album,
            'error_message':'You did not select a valid song'})
    else:
        selected_song.is_favourite = True
        selected_song.save()
        #print(selected_song.is_favourite)
        return render(request,'music/detail.html',{'album':album})
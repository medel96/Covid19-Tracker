from django.shortcuts import render,redirect,render_to_response
from .forms import UtiForm
from .models import Sie_Utilisateur
import folium
import geocoder
from folium.plugins import Draw, LocateControl

# Create your views here. Es donde ponemos la logica de nuetsra app, toma info del model y pasa a una view

def uti_list(request):
    sie_utilisateur = Sie_Utilisateur.objects.filter()

    map = folium.Map(location=[33.6, -7.63], zoom_start=5,tiles='OpenStreetMap')

    for i in sie_utilisateur:
        lat_log_many = geocoder.osm(i.UTI_ADRESSE)
        folium.Marker(
            location = lat_log_many.latlng ,
            popup = ('<strong>Created by :</strong>: ' + str(i.UTI_NOM).capitalize() + '<strong>  </strong>: '+ str(i.UTI_PRENOM).capitalize() + '<br>' + '<strong>Nmber of cases</strong>: ' + str(i.UTI_NUMBER) + '<br>')
        ).add_to(map)

    draw = Draw()
    location = LocateControl()
    draw.add_to(map)
    location.add_to(map)
    folium.LayerControl().add_to(map)
    iframe = map._repr_html_();

    return render(request, 'info/uti_list.html', {'sie_utilisateur':sie_utilisateur, 'iframe':iframe})


def uti_new(request):
    if request.method == 'POST':
        form = UtiForm(request.POST)
        if form.is_valid():
            sie_utilisateur = form.save(commit=False)
            sie_utilisateur.UTI_SUPPRIME = False
            sie_utilisateur.save()
           # return redirect('/uti_new', pk=sie_utilisateur.pk)

            return redirect('/uti_list', pk=sie_utilisateur.pk)
    else:
        form = UtiForm()
    return render(request, 'info/formulaire.html', {'form':form})
# commit = False nos procura un objeto modelo , pero puedo aumentar datos y guardarlos

# Ayax que busca los utilisadores , es como un filtro
def chercher(request):
    if request.method == "POST":
        mot = request.POST['mot']
        if mot == "":
            sie_utilisateur = Sie_Utilisateur.objects.filter()
        else:
            sie_utilisateur = Sie_Utilisateur.objects.filter(UTI_NOM__contains=mot)

    return render_to_response('info/liste.html',{'sie_utilisateur' : sie_utilisateur })

from django.shortcuts import render
from django.utils import timezone
from .models import Contato


"""
from .models import Post - chamada realizada para post_list html 
O ponto depois de from significa o diretório atual ou o aplicativo atual. Como views.py e models.py
def post_list chama html no lugar de url 127.0.0.1:8000
 Create your views here.

 """

def post_list(request):

	posts = Contato.objects.get(contato_id=1) 
  
	return render(request, 'contato/post_list.html', {'posts': posts}) 



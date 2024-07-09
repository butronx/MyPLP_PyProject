from django.shortcuts import render
import uuid

# Create your views here (bixapp/views).
def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:6]
        new_url = Url(link=link,uuid=uid)
        new_url.save()
        return HttpResponse(uid)
    
def go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect('https://'+url_details.link)

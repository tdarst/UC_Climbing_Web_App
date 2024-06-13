from django.shortcuts import render
from authuser.models import User

# Create your views here.
def rockfall(request):
    username = request.user.username
    user = User.objects.get(username=username)
    context = {
        'user': user
    }
    return render(request, 'rockfall_templates/rockfall_template.html')
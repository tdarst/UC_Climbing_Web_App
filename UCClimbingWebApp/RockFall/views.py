from django.shortcuts import render
from authuser.models import User, Profile
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def rockfall(request):
    if request.user.is_authenticated:
        username = request.user.username
        user = User.objects.get(username=username)
        context = {
            'user': user
        }
    return render(request, 'rockfall_templates/rockfall_template.html')

@csrf_exempt
def update_score(request):
    username = request.user.username
    user = User.objects.get(username=username)
    if request.method == "POST":
        score = request.POST.get('score', 0)
        user.profile.score = score
        user.profile.save()
        return JsonResponse({'status': 'success', 'score':user.profile.score})
    return JsonResponse({'status': 'error'}, status=400)
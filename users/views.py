from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from accounts.models import Profile

# Create your views here.
def mypage(request, id):
    profile_user = get_object_or_404(User, pk=id)
    profile = get_object_or_404(Profile, user=profile_user)

    context = {
        'profile_user': profile_user,
        'profile': profile,
    }

    return render(request, 'users/mypage.html', context)
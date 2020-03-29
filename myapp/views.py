from django.shortcuts import render,redirect
from myapp.forms import PostForm, NewForm
from django.http import JsonResponse
from myapp.models import user, activity_periods
from myapp.serializers import userSerializer,activity_periodsSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


def send_json(request):

    data = [{
			"id": "W012A3CDE",
			"real_name": "Egon Spengler",
			"tz": "America/Los_Angeles",
			"activity_periods": [{
					"start_time": "Feb 1 2020  1:33PM",
					"end_time": "Feb 1 2020 1:54PM"
				},
				{
					"start_time": "Mar 1 2020  11:11AM",
					"end_time": "Mar 1 2020 2:00PM"
				},
				{
					"start_time": "Mar 16 2020  5:33PM",
					"end_time": "Mar 16 2020 8:02PM"
				}
			]
		},
		{
			"id": "W07QCRPA4",
			"real_name": "Glinda Southgood",
			"tz": "Asia/Kolkata",
			"activity_periods": [{
					"start_time": "Feb 1 2020  1:33PM",
					"end_time": "Feb 1 2020 1:54PM"
				},
				{
					"start_time": "Mar 1 2020  11:11AM",
					"end_time": "Mar 1 2020 2:00PM"
				},
				{
					"start_time": "Mar 16 2020  5:33PM",
					"end_time": "Mar 16 2020 8:02PM"
				}
			]
		}
	]


    return JsonResponse(data, safe=False)

def index(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form=PostForm()
	return render(request,'home.html',{'form':form})
    
def show(request):
    if request.method == "POST":
        form = NewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=NewForm()
    return render(request,'showhome.html',{'form':form})
    
class userViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = userSerializer

class activity_periodsViewSet(viewsets.ModelViewSet):
    queryset = activity_periods.objects.all()
    serializer_class = activity_periodsSerializer
    

class UserCountView(APIView):
    """
    A view that returns the count of active users in JSON.
    """
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        user_count = User.objects.filter(active=True).count()
        content = {'user_count': user_count}
        return Response(content)
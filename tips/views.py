from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
import json

from .models import Series, Tip

def sort_resources(request):
	if request.method == 'POST':
		tipTitle = request.POST.get('tip', None)
		tip = get_object_or_404(Tip, title=tipTitle)
		tipID = tip.pk

		resources = {}
		currentResources = tip.resources.replace(', ', ' ')
		resource = []
		previousIndex = 0
		for index in range(0, len(currentResources)):
			char = currentResources[index]
			if " " == char:
				resource.append(currentResources[previousIndex:index])
				previousIndex = index + 1
			elif index == len(currentResources) - 1:
				resource.append(currentResources[previousIndex:])

		for i in range(0, len(resource)):
			resources[i] = resource[i]

		ctx = { 'resources': resources, 'id': tipID }

		return HttpResponse(json.dumps(ctx), content_type='application/json')
	else:
		return HttpResponse("No Data.")

def like(request):
	if request.method == 'POST':
		tipID = request.POST.get('id', None)
		tip = get_object_or_404(Tip, pk=tipID)
		tip.likes += 1
		tip.save()

		ctx  = {'likes': tip.likes, 'id': tipID}
		return HttpResponse(json.dumps(ctx), content_type='application/json')
	else:
		return HttpResponse("No Data.")

def dislike(request):
	if request.method == 'POST':
		tipID = request.POST.get('id', None)
		tip = get_object_or_404(Tip, pk=tipID)
		tip.dislikes += 1
		tip.save()

		ctx  = {'dislikes': tip.dislikes, 'id': tipID}
		return HttpResponse(json.dumps(ctx), content_type='application/json')
	else:
		return HttpResponse("No Data.")

# Create your views here.
def all_series_list(request):
	series = Series.objects.all()
	return render(request, 'tips/series_list.html', { 'series': series })

def all_tip_list(request):
	tips = Tip.objects.all().order_by('-pub_date')
	series_length = len(tips)
	return render(request, 'tips/tip_list.html', { 'tips': tips, 'series_length': series_length })

def all_tips_in_series(request, pk):
	series = get_object_or_404(Series, pk=pk)
	tips = Tip.objects.filter(series=series).order_by('-pub_date')
	series_length = len(tips)
	context = {
		'series': series,
		'tips': tips,
		'series_length': series_length
	}
	return render(request, 'tips/all_tips_in_series.html', context)
from django.shortcuts import render 

from . import util


def index(request):
	return render(request, "encyclipedia/index.html",{
		"entries": util.list_entries()
		})
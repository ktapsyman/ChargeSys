from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Receipt
# Create your views here.
def index( request ):
#	LatestQList = Question.objects.order_by('-create_date')[:5]
#	output = ', '.join( [ q.question_text for q in LatestQList ] )
#	template = loader.get_template( 'HelloDJ/index.html' )
#	context = {
#		'List': LatestQList,
#	}
	ShoppingRecords = Receipt.objects.all()
	TotalCost = 0
	if( ShoppingRecords and 0 != len(ShoppingRecords)):
		for items in ShoppingRecords :
			TotalCost += items.TotalCost
		print TotalCost
	context = {
		'List' : ShoppingRecords,
		'TotalCost' : TotalCost,
	}
	template = loader.get_template( 'HelloDJ/index.html' )
	print ','.join( [ q.ItemName for q in ShoppingRecords ] )
	return HttpResponse(template.render(context, request))



def Greeting( request, name ):
	return HttpResponse( "Hello %s" % name )

def TestPostWithJson(request):
	print "IN"
	TestDataPack = request.POST.getlist('TestData[]')
	print TestDataPack
	for data in TestDataPack:
		print data
	return JsonResponse({'Result':100})

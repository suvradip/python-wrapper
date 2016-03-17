from django.shortcuts import render
from django.http import HttpResponse
from fcWrapper import FusionCharts


# Create your views here.
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def demo(request):
	column2d = FusionCharts("column2d", 
			"ex1" , 
			"600", 
			"400", 
			"chart-1", 
			"json", 
			"""{  
			   "chart":
			   {  
				  "caption":"Harry\'s SuperMart",
				  "subCaption":"Top 5 stores in last month by revenue",
				  "numberPrefix":"$",
				  "theme":"ocean"
			   },
			   "data":
			   [  
				  {  
					 "label":"Bakersfield Central",
					 "value":"880000"
				  },
				  {  
					 "label":"Garden Groove harbour",
					 "value":"730000"
				  },
				  {  
					 "label":"Los Angeles Topanga",
					 "value":"590000"
				  },
				  {  
					 "label":"Compton-Rancho Dom",
					 "value":"520000"
				  },
				  {  
					 "label":"Daly City Serramonte",
					 "value":"330000"
				  }
			   ]
		}""")
 	return  render(request, 'index.html', {'output' : column2d.render()})
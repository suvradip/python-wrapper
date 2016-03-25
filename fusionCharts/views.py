from django.shortcuts import render
from django.http import HttpResponse
from lib.fusioncharts import FusionCharts
from models import *
# Create your views here.

def demo(request):
	column2d = FusionCharts("column2d", "ex1" , "600", "400", "chart-1", "json", 
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

def event(request):
	column2d = FusionCharts("column2d", "ex1" , "600", "400", "chart-1", "json", 
			"""{  
			   "chart": {  
				  "caption":"Harry\'s SuperMart",
				  "subCaption":"Top 5 stores in last month by revenue",
				  "numberPrefix":"$",
				  "theme":"ocean"
			   },
			   "data": [  
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
		},
            "events": {
                "dataplotRollOver": function (eventObj, dataObj) {
                alert("chart rendered.");
            }
        }""")
 	return  render(request, 'index.html', {'output' : column2d.render()}) 	

def jsonurl(request):
	area2d = FusionCharts("area2d", "ex1" , "600", "400", "chart-1", "jsonurl","http://127.0.0.1:8000/static/data/data.json")
	return render(request, 'index.html', {'output': area2d.render()})

def xmlurl(request):
	bar2d = FusionCharts("bar2d", "ex1" , "600", "400", "chart-1", "xmlurl","http://127.0.0.1:8000/static/data/data.xml")
	return render(request, 'index.html', {'output': bar2d.render()}) 		 



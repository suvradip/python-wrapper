from django.shortcuts import render
from django.http import HttpResponse
from lib.fusioncharts import FusionCharts

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

def xml(request):
	column2d = FusionCharts("column2d", "ex1" , "600", "400", "chart-1", "xml", 
			"""<chart caption="Monthly revenue for last year" subcaption="Harry&#39;s SuperMart" xaxisname="Month" yaxisname="Revenues (In USD)" numberprefix="$" palettecolors="#0075c2" bgcolor="#ffffff" borderalpha="20" canvasborderalpha="0" useplotgradientcolor="0" plotborderalpha="10" placevaluesinside="1" rotatevalues="1" valuefontcolor="#ffffff" showxaxisline="1" xaxislinecolor="#999999" divlinecolor="#999999" divlinedashed="1" showalternatehgridcolor="0" subcaptionfontbold="0" subcaptionfontsize="14">
			    <set label="Jan" value="420000" />
			    <set label="Feb" value="810000" />
			    <set label="Mar" value="720000" />
			    <set label="Apr" value="550000" />
			    <set label="May" value="910000" />
			    <set label="Jun" value="510000" />
			    <set label="Jul" value="680000" />
			    <set label="Aug" value="620000" />
			    <set label="Sep" value="610000" />
			    <set label="Oct" value="490000" />
			    <set label="Nov" value="900000" />
			    <set label="Dec" value="730000" />
			    <trendlines>
			        <line startvalue="700000" color="#1aaf5d" valueonright="1" displayvalue="Monthly Target" />
			    </trendlines>
			</chart>""")
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

def pythonData(request):
	dataSource = {}
	dataSource['chart'] = { 
				"caption":"Harry\'s SuperMart",
		  		"subCaption":"Top 5 stores in last month by revenue",
		  		"numberPrefix":"$",
		  		}

	dataSource['data']	 = [  
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
	column2d = FusionCharts("column2d", "ex1" , "600", "400", "chart-1", "json", dataSource)
	return render(request, 'index.html', {'output': column2d.render()}) 
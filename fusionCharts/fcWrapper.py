from django.http import HttpResponse
import json

class FusionCharts:
   'Common base class for FC'

   constructorOptions = {}
   constructorTemplate = """
     <script type="text/javascript">
         FusionCharts.ready(function () {
             new FusionCharts(__constructorOptions__);
         });
     </script>"""
   renderTemplate = """
     <script type="text/javascript">
         FusionCharts.ready(function () {
             FusionCharts("__chartId__").render();
         });
     </script>
   """

   def __init__(self, type, id, width, height, renderAt, dataFormat, dataSource):    
      FusionCharts.constructorOptions['type'] = type
      FusionCharts.constructorOptions['id'] = id
      FusionCharts.constructorOptions['width'] = width
      FusionCharts.constructorOptions['height'] = height
      FusionCharts.constructorOptions['renderAt'] = renderAt
      FusionCharts.constructorOptions['dataFormat'] = dataFormat
      dataSource = json.loads(dataSource)
      FusionCharts.constructorOptions['dataSource'] = dataSource
  
   def render(self):
    prepJson = json.dumps(FusionCharts.constructorOptions)
    prepJson = FusionCharts.constructorTemplate.replace('__constructorOptions__', prepJson)
    prepJson = prepJson + FusionCharts.renderTemplate.replace('__chartId__', FusionCharts.constructorOptions['id'])
    return prepJson
 
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
# Create your views here.
def index( request ):

#	import pdb; pdb.set_trace();
#	return HttpResponse("""{ "ResponseCode": "Success"}""", content_type="application/json; charset=UTF-8")
	return render_to_response('index.html')

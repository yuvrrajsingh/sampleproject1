from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
globalcount = dict()
# create your views

def index(request):
    languages = ['Java', 'Python', 'C', 'C++' ,'Perl', 'Javascript', 'Kotlin', 'Ruby', 'DotNet', 'PHP', 'Html', 'Swift', 'SQL', 'Flutter', 'Objective-C', 'Go', 'VisualBasic', 'MATLAB']
    return render(request, 'votingapp/index.html')

def getquery(request):
    q = request.GET['languages']

    if q in globalcount:
        globalcount[q]+=1
    else:
        globalcount[q]=1

    # sorting the data in stored in globalcount dictionary
    sorted_data = {}
    for val in sorted(globalcount.values(), reverse=True):
        for key in globalcount.keys():
            if globalcount[key] == val:
                sorted_data[key] = val


    mydict = {
        'data': sorted_data
    }

    # return JsonResponse(globalcount)
    return render(request, 'votingapp/index.html', context=mydict)
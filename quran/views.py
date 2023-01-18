from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
import json

es = Elasticsearch(['https://cca77a3d5f9448a0bd133b478b6cc25b.uksouth.azure.elastic-cloud.com:9243'], http_auth=('elastic', 'ZECx5bK7cJBb90adVKxj2bYB'))
print(es)

# Create your views here.
@csrf_exempt
def search_(request):
    print("INSIDE SEARCH VIEW",request.body.decode('utf-8'))

        #word = request.POST.get('word')
    word = json.loads(request.body.decode('utf-8'))
    print("word = json.loads(request.body.decode('utf-8'))")
    print(type(word))
    print("REQUEST PARAMTERES : " ,word)
    
    res = {} 
     
    if word:
        search_query = Search(using=es,index='quranic_rootwords').query("match",word=word)  
        res = search_query.execute()
        print("RESPONSE TYPE : ",type(res))
    
    #print("if word:search_query = Search(using=es,index='quranic_rootwords').query()")
    
    objs = []

    
    print("RESPONSE : ",res)
    print("ELASTIC SEARCH RESPONSE LENGTH : " , len(res))
    for hit in res:
        parts_of_speech = ' '.join(hit.parts_of_speech)

        es_response = {'word':hit.word,
        'surat_no':hit.surah_no,
        'description':hit.decription,
        'ayat_no':hit.ayat_no,
        'surat_name':hit.surah_name,
        'parts_of_speech':parts_of_speech,
        'root':hit.root,
        'word':hit.word,
        'ayat':hit.ayat}
        objs.append(es_response)
       
    #print(objs)

    parsed = json.dumps(objs, ensure_ascii=False)

    print("PARSED :" ,parsed)
    
    return HttpResponse(parsed)








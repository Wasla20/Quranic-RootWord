from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search


#es = Elasticsearch(ES_USR = "elastic",ES_PWD = "ZECx5bK7cJBb90adVKxj2bYB",ES_SRV = "https://cca77a3d5f9448a0bd133b478b6cc25b.uksouth.azure.elastic-cloud.com:9243",ES_IDX = "quranic_rootwords")
#es = Elasticsearch(['https://cca77a3d5f9448a0bd133b478b6cc25b.uksouth.azure.elastic-cloud.com:9243'], http_auth=('elastic', 'ZECx5bK7cJBb90adVKxj2bYB'))

#print(es)

def searchView(request):
    if 'word' in request.GET:
        word = request.GET['word']

    es = Elasticsearch(['https://cca77a3d5f9448a0bd133b478b6cc25b.uksouth.azure.elastic-cloud.com:9243'], http_auth=('elastic', 'ZECx5bK7cJBb90adVKxj2bYB'))
    print(es)

    search_query = Search(using=es,index='quranic_rootwords').query("match",word=word)  
    response = search_query.execute()

    print(type(response))

    for hit in response:
        print("Score : ", hit.meta.score , hit.word)
        print("Surah number : ",hit.surah_no)

    return 








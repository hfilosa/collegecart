import urllib2
import json
import random

#Returns a college with that position n, some schools don't have tuition in the database
#Returned as a dictionary with 'name' and 'cost' keys
#n goes up to 3,586
def get_college(n):
    key="umxI9TYizENUIsLg0YaQdJSd8b0AOyxhKOs8iVr5"
    page_num=n/20
    n=n-(20*(n/20))
    url = "https://api.data.gov/ed/collegescorecard/v1/schools?&api_key=%s&page=%d"%(key,page_num)
    request = urllib2.urlopen(url)
    result = request.read()
    r = json.loads(result)
    return {'name':r['results'][n]['school']['name'],'cost':r['results'][n]['2013']['cost']['tuition']}

#Return a random college
def get_random_college():
    done=False
    while (done!=True):
        random.seed();
        r=random.randrange(0,3587)
        college=get_college(r)
        if (college['cost']['in_state']!='None' or college['cost']['program_year']!="None" or college['cost']['out_of_state']!="None"):
            return college

#Returns a basket of amazon products. Add quantity of product to product dictionary
#Last item in basket array is remainder of tutition
def get_basket(tuiton):
    basket=[]
    while (tuition>30):
        product=get_random_product
        budget=tuiton/2
        while (product.price>budget);
            product=get_random_product
        product['quantity']=budget/product.price
        tuiton-=(budget-(budget%product.price))
        basket.append(product)
    basket.append(tuiton)
    return basket

#When given a word, searches amazon and returns the first hit
#Returns product name and cost
def get_goods(search):
    return null

print get_random_college()

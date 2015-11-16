import urllib2
import json
import random
from pyquery import PyQuery as pq
from amazon.api import AmazonAPI

Amazon = AmazonAPI('AKIAJUNVP6BHD3AFMXSQ', 'KQNrDP1ij/4RtEJIp/eFXogV48qha5YO3yHNjMHz', 'chrgra-20')

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

    #all the possible avalible costs
    cost_dict=r['results'][n]['2013']['cost']['tuition']
    #Narrow the cost down to one value
    if (cost_dict['out_of_state']=='None'):
        if (cost_dict['in_state']=='None'):
            if (ost_dict['program_year']=='None'):
                cost=0
            cost=cost_dict['program_year']
        else:
            cost=cost_dict['in_state']
    else:
        cost=cost_dict['out_of_state']
    
    return {'name':r['results'][n]['school']['name'],'cost':cost}

#Return a random college
def get_random_college():
    print("Starting college selection")
    done=False
    random.seed()
    while (done!=True):
        print("looping...")
        r=random.randrange(0,3587)
        college=get_college(r)
        if (college['cost']!=None):
            print("College selected")
            print(college)
            return college

#Returns a basket of amazon products. Add quantity of product to product dictionary
#Last item in basket array is remainder of tutition
def get_basket(tuition):
    basket=[]
    while (tuition>30):
        product={}
        product=get_random_product()
        print(product)
        budget=tuition/2
        while (product['price']>budget or product['price']<0.01 ):
            product=get_random_product()
        product['quantity']=(int)(budget/product['price'])
        tuition-=(budget-(budget%product['price']))
        basket.append(product)
    basket.append(tuition)
    return basket

def get_random_product():
    product = {
        'name': '',
        'link': '',
        'price': 0,
        'image': ''
    }
    url="http://www.randomamazonproduct.com"

    d = pq(url=url, headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
        'cookie': '__cfduid=d5fccb67ae1087311327fbfaf2f1644401447515945'
    })

    product['link'] = d(".outlink").attr('href')
    product['name'] = d(".amazon-title").text()
    product['image'] = d(".amazon-image").attr('src')

    pid = product['link'].split('/dp/')[1].split('%3F')[0]
    product['price'] = Amazon.lookup(ItemId=pid).price_and_currency[0]

    return product

"""
basket=get_basket(1000)
i=0
while (i<basket.size):
    print(basket[i])
    i+=1
"""

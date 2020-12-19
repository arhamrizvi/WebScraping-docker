import requests
import json
import pprint

def getResponse(url):
    url = url
    hdr = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}

    response = requests.get(url, headers=hdr)
    return response


url = 'https://www.zalora.com.my/_c/v1/desktop/list_catalog_full?url=%2Fwomen%2Fshoes&sort=popularity&dir=desc&category_id=4&occasion=Casual&brand=87&gender=women&segment=women&special_price=false&all_products=false&new_products=false&top_sellers=false&catalogtype=Main&lang=en&is_brunei=false&sort_formula=sum(product(0.01%2Cscore_simple_availability)%2Cproduct(0.0%2Cscore_novelty)%2Cproduct(0.99%2Cscore_product_boost)%2Cproduct(0.0%2Cscore_random)%2Cproduct(1.0%2Cscore_personalization))&search_suggest=false&enable_visual_sort=true&enable_filter_ads=true&compact_catalog_desktop=false&name_search=false&solr7_support=true&pick_for_you=false&learn_to_sort_catalog=false&is_multiple_source=true'

response = getResponse(url)

json_result = json.loads(response.text)

print(json.dumps(json_result)) # , indent=4

numItems = response.json()['response']['numFound']
print(numItems)


url = 'https://www.zalora.com.my/_c/v1/desktop/list_catalog_full?url=%2Fwomen%2Fshoes&sort=popularity&dir=desc&offset=0&limit=' + str(
    numItems) + '&category_id=4&occasion=Casual&brand=87&gender=women&segment=women&special_price=false&all_products=false&new_products=false&top_sellers=false&catalogtype=Main&lang=en&is_brunei=false&sort_formula=sum(product(0.01%2Cscore_simple_availability)%2Cproduct(0.0%2Cscore_novelty)%2Cproduct(0.99%2Cscore_product_boost)%2Cproduct(0.0%2Cscore_random)%2Cproduct(1.0%2Cscore_personalization))&search_suggest=false&enable_visual_sort=true&enable_filter_ads=true&compact_catalog_desktop=false&name_search=false&solr7_support=true&pick_for_you=false&learn_to_sort_catalog=false&is_multiple_source=true'

response = getResponse(url)

# Brand, Actual price, Discounted price, link to the image of the product
sku = []
name = []
brand = []
actual_price = []
discounted_price = []
img_link = []
# data['output'] = []
data = []

for a in response.json()['response']['docs']:
    data.append({
        "sku": a['meta']['sku'],
        "name": a['meta']['name'],
        "brand": a['meta']['brand'],
        "price": a['meta']['price'],
        "discountPrice": a['meta']['special_price'],
        "imgLink": a['image']
    })
with open('data.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)




import json
import eel

# Load the JSON data from the file
with open('all_items.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Define a function that returns the items as a list of dictionaries
@eel.expose
def get_items(rate, volume, price_uah, price_uah_max, price_rub):
    items = []
    for item in data.values():
        rate_value = item.get('rate', 0)  # Use 0 as the default value if 'rate' is not present
        volume_value = item.get('tm_volume', 0)  # Use 0 as the default value if 'tm_volume' is not present
        price_uah_value = item.get('sale_price_text_uah', 0)
        price_rub_value = item.get('sale_price_text_rub', 0)
        name = item['market_hash_name']
        
        if rate_value is not None and float(rate_value) > float(rate) and volume_value is not None and int(volume_value) > int(volume) and price_uah_value is not None and float(price_uah) < float(price_uah_value) < float(price_uah_max) and price_rub_value is not None and float(price_rub_value) > float(price_rub):
            items.append({'name': name, 'price': price_uah_value, 'rate': rate_value, 'tm_volume': volume_value, 'rubprice': price_rub_value})
    
    return items

# Start the Eel app
eel.init('front')
eel.start('index.html', size=(1280, 800))
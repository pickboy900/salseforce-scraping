from csv import DictWriter
import time
import os.path
import urllib.request
from selenium import webdriver
from random import randrange
from selenium.webdriver import ChromeOptions
options = ChromeOptions()
options.add_extension('block_image.crx')
chrome = webdriver.Chrome(options=options)
rows = ['sku', 'store_view_code', 'attribute_set_code', 'product_type', 'categories', 'product_websites', 'name', 'description', 'short_description', 'weight', 'product_online', 'tax_class_name', 'visibility', 'price', 'special_price', 'special_price_from_date', 'special_price_to_date', 'url_key', 'meta_title', 'meta_keywords', 'meta_description', 'base_image', 'base_image_label', 'small_image', 'small_image_label', 'thumbnail_image', 'thumbnail_image_label', 'swatch_image', 'swatch_image_label', 'created_at', 'updated_at', 'new_from_date', 'new_to_date', 'display_product_options_in', 'map_price', 'msrp_price', 'map_enabled', 'gift_message_available', 'custom_design', 'custom_design_from', 'custom_design_to', 'custom_layout_update', 'page_layout', 'product_options_container', 'msrp_display_actual_price_type', 'country_of_manufacture', 'additional_attributes', 'qty', 'out_of_stock_qty', 'use_config_min_qty', 'is_qty_decimal', 'allow_backorders', 'use_config_backorders', 'min_cart_qty', 'use_config_min_sale_qty', 'max_cart_qty', 'use_config_max_sale_qty', 'is_in_stock', 'notify_on_stock_below', 'use_config_notify_stock_qty', 'manage_stock', 'use_config_manage_stock', 'use_config_qty_increments', 'qty_increments', 'use_config_enable_qty_inc', 'enable_qty_increments', 'is_decimal_divided', 'website_id', 'related_skus', 'related_position', 'crosssell_skus', 'crosssell_position', 'upsell_skus', 'upsell_position', 'additional_images', 'additional_image_labels', 'hide_from_product_page', 'custom_options', 'bundle_price_type', 'bundle_sku_type', 'bundle_price_view', 'bundle_weight_type', 'bundle_values', 'bundle_shipment_type', 'associated_skus', 'configurable_variations', 'configurable_variation_labels', 'base_label', 'small_label', 'swatch_label', 'thumbnail_label']
url = 'https://www.discountbathroomvanities.com/Chans+Furniture-CTO.html'
chrome.get(url)
brand = 'Chans Furniture'
try:
    chrome.find_element_by_css_selector("a[title='close']").click()
except:
    pass
expected_results = 334
# To get the full results we have to scroll until the
#     Result count is 42 Then we will go pagination
all_links = set()
all_imges = []


with open('data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = DictWriter(file, fieldnames=rows)
    writer.writeheader()
    nx = 2
    while True:
        links = []
        last_height = chrome.execute_script("return document.body.scrollHeight")

        while True:
            rets = chrome.execute_script("""
            links = $('h5 a.product-info-link');
            all_links = [];
            for (i=0;i<links.length;i++){
                link = links[i];
                if (all_links.indexOf(link.href < 0))
                    all_links.push(link.href);
            }
            return all_links;
            """)
            # assert type(rets) == list
            for ret in rets:
                if ret not in all_links:
                    links.append(ret)
                    all_links.add(ret)
            chrome.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            randint = randrange(1, 5)
            time.sleep(randint)
            # Calculate new scroll height and compare with last scroll height
            new_height = chrome.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        for link in links:
            data = {'sku': '', 'store_view_code': '', 'attribute_set_code': 'Default', 'product_type': 'simple',
                    'categories': 'Default Category/Brands;Default Category/Brands/{}'.format(brand),
                    'product_websites': 'base', 'name': '', 'description': '', 'short_description': '', 'weight': '',
                    'product_online': '1', 'tax_class_name': 'Taxable Goods', 'visibility': 'Catalog, Search',
                    'price': '',
                    'special_price': '', 'special_price_from_date': '', 'special_price_to_date': '', 'url_key': '',
                    'meta_title': '',
                    'meta_keywords': '', 'meta_description': '', 'base_image': '', 'base_image_label': 'TY-650PW_1.jpg',
                    'small_image': '', 'small_image_label': 'TY-650PW_1.jpg', 'thumbnail_image': '',
                    'thumbnail_image_label': 'TY-650PW_1.jpg', 'swatch_image': '',
                    'swatch_image_label': 'TY-650PW_1.jpg',
                    'created_at': '10/20/19, 4:50 AM', 'updated_at': '10/20/19, 4:50 AM', 'new_from_date': '10/20/2019',
                    'new_to_date': '10/21/2019', 'display_product_options_in': 'Block after Info Column',
                    'map_price': '',
                    'msrp_price': '', 'map_enabled': '', 'gift_message_available': 'Use config', 'custom_design': '',
                    'custom_design_from': '', 'custom_design_to': '', 'custom_layout_update': '',
                    'page_layout': '3 columns',
                    'product_options_container': '', 'msrp_display_actual_price_type': 'Use config',
                    'country_of_manufacture': '',
                    'additional_attributes': '', 'qty': '22', 'out_of_stock_qty': '0', 'use_config_min_qty': '1',
                    'is_qty_decimal': '0', 'allow_backorders': '0', 'use_config_backorders': '1', 'min_cart_qty': '1',
                    'use_config_min_sale_qty': '1', 'max_cart_qty': '10000', 'use_config_max_sale_qty': '1',
                    'is_in_stock': '1',
                    'notify_on_stock_below': '1', 'use_config_notify_stock_qty': '1', 'manage_stock': '1',
                    'use_config_manage_stock': '1', 'use_config_qty_increments': '1', 'qty_increments': '1',
                    'use_config_enable_qty_inc': '1', 'enable_qty_increments': '0', 'is_decimal_divided': '0',
                    'website_id': '0',
                    'related_skus': '', 'related_position': '', 'crosssell_skus': '', 'crosssell_position': '',
                    'upsell_skus': '',
                    'upsell_position': '', 'additional_images': '', 'additional_image_labels': '',
                    'hide_from_product_page': '',
                    'custom_options': '', 'bundle_price_type': '', 'bundle_sku_type': '', 'bundle_price_view': '',
                    'bundle_weight_type': '', 'bundle_values': '', 'bundle_shipment_type': '', 'associated_skus': '',
                    'configurable_variations': '', 'configurable_variation_labels': '', 'base_label': '',
                    'small_label': '',
                    'swatch_label': '', 'thumbnail_label': ''}

            chrome.get(link)
            try:
                data['sku'] = chrome.find_elements_by_css_selector('h1.product-name')[1].text.split()[2]
            except Exception as e:
                continue
            data['name'] = chrome.find_element_by_css_selector('h1.product-name').text
            data['url_key'] = data['name'].lower().replace(' ', '-')
            data['price'] = chrome.find_element_by_css_selector('span.price').text[1:]
            images = chrome.find_elements_by_css_selector('.owl-item img.lazy_load[data-big-img]')
            images_name = []
            for img in images:
                img_url = 'https://www.discountbathroomvanities.com' + img.get_attribute('data-big-img')
                all_imges.append(img_url)
                image_name = img_url.split('/')[-1]
                images_name.append(image_name)
            data['description'] = chrome.find_element_by_id("product-detail").text.replace('Description', '')
            data['additional_images'] = ';'.join(images_name)
            data['additional_attributes'] = "brand={};coming_soon=NO;model={};specifications={}".format(
                brand,
                data['sku'],
                chrome.find_element_by_class_name('specification').text
            )
            writer.writerow(data)
        if randint == 3:
            chrome.get('https://github.com/')
        chrome.get(url)
        chrome.execute_script('RequireToChangeProducts({})'.format(nx))
        if nx > (expected_results // 42) + 2:
            print('next page request', nx, (expected_results // 42) + 1)
            break
        nx += 1
print(len(all_links))
print(all_links)
chrome.close()
for url in all_imges:
    image_name = url.split('/')[-1]
    dir = os.path.abspath(os.getcwd())
    img_path = os.path.join(dir, 'images', image_name)
    if not os.path.exists(img_path):
        urllib.request.urlretrieve(url, img_path)


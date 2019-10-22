from csv import DictWriter
import time
import urllib.request
from selenium import webdriver
from selenium.webdriver import ChromeOptions
options = ChromeOptions()
options.add_extension('block_image.crx')
chrome = webdriver.Chrome(options=options)
rows = ['sku','store_view_code','attribute_set_code','product_type','categories','product_websites','name',
        'description','short_description','weight','product_online','tax_class_name','visibility','price',
        'special_price','special_price_from_date','special_price_to_date','url_key','meta_title','meta_keywords',
        'meta_description','base_image','base_image_label','small_image','small_image_label','thumbnail_image',
        'thumbnail_image_label','swatch_image','swatch_image_label','created_at','updated_at','new_from_date',
        'new_to_date','display_product_options_in','map_price','msrp_price','map_enabled','gift_message_available',
        'custom_design','custom_design_from','custom_design_to','custom_layout_update','page_layout',
        'product_options_container','msrp_display_actual_price_type','country_of_manufacture','additional_attributes',
        'qty','out_of_stock_qty','use_config_min_qty','is_qty_decimal','allow_backorders','use_config_backorders',
        'min_cart_qty','use_config_min_sale_qty','max_cart_qty','use_config_max_sale_qty','is_in_stock',
        'notify_on_stock_below','use_config_notify_stock_qty','manage_stock','use_config_manage_stock',
        'use_config_qty_increments','qty_increments','use_config_enable_qty_inc','enable_qty_increments',
        'is_decimal_divided','website_id','related_skus','related_position','crosssell_skus','crosssell_position',
        'upsell_skus','upsell_position','additional_images','additional_image_labels','hide_from_product_page',
        'custom_options','bundle_price_type','bundle_sku_type','bundle_price_view','bundle_weight_type','bundle_values',
        'bundle_shipment_type','associated_skus','configurable_variations','configurable_variation_labels']
chrome.get('https://www.discountbathroomvanities.com/bathroom-vanities-stufurhome-vc2495-12.html')
try:
    chrome.find_element_by_css_selector("a[title='close']").click()
except:
    pass
expected_results = 70
# To get the full results we have to scroll until the
#     Result count is 42 Then we will go pagination
all_links = {'https://www.discountbathroomvanities.com/Stufurhome-GM-2206-40ES-CR-Grand-Cheswick-40-Single-Sink-Bathroom-Vanity.-Carrara-Marble-Top-lwLWV94803526-6.html', 'https://www.discountbathroomvanities.com/Stufurhome-HD-6004-49-QZ-Erin-49-Modern-Single-Sink-Bathroom-Vanity-lwPROD14794.html', 'https://www.discountbathroomvanities.com/Stufurhome-TY-6262-59-QZ-Emily-59-Transitional-Double-Sink-Bathroom-Vanity-lwLWV295B19E4-E.html', 'https://www.discountbathroomvanities.com/Stufurhome-HD-6868-60-CR-Marla-60-Transitional-Double-Sink-Bathroom-Vanity-lwLWVA93E5C2A-E.html', 'https://www.discountbathroomvanities.com/Stufurhome-GM-6123-48-TR-Lotus-48-Traditional-Single-Sink-Bathroom-Vanity-lwGM-6123.html', 'https://www.discountbathroomvanities.com/Stufurhome-GM-6412-72GY-CR-Malibu-72-Transitional-Double-Sink-Bathroom-Vanity-in-Grey-lwPROD14795.html', 'https://www.discountbathroomvanities.com/Stufurhome-HD-7130G-48-CR-Newport-48-Transitional-Single-Sink-Bathroom-Vanity-in-Grey-lwLWVBD219A9A-9.html', 'https://www.discountbathroomvanities.com/Stufurhome-GM-5110-56-TR-Princeton-56-Antique-Single-Sink-Bathroom-Vanity-with-Travertine-Top-lwLWV93B87962-D.html', 'https://www.discountbathroomvanities.com/Stufurhome-GM-3211-62-TR-Catherine-62-Traditional-Double-Sink-Bathroom-Vanity-with-Travertine-Top-lwLWVD5D134F2-8.html', 'https://www.discountbathroomvanities.com/Stufurhome-HD-6004-31-QZ-Erin-31-Modern-Single-Sink-Bathroom-Vanity-lwPROD14813.html', 'https://www.discountbathroomvanities.com/Stufurhome-GM-6412-36GY-CR-Malibu-36-Transitional-Single-Sink-Bathroom-Vanity-In-Grey-lwPROD14792.html', 'https://www.discountbathroomvanities.com/Stufurhome-GM-6412-36ES-CR-Malibu-36-Modern-Espresso-Single-Sink-Bathroom-Vanity-lwLWV30D34704-B.html', 'https://www.discountbathroomvanities.com/Stufurhome-GM-5116-60-TR-Amelia-60-Antique-Double-Sink-Bathroom-Vanity-with-Travertine-Top-lwGM-5116-60-BB-1.html', 'https://www.discountbathroomvanities.com/Stufurhome-HD-7000G-72-CR-Cadence-72-Transitional-Double-Sink-Bathroom-Vanity-in-Grey-lwLWVD98777D6-9.html', 'https://www.discountbathroomvanities.com/Stufurhome-GM-Y01W-30.5-White-Single-Sink-Bathroom-Vanity-Laundry-Sink-lwLWV95B39448-E.html', 'https://www.discountbathroomvanities.com/Stufurhome-GM-6412-72ES-CR-Malibu-72-Transitional-Double-Sink-Bathroom-Vanity-in-Espresso-lwPROD14793.html', 'https://www.discountbathroomvanities.com/Stufurhome-GM-6412-48ES-CR-Malibu-48-Transitional-Espresso-Single-Sink-Bathroom-Vanity-lwLWV83C4D5BA-3.html', 'https://www.discountbathroomvanities.com/Stufurhome-GM-6412-36ES-CR-M35-Malibu-36-Transitional-Single-Sink-Bathroom-Vanity-in-Espresso-withMirror-lwPROD14790.html', 'https://www.discountbathroomvanities.com/Stufurhome-HD-7130G-36-CR-Newport-36-Transitional-Single-Sink-Bathroom-Vanity-in-Grey-lwLWV44118D62-3.html', 'https://www.discountbathroomvanities.com/Stufurhome-GM-5116-60-BB-Amelia-60-Antique-Double-Sink-Bathroom-Vanity-with-Baltic-Brown-Granite-Top-lwGM-5116-60-BB.html', 'https://www.discountbathroomvanities.com/Stufurhome-GM-6412-60GY-CR-M59-Malibu-60-Transitional-Double-Sink-Bathroom-Vanity-in-Grey-withMirror-lwPROD14815.html', 'https://www.discountbathroomvanities.com/Stufurhome-HD-6868-48-CR-Marla-48-Transitional-Single-Sink-Bathroom-Vanity-lwLWVE0E87896-C.html', 'https://www.discountbathroomvanities.com/Stufurhome-GM-6412-48PW-CR-M47-Malibu-48-Transitional-Single-Sink-Bathroom-Vanity-in-White-withMirror-lwPROD14802.html', 'https://www.discountbathroomvanities.com/Stufurhome-GM-6412-36GY-CR-M35-Malibu-36-Transitional-Single-Sink-Bathroom-Vanity-in-Grey-withMirror-lwPROD14791.html', 'https://www.discountbathroomvanities.com/Stufurhome-GM-6412-60GY-CR-Malibu-60-Transitional-Double-Sink-Bathroom-Vanity-in-Grey-lwPROD14784.html', 'https://www.discountbathroomvanities.com/Stufurhome-TY-650GY-Monte-25-Corner-Single-Sink-Bathroom-Vanity-in-Grey-lwPROD14812.html', 'https://www.discountbathroomvanities.com/Stufurhome-HD-7130W-72-CR-Newport-72-Transitional-Double-Sink-Bathroom-Vanity-in-White-lwLWV972F7FEC-0.html', 'https://www.discountbathroomvanities.com/Stufurhome-HD-6004-37-QZ-Erin-37-Modern-Single-Sink-Bathroom-Vanity-lwPROD14819.html', 'https://www.discountbathroomvanities.com/Stufurhome-GM-3323-60-TR-Saturn-60-Antique-Double-Sink-Vanity-with-Travertine-Top-lwGM-3323-60-BB-1.html', 'https://www.discountbathroomvanities.com/Stufurhome-GM-6412-72GY-CR-M71-Malibu-72-Transitional-Double-Sink-Bathroom-Vanity-in-Grey-withMirror-lwPROD14799.html', 'https://www.discountbathroomvanities.com/Stufurhome-HD-6868-72-CR-Marla-72-Transitional-Double-Sink-Bathroom-Vanity-lwLWVC724C95E-3.html', 'https://www.discountbathroomvanities.com/Stufurhome-GM-3323-60-BB-Saturn-60-Antique-Double-Sink-Vanity-with-Baltic-Brown-Granite-Top-lwGM-3323-60-BB.html', 'https://www.discountbathroomvanities.com/Stufurhome-TY-415GY-Hampton-27-Corner-Bathroom-Vanity-in-Grey-lwPROD14818.html', 'https://www.discountbathroomvanities.com/Stufurhome-GM-6412-48PW-CR-Malibu-48-White-Single-Sink-Bathroom-Vanity-lwLWVC720FEB7-E.html', 'https://www.discountbathroomvanities.com/Stufurhome-GM-6412-36PW-CR-Malibu-36-Transitional-White-Single-Sink-Bathroom-Vanity-lwLWV56492C26-8.html', 'https://www.discountbathroomvanities.com/Stufurhome-GM-5116-48-BB-Amelia-48-Traditional-Single-Sink-Bathroom-Vanity-with-Baltic-Brown-Top-lwLWV12FBEB2E-C.html', 'https://www.discountbathroomvanities.com/Stufurhome-TY-650PW-Monte-25-Corner-Single-Sink-Bathroom-Vanity-in-White-lwPROD14811.html', 'https://www.discountbathroomvanities.com/Stufurhome-HD-6868G-48-CR-Marla-48-Modern-Single-Sink-Bathroom-Vanity-in-Grey-withMirror-lwPROD14805.html', 'https://www.discountbathroomvanities.com/Stufurhome-GM-2206-40-BB-Grand-Cheswick-40-Traditional-Single-Sink-Bathroom-Vanity-lwGM-2206.html', 'https://www.discountbathroomvanities.com/Stufurhome-GM-5110-56-BB-Princeton-56-Antique-Single-Sink-Bathroom-Vanity-with-Baltic-Brown-Top-lwLWV3BCF164C-A.html', 'https://www.discountbathroomvanities.com/Stufurhome-GM-6119-36-TR-Alyssa-36-Traditional-Single-Sink-Bathroom-Vanity-lwGM-6119.html', 'https://www.discountbathroomvanities.com/Stufurhome-GM-6412-48GY-CR-M47-Malibu-48-Transitional-Single-Sink-Bathroom-Vanity-in-Grey-withMirror-lwPROD14820.html', 'https://www.discountbathroomvanities.com/Stufurhome-TY-6262-49-QZ-Emily-49-Transitional-Single-Sink-Bathroom-Vanity-lwLWV253B6835-4.html', 'https://www.discountbathroomvanities.com/Stufurhome-HD-6004-59-QZ-Erin-59-Transitional-Double-Sink-Bathroom-Vanity-in-White-lwPROD14785.html', 'https://www.discountbathroomvanities.com/Stufurhome-GM-6412-60ES-CR-M59-Malibu-60-Espresso-Double-Sink-Bathroom-Vanity-lwLWVC405A4F6-6.html', 'https://www.discountbathroomvanities.com/Stufurhome-HD-7130G-72-CR-Newport-72-Transitional-Double-Sink-Bathroom-Vanity-in-Grey-lwLWVFF5080B5-2.html', 'https://www.discountbathroomvanities.com/Stufurhome-HD-6868G-72-CR-Marla-72-Modern-Double-Sink-Bathroom-Vanity-in-Grey-lwPROD14816.html', 'https://www.discountbathroomvanities.com/Stufurhome-GM-5115-48-TR-Yorktown-48-Traditional-Single-Sink-Bathroom-Vanity-with-Travertine-Top-lwLWVBDCB91AC-2.html', 'https://www.discountbathroomvanities.com/Stufurhome-HD-7130G-60-CR-Newport-60-Transitional-Double-Sink-Bathroom-Vanity-in-Grey-lwLWV2814B307-C.html', 'https://www.discountbathroomvanities.com/Stufurhome-GM-3323-72-BB-Saturn-Antique-72-Double-Sink-Bathroom-Vanity-lwGM-3323-72.html', 'https://www.discountbathroomvanities.com/Stufurhome-GM-3323-72-TR-Saturn-Antique-72-Double-Sink-Bathroom-Vanity-Travertine-Top-lwLWVF32F9C72-0.html', 'https://www.discountbathroomvanities.com/Stufurhome-GM-6412-72PW-CR-Malibu-72-Transitional-Double-Sink-Bathroom-Vanity-in-White-lwPROD14798.html', 'https://www.discountbathroomvanities.com/Stufurhome-GM-6412-72ES-CR-M71-Malibu-72-Transitional-Double-Sink-Bathroom-Vanity-in-Espresso-withMirror-lwPROD14796.html', 'https://www.discountbathroomvanities.com/Stufurhome-HD-6868G-30-CR-Marla-30-Modern-Single-Sink-Bathroom-Vanity-in-Grey-withMirror-lwPROD14803.html', 'https://www.discountbathroomvanities.com/Stufurhome-GM-6412-48GY-CR-Malibu-48-Transitional-Single-Sink-Bathroom-Vanity-in-Grey-lwPROD14806.html', 'https://www.discountbathroomvanities.com/Stufurhome-HD-7000W-60-CR-Cadence-60-Transitional-Double-Sink-Bathroom-Vanity-in-White-lwLWVC2BAE0C3-7.html', 'https://www.discountbathroomvanities.com/Stufurhome-HD-6868G-60-CR-Marla-60-Modern-Double-Sink-Bathroom-Vanity-in-Grey-withMirror-lwPROD14804.html', 'https://www.discountbathroomvanities.com/Stufurhome-HD-7000W-72-CR-Cadence-72-Transitional-Double-Sink-Bathroom-Vanity-in-White-lwLWV86FF0435-4.html', 'https://www.discountbathroomvanities.com/Stufurhome-GM-2206-40-TR-Grand-Cheswick-40-Traditional-Single-Sink-Bathroom-Vanity-with-Travertine-Top-lwLWVCE92C168-A.html', 'https://www.discountbathroomvanities.com/Stufurhome-GM-6412-60PW-CR-M59-Malibu-60-White-Double-Sink-Bathroom-Vanity-lwLWVF2AB93A2-A.html', 'https://www.discountbathroomvanities.com/Stufurhome-HD-6868-30-CR-Marla-30-Transitional-Single-Sink-Bathroom-Vanity-lwLWVB40A203D-3.html', 'https://www.discountbathroomvanities.com/Stufurhome-GM-5116-48-TR-Amelia-48-Traditional-Single-Sink-Bathroom-Vanity-with-Travertine-Top-lwGM-5116.html', 'https://www.discountbathroomvanities.com/Stufurhome-GM-Y01G-Manhattan-30-Laundry-Sink-in-Grey-lwPROD14817.html', 'https://www.discountbathroomvanities.com/Stufurhome-TY-7615-59-QZ-Hamilton-59-Transitional-Double-Sink-Bathroom-Vanity-lwLWVC5CFD96B-A.html', 'https://www.discountbathroomvanities.com/Stufurhome-GM-6412-60ES-CR-Malibu-60-Transitional-Double-Sink-Bathroom-Vanity-in-Espresso-lwPROD14810.html', 'https://www.discountbathroomvanities.com/Stufurhome-GM-5115-48-BB-Yorktown-48-Traditional-Single-Sink-Bathroom-Vanity-with-Baltic-Brown-Top-lwLWV0196405B-D.html', 'https://www.discountbathroomvanities.com/Stufurhome-HD-7000G-60-CR-Cadence-60-Transitional-Double-Sink-Bathroom-Vanity-in-Grey-lwLWV7C1EE864-6.html', 'https://www.discountbathroomvanities.com/Stufurhome-GM-6412-72PW-CR-M71-Malibu-72-White-Double-Sink-Bathroom-Vanity-lwLWV40451AD2-F.html', 'https://www.discountbathroomvanities.com/Stufurhome-GM-6412-60PW-CR-Malibu-60-Transitional-Double-Sink-Bathroom-Vanity-in-White-lwPROD14786.html'}


# nx = 2
# while True:
#     links = []
#     scrollY = 0
#     last_height = chrome.execute_script("return document.body.scrollHeight")
#
#     while True:
#         scrollY += 1500
#         rets = chrome.execute_script("""
#         links = $('h5 a.product-info-link');
#         all_links = [];
#         for (i=0;i<links.length;i++){
#             link = links[i];
#             if (all_links.indexOf(link.href < 0))
#                 all_links.push(link.href);
#         }
#         return all_links;
#         """)
#         # assert type(rets) == list
#         for ret in rets:
#             if ret not in all_links:
#                 links.append(ret)
#                 all_links.add(ret)
#         chrome.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(2)
#         # Calculate new scroll height and compare with last scroll height
#         new_height = chrome.execute_script("return document.body.scrollHeight")
#         if new_height == last_height:
#             break
#         last_height = new_height
#     chrome.execute_script('RequireToChangeProducts({})'.format(nx))
#     if nx > (expected_results // 42) + 1:
#         print('next page request', nx, (expected_results // 42) + 1)
#         break
#     nx += 1
# print(len(all_links))
# print(all_links)
for link in all_links:
    data = dict().fromkeys(rows)
    chrome.get(link)
    data['sku'] = chrome.find_elements_by_css_selector('h1.product-name')[1].text.split()[2]
    data['name'] = chrome.find_element_by_css_selector('h1.product-name').text
    data['url_key'] = data['name'].lower().replace(' ', '-')
    data['price'] = chrome.find_element_by_css_selector('span.price').text[1:]
    images = chrome.find_elements_by_css_selector('.owl-item img.lazy_load[data-big-img]')
    images_name = []
    for img in images:
        img_url = 'https://www.discountbathroomvanities.com' + img.get_attribute('data-big-img')
        image_name = img_url.split('/')[-1]
        images_name.append(image_name)
        img_name = 'images/' + image_name
        urllib.request.urlretrieve(img_url, img_name)
    data['description'] = chrome.find_element_by_id("product-detail").text.replace('Description', '')
    data['additional_images'] = ';'.join(images_name)
    data['additional_attributes'] = "brand={};coming_soon=NO;model={};specifications={}".format(
        'Stufurhome',
        data['sku'],
        chrome.find_element_by_class_name('specification').text
    )
    with open('data.csv', 'a', newline='', encoding='utf-8') as file:
        writer = DictWriter(file,fieldnames=rows)
        print('writting ', data['name'])
        writer.writerow(data)
chrome.close()

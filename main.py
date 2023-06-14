import re
import requests
from htmlAttributeExtraction import *
from beautiful_print import beautiful_print, raw_print
from javascriptExtractions import extract_js_globals, extract_JSON_object
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--url',required=True ,help='URL to extract JavaScript variables and JSON objects from')
parser.add_argument('-o', '--output', required=True, help='Output file to save the results')
parser.add_argument('-b', '--beautify', action='store_true', help='Call the beautiful_print function')
args = parser.parse_args()

if args.url:
    url = args.url
else:
    print("URL is required. Please provide a valid URL using the -d or --url argument.")
    exit(1)

if args.url:
    out_put =args.output
else:
    print("Output is required. Please provide a valid output using the -o or --output argument.")
    exit(1)




headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:108.0) Gecko/20100101 Firefox/108.0",
        "Referer": url
    }


response = requests.get(url, headers=headers)
html_code = response.text


global_variable_names, local_variable_names = extract_js_globals(html_code)
json_object_names, json_object_keys = extract_JSON_object(html_code)


if args.beautify:
    beautiful_print("Locals", local_variable_names,file_Name=out_put)
    beautiful_print("Globals", global_variable_names,file_Name=out_put)
    beautiful_print("JSON OBJ Keys", json_object_keys,file_Name=out_put)
    beautiful_print("Json OBJ Names", json_object_names,file_Name=out_put)
    beautiful_print("Input tag name", extract_input_tag_names(html_code),file_Name=out_put)
    beautiful_print("Input tag id", extract_input_tag_ids(html_code),file_Name=out_put)
    beautiful_print("URL parameters", extract_url_parameters(html_code),file_Name=out_put)
else:
    raw_print(local_variable_names,file_Name=out_put)
    raw_print(global_variable_names,file_Name=out_put)
    raw_print(json_object_keys,file_Name=out_put)
    raw_print(json_object_names,file_Name=out_put)
    raw_print(extract_input_tag_names(html_code),file_Name=out_put)
    raw_print(extract_input_tag_ids(html_code),file_Name=out_put)
    raw_print(extract_url_parameters(html_code),file_Name=out_put)
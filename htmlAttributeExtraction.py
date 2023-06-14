from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs, unquote




input_tag_names = []
input_tag_ids = []
url_parameters=[]

# extract input tag names
def extract_input_tag_names(html_code):
    soup = BeautifulSoup(html_code, 'html.parser')
    for input_tag in soup.find_all('input', attrs={'name': True}):
        name_value = input_tag['name']
        if name_value.strip():
            input_tag_names.append(name_value)
    return input_tag_names


# extract input tag ids
def extract_input_tag_ids(html_code):
    soup = BeautifulSoup(html_code, 'html.parser')
    for input_tag in soup.find_all('input'):
        if 'id' in input_tag.attrs:
            id_value = input_tag['id']
            if id_value.strip():
                input_tag_ids.append(id_value)
    return input_tag_ids

def extract_url_parameters(html_code):
    soup = BeautifulSoup(html_code, 'html.parser')
    for a_tag in soup.find_all('a'):
        href_value = a_tag.get('href')
        if href_value is not None:
            parsed_url = urlparse(href_value)
            query_parameters = parse_qs(parsed_url.query)

            # Check if the URL is encoded or not
            if '%' in href_value:
                for param, values in query_parameters.items():
                    for value in values:
                        decoded_param = unquote(param)
                        decoded_value = unquote(value)
                        url_parameters.append((decoded_param, decoded_value))
            else:
                for param, value in query_parameters.items():
                    url_parameters.append(param)
    return url_parameters
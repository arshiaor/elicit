import re
from pyjsparser import parse, JsSyntaxError

def extract_js_globals(html_code):
    global_variable_names = []
    local_variable_names = []

    def extract_variables(node, scope="global"):
        if isinstance(node, dict):
            if node.get("type") == "VariableDeclaration" and (node.get("kind") == "var" or node.get("kind") == "let"):
                for declaration in node["declarations"]:
                    if declaration.get("init"):
                        variable_name = declaration["id"]["name"]
                        if scope == "global":
                            global_variable_names.append(variable_name)
                        elif scope == "local":
                            local_variable_names.append(variable_name)
            if node.get("type") == "FunctionDeclaration":
                for var_decl in node["body"]["body"]:
                    if var_decl.get("type") == "VariableDeclaration" and (var_decl.get("kind") == "var" or var_decl.get("kind") == "let"):
                        for declaration in var_decl["declarations"]:
                            if declaration.get("init"):
                                variable_name = declaration["id"]["name"]
                                local_variable_names.append(variable_name)

            for key, value in node.items():
                if isinstance(value, (dict, list)):
                    extract_variables(value, scope)
        elif isinstance(node, list):
            for item in node:
                extract_variables(item, scope)

    script_pattern = r"<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>"
    cdata_pattern = r"<!\[CDATA\[(.*?)\]\]>"

    script_matches = re.findall(script_pattern, html_code, re.DOTALL)
    for match in script_matches:
        try:
            script_code = re.sub(r"<.*?>", "", match)
            script_code = re.sub(r"//.*?\n|/\*.*?\*/", "", script_code)
            extract_variables(parse(script_code), scope="global")
        except JsSyntaxError as e:
            print(f"Syntax error occurred: {e}")

    cdata_matches = re.findall(cdata_pattern, html_code, re.DOTALL)
    for match in cdata_matches:
        try:
            tree = parse(match)
            extract_variables(tree, scope="global")
        except JsSyntaxError as e:
            print(f"Syntax error occurred: {e}")

    return global_variable_names, local_variable_names


def extract_JSON_object(html_code):
    json_object_names = []
    json_object_keys = []

    script_pattern = r"<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>"
    script_matches = re.findall(script_pattern, html_code, re.DOTALL)
    for match in script_matches:
        json_matches = re.findall(r"var\s+(\w+)\s+=\s+({.*?})", match, re.MULTILINE | re.DOTALL)
        for json_match in json_matches:
            json_object_name = json_match[0]
            json_object_text = json_match[1]
            json_object = eval(json_object_text)
            json_object_names.append(json_object_name)
            json_object_keys.extend(json_object.keys())

    return json_object_names, json_object_keys

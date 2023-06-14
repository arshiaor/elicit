def beautiful_print(scope, variable,file_Name):
    with open(file_Name, "a") as file:
        file.write(f"{scope}:\n")
        file.write("-" * 20 + "\n")

        if len(variable) == 0:
            file.write("Empty\n")
        else:
            file.write("\n".join(variable))

        file.write("\n\n")

def raw_print(variable,file_Name):
    with open(file_Name,"a") as file:
        file.write("\n".join(variable))
        file.write("\n")


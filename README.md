# elicit
Elicit tool is written to extract so called "Majical Variables" from the source of a website to capture and save data like JS variables, etc as an asset to use in bug hunting. <br><br>
**Note!** you have to have Python installed in order to use this tool <br>
---
### Installation <br>
First clone the repository
>`git clone https://github.com/arshiaor/elicit` <br>

Then install the requirements by
>` pip install -r requirements.txt` <br>
---
### Usage <br>
This tool gets multiple input arguments, as an exmple:
>`python main.py -d domain.com -o ./extracted_variables.txt` <br>

#### arguments
> -d&nbsp; → &nbsp;  gets domain as an input  **(Mandatory)** <br>
> -o&nbsp; → &nbsp;  gets a file to print the output  **(Mandatory)** <br>
> -b&nbsp; → &nbsp;  Prints the output in a beautiful way **(Optional)**
---
please if you encounter any issues, open an issue in the github and for collaboration inquiries like feature addition please fork the project
and create a pull request. 
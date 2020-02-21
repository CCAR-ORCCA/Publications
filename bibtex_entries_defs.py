# MIT License

# Copyright (c) 2019 Benjamin Bercovici and Jay McMahon

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from bibtexparser.bibdatabase import as_text
import bibtexparser


#############################################
# \name : bibtex_entries_def.py
# \author : Benjamin Bercovici
# \date : 02/10/19
# \brief : functions used to populated HTML entries 
# for various publication types
# \dependencies:
# - bibtexparser must be installed.
# it can be retrieved through `pip install bibtexparser`
# \usage : Do not use the functions in this file as is.
# They should be called by biblio_export.py
#############################################


def sort_by_year(entry):
    try:
        return int(entry["year"])
    except KeyError:
        try:

            return int(entry["Year"])
        except KeyError:
            return 1970

def proceedings_latex_entry_to_html_box(entry):
    string = "<br />[expand title=\"BibTex\" style=\"small\"] [box color=\"lightgray\" style=\"filled\" float=\"none\"]<br />"

    # Get all keys in entry
    entry_keys = list(entry.keys())

    # Start writing string
    string += "@" + entry["ENTRYTYPE"] + "{"

    string += entry["ID"] + ",<br />"
    
    try:
        string += "Address = {" + entry["address"] + "},<br />"
    except KeyError:
        None

    try:
        string += " title = {" + entry["title"] + "},<br />"
    except KeyError:
        None

    try:
        string += " Booktitle = {" + entry["booktitle"] + "},<br />"
    except KeyError:
        None

    try:
        string += "Year = {" + entry["year"] + "},<br />"
    except KeyError:
        try:
            string += "Year = {" + entry["Year"] + "},<br />"
        except KeyError:
            None

    string += " Author = {" + entry["author"] + "}<br />"

    # Finish writing string
    string += "}\n"
   
    string += "[/box]<font face=\"monospace\"> </font>[/expand]"
    return string

def journal_latex_entry_to_html_box(entry):
    string = "<br />[expand title=\"BibTex\" style=\"small\"] [box color=\"lightgray\" style=\"filled\" float=\"none\"]<br />"

    # Get all keys in entry
    entry_keys = list(entry.keys())

    # Start writing string
    string += "@" + entry["ENTRYTYPE"] + "{"

    string += entry["ID"] + ",<br />"
    
    try:
        string += "Title = {" + entry["title"] + "},<br />"
    except KeyError:
        None

    try:
        string += "Volume = {" + entry["volume"] + "},<br />"
    except KeyError:
        None

    try:
        string += "Keywords = {" + entry["keywords"] + "},<br />"
    except KeyError:
        None

    try:
        string += "Issue = {" + entry["number"] + "},<br />"
    except KeyError:
        None

    try:
        string += "Journal = {" + entry["journal"] + "},<br />"
    except KeyError:
        None

    try:
        string += "DOI = {" + entry["doi"] + "},<br />"
    except KeyError:
        try:
            string += "DOI = {" + entry["DOI"] + "},<br />"
        except KeyError:
            None

    try:
        string += "Year = {" + entry["year"] + "},<br />"
    except KeyError:
        try:
            string += "Year = {" + entry["Year"] + "},<br />"
        except KeyError:
            None

    string += " Author = {" + entry["author"] + "}<br />"

    # Finish writing string
    string += "}\n"
   
    string += "[/box]<font face=\"monospace\"> </font>[/expand]"
    return string

def thesis_latex_entry_to_html_box(entry):
    string = "<br />[expand title=\"BibTex\" style=\"small\"] [box color=\"lightgray\" style=\"filled\" float=\"none\"]<br />"

    # Get all keys in entry
    entry_keys = list(entry.keys())

    # Start writing string
    string += "@" + entry["ENTRYTYPE"] + "{"

    string += entry["ID"] + ",<br />"
    
    try:
        string += " title = {" + entry["title"] + "},<br />"
    except KeyError:
        None

    try:
        string += "URL = {" + entry["url"] + "},<br />"
    except KeyError:
        try:
            string += "URL = {" + entry["url"] + "},<br />"
        except KeyError:
            None

    try:
        string += "Year = {" + entry["year"] + "},<br />"
    except KeyError:
        try:
            string += "Year = {" + entry["Year"] + "},<br />"
        except KeyError:
            None

    string += " Author = {" + entry["author"] + "}<br />"

    # Finish writing string
    string += "}\n"
   
    string += "[/box]<font face=\"monospace\"> </font>[/expand]"
    return string

def misc_latex_entry_to_html_box(entry):
    string = "<br />[expand title=\"BibTex\" style=\"small\"] [box color=\"lightgray\" style=\"filled\" float=\"none\"]<br />"

    # Get all keys in entry
    entry_keys = list(entry.keys())

    # Start writing string
    string += "@" + entry["ENTRYTYPE"] + "{"

    string += entry["ID"] + ",<br />"
    
    try:
        string += " title = {" + entry["title"] + "},<br />"
    except KeyError:
        None

    try:
        string += "URL = {" + entry["url"] + "},<br />"
    except KeyError:
        try:
            string += "URL = {" + entry["URL"] + "},<br />"
        except KeyError:
            None

    try:
        string += "Year = {" + entry["year"] + "},<br />"
    except KeyError:
        try:
            string += "Year = {" + entry["Year"] + "},<br />"
        except KeyError:
            None

    string += " Author = {" + entry["author"] + "}<br />"

    # Finish writing string
    string += "}\n"
   
    string += "[/box]<font face=\"monospace\"> </font>[/expand]"
    return string



def create_journal_entry(entry):
    
    # Starting item
    formatted_entry = "\n<li>"

    # Authors
    formatted_entry += entry["author"]

    # Year
    try:
        formatted_entry += " (" + str(entry['year']) + "). "
    except KeyError:
        try:
            formatted_entry += " (" + str(entry['Year']) + "). "
        except KeyError:
            print("No year found in " + str(entry["ID"]))
            formatted_entry += " (no year). "

    # Title
    formatted_entry +=  entry["title"].replace("{","").replace("}","")

    # Journal 
    formatted_entry += ". <em>" + entry["journal"] +  "</em>"

    # Volume 
    try:
        formatted_entry += ", Volume " + entry["volume"]
    except KeyError:
        print ("No volume in " + str(entry["ID"]))
  
    # Issue
    try:
        formatted_entry += ", Issue " + entry["number"]
    except KeyError:
        print ("No number in " + str(entry["ID"]))


    # DOI
    try:
        formatted_entry += " (" + entry["doi"] + ")"
    except KeyError:
        try:
            formatted_entry += " (" + entry["DOI"] + ")"
        except KeyError:
            print("No doi found in " + str(entry["ID"]))


    # Bibtex box
    formatted_entry += journal_latex_entry_to_html_box(entry)

    # Closing item
    formatted_entry += "</li><br />\n"


    return formatted_entry

def create_proceedings_entry(entry):

    # Starting item
    formatted_entry = "\n<li>"

    # Authors
    formatted_entry += entry["author"]

    # Year
    try:
        formatted_entry += " (" + str(entry['year']) + "). "
    except KeyError:
        try:
            formatted_entry += " (" + str(entry['Year']) + "). "
        except KeyError:
            formatted_entry += " (no year). "
            print("No year found in " + str(entry["ID"]))

    # Title
    formatted_entry += " " + entry["title"].replace("{","").replace("}","")

    # Proceedings 
    try:
        formatted_entry += ". <em>" + entry["booktitle"] +  "</em>. "
    except KeyError:
        print ("No booktitle found in " + str(entry["ID"]))
   
    # Address of conferences
    try:
        formatted_entry += entry["address"]
    except KeyError:
        print ("No address found in " + str(entry["ID"]))

    # Bibtex box
    formatted_entry += proceedings_latex_entry_to_html_box(entry)

    # Closing item
    formatted_entry += "</li><br />\n"


    return formatted_entry

def create_thesis_entry(entry):

    # Starting item
    formatted_entry = "\n<li>"

    # Authors
    formatted_entry += entry["author"]

    # Year
    try:
        formatted_entry += " (" + str(entry['year']) + "). "
    except KeyError:
        try:
            formatted_entry += " (" + str(entry['Year']) + "). "
        except KeyError:
            print("No year found in " + str(entry["ID"]))

    # Title
    formatted_entry += " " + entry["title"].replace("{","").replace("}","")

    # Bibtex box
    formatted_entry += thesis_latex_entry_to_html_box(entry)

    # Closing item
    formatted_entry += "</li><br />\n"


    return formatted_entry

def create_misc_entry(entry):

    # Starting item
    formatted_entry = "\n<li>"

    # Authors
    formatted_entry += entry["author"]

    # Year
    try:
        formatted_entry += " (" + str(entry['year']) + "). "
    except KeyError:
        try:
            formatted_entry += " (" + str(entry['Year']) + "). "
        except KeyError:
            print("No year found in " + str(entry["ID"]))

    # Title
    formatted_entry += " " + entry["title"].replace("{","").replace("}","")
     
    # Url
    try:
        formatted_entry += " (" + str(entry['url']) + "). "
    except KeyError:
        try:
            formatted_entry += " (" + str(entry['Url']) + "). "
        except KeyError:
            print("No url found in " + str(entry["ID"]))

    # Bibtex box
    formatted_entry += misc_latex_entry_to_html_box(entry)

    # Closing item
    formatted_entry += "</li><br />\n"


    return formatted_entry

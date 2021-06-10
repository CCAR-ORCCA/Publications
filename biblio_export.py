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


import bibtexparser
from bibtex_entries_defs import *
from merge_bibfiles import *
import glob, os


#############################################
# \name : biblio_export.py
# \author : Benjamin Bercovici
# \date : 02/10/19
## modified by Kenshiro Oguri on Sept. 1, 2019
# \brief : a python script that parses .bib
# files to produce a structured HTML page 
# listing the different publications sorted by type/year
# \dependencies:
# - bibtexparser must be installed.
# it can be retrieved through `pip install bibtexparser`
# - bibtex_entries_defs.py 
# \usage : Have all the .bib files of interest in 
# the same folder as biblio_export.py and run the script
#############################################


# Creating empty containers
journal_articles = []
conference_proceedings = []
misc = []
mislabeled = []
theses = []


### Added by Kenshiro Oguri
### FROM HERE
# Merge .bib files into a large .bib file
mergedFileName = 'ORCCA_merged.bib'
generate_merged_bibfile(mergedFileName)

# Reading from the merged .bib file
with open(mergedFileName) as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

# Put each publication in the correct category
for entry in bib_database.entries:
    if entry["ENTRYTYPE"] == "inproceedings":
        conference_proceedings += [entry]
    elif entry["ENTRYTYPE"] == "article":
        journal_articles += [entry]
    elif entry["ENTRYTYPE"] == "misc":
        misc += [entry]
    elif entry["ENTRYTYPE"] == "phdthesis":
        theses += [entry]
    else:
        mislabeled += [entry]
### TO HERE


### Ben's original script that retrieves the entries from bibfiles
### FROM HERE
# for file in glob.glob("*.bib"):
    
#     # Reading from each of the .bib files that were found
#     with open(file) as bibtex_file:
#         bib_database = bibtexparser.load(bibtex_file)

#     # Uncomment this to see the content of each bib file
#     # print (bib_database.entries)

#     # Put each publication in the correct category
#     for entry in bib_database.entries:
#         if entry["ENTRYTYPE"] == "inproceedings":
#             conference_proceedings += [entry]
#         elif entry["ENTRYTYPE"] == "article":
#             journal_articles += [entry]
#         elif entry["ENTRYTYPE"] == "misc":
#             misc += [entry]
#         elif entry["ENTRYTYPE"] == "phdthesis":
#             theses += [entry]
#         else:
#             mislabeled += [entry]
### TO HERE

# Sorting each publication type by year
conference_proceedings = sorted(conference_proceedings, key = sort_by_year)[::-1] 
journal_articles = sorted(journal_articles, key = sort_by_year)[::-1] 
misc = sorted(misc, key = sort_by_year)[::-1] 
theses = sorted(theses, key = sort_by_year)[::-1]


# Lists any entry whose "ENTRYTYPE" is not amongst ["inproceedings" ,"article", "misc", "phdthesis"]
if (len(mislabeled) > 0):
    print("Mislabeled entries: ")
    for entry in mislabeled:
        print(entry)

# Start Writing the HTML page
page = []

# Journal papers
page += ["<h2 class=\"lead\">Journal Papers</h2>\n"]
page += ["<ol reversed>\n"]
for journal_entry in journal_articles:
    page += create_journal_entry(journal_entry)
page += ["</ol>\n"]

# Conference proceedings
page += ["<h2 class=\"lead\">Conference Proceedings</h2>\n"]
page += ["<ol reversed>\n"]
for conference_proceedings_entry in conference_proceedings:
    page += create_proceedings_entry(conference_proceedings_entry)
page += ["</ol>\n"]

# Theses
page += ["<h2 class=\"lead\">Theses</h2>\n"]
page += ["<ol reversed>\n"]
for theses_entry in theses:
    page += create_thesis_entry(theses_entry)
page += ["</ol>\n"]

# Misc
page += ["<h2 class=\"lead\">Miscellaneous</h2>\n"]
page += ["<ol reversed>\n"]
for misc_entry in misc:
    page += create_misc_entry(misc_entry)
page += ["</ol>\n"]

# Show some statistics
print("ORCCA Publications count:\n")
print ("\t" + str(len(conference_proceedings)) + " conference proceedings")
print ("\t" + str(len(journal_articles)) + " journal articles")
print ("\t" + str(len(theses)) + " theses")
print ("\t" + str(len(misc)) + " miscellaneous entries")
print ("\t" + str(len(mislabeled)) + " mislabeled entries")

# Saving the page
with open('orcca_publications.html', 'w') as f:
    for item in page:
        f.write("%s" % item)




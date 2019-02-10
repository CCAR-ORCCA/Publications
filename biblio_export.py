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
import glob, os


# Creating empty containers
journal_articles = []
conference_proceedings = []
misc = []
mislabeled = []
theses = []

for file in glob.glob("*.bib"):
    
    # Reading from the bib file storing all of ORCCA's publications to date
    with open(file) as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
    print (bib_database.entries)
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

# Sorting each publication type by year
conference_proceedings = sorted(conference_proceedings, key = sort_by_year)[::-1] 
journal_articles = sorted(journal_articles, key = sort_by_year)[::-1] 
misc = sorted(misc, key = sort_by_year)[::-1] 
theses = sorted(theses, key = sort_by_year) [::-1]


# Lists any entry whose "ENTRYTYPE" is not amongst ["inproceedings" ,"article", "misc", "phdthesis"]
if (len(mislabeled) > 0):
    print("Mislabeled entries: ")
    for entry in mislabeled:
        print(entry)

# Start Writing the HTML page
page = []

# Journal papers
page += ["<p class=\"lead\">Journal Papers</p>\n"]
page += ["<ol>\n"]
for journal_entry in journal_articles:
    page += create_journal_entry(journal_entry)
page += ["</ol>\n"]

# Conference proceedings
page += ["<p class=\"lead\">Conference Proceedings</p>\n"]
page += ["<ol>\n"]
for conference_proceedings_entry in conference_proceedings:
    page += create_proceedings_entry(conference_proceedings_entry)
page += ["</ol>\n"]

# Theses
page += ["<p class=\"lead\">Theses</p>\n"]
page += ["<ol>\n"]
for theses_entry in theses:
    page += create_thesis_entry(theses_entry)
page += ["</ol>\n"]

# Misc
page += ["<p class=\"lead\">Miscellaneous</p>\n"]
page += ["<ol>\n"]
for misc_entry in misc:
    page += create_misc_entry(misc_entry)
page += ["</ol>\n"]

# Show some statistics
print("ORCCA Publications count:\n")
print ("\t" + str(len(conference_proceedings)) + " conference proceedings")
print ("\t" + str(len(journal_articles)) + " journal articles")
print ("\t" + str(len(misc)) + " miscellaneous entries")
print ("\t" + str(len(mislabeled)) + " mislabeled entries")

# Saving the page
with open('orcca_publications.html', 'w') as f:
    for item in page:
        f.write("%s" % item)




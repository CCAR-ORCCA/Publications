from bibtexparser.bparser import BibTexParser
import bibtexparser
import glob, os, textwrap

#############################################
# \name : merge_bibfiles.py
# \author : Benjamin Bercovici
# \date : 09/01/19
# \brief : a python script that merges .bib
# files to produce a merged .bib files, removing duplicate entries 
# \dependencies:
# - bibtexparser must be installed.
# it can be retrieved through `pip install bibtexparser`
# \usage : Have all the .bib files of interest in 
# the same folder as merge_bibfiles.py and run the script.
# A merged .bib file is generated
#############################################


def generate_merged_bibfile(mergedFileName):
    if os.path.exists(mergedFileName): os.unlink(mergedFileName)    
    
    myparser = BibTexParser(common_strings=True)
    entry_i_keys = []
    
    for file in glob.glob("*.bib"):
        
        # Reading from each of the .bib files that were found
        with open(file, 'r') as bibfile:
            bp = bibtexparser.load(bibfile, parser=myparser)
            # bp = BibTexParser(bibfile)
            entries_i = bp.get_entry_list()
    
        for entry in entries_i:
            if not entry['ID'] in entry_i_keys:
                with open(mergedFileName, 'a') as f:
                    f.write(format_bibtex_entry(entry))
    
        # store keys to check for duplicates
        entry_i_keys += [entry['ID'] for entry in entries_i]


def format_bibtex_entry(entry):
    # field, format, wrap or not
    field_order = [(u'author', '{{{0}}},\n', True),
                   (u'title', '{{{0}}},\n', True),
                   (u'journal', '"{0}",\n', True),
                   (u'volume', '{{{0}}},\n', True),
                   (u'number', '{{{0}}},\n', True),
                   (u'pages', '{{{0}}},\n', True),
                   (u'year', '{0},\n', True),
                   (u'doi', '{{{0}}},\n', False)]
    
    keys = set(entry.keys())

    extra_fields = keys.difference([f[0] for f in field_order])
    # we do not want these in our entry
    extra_fields.remove('ENTRYTYPE')
    extra_fields.remove('ID')

    # Now build up our entry string
    s = '@{type}{{{id},\n'.format(type=entry['ENTRYTYPE'],
                                  id=entry['ID'])

    for field, fmt, wrap in field_order:
        if field in entry:
            s1 = '  {0} ='.format(field)
            s2 = fmt.format(entry[field])
            s3 = '{0:17s}{1}'.format(s1, s2)
            if wrap:
                # fill seems to remove trailing '\n'
                s3 = textwrap.fill(s3, subsequent_indent=' '*18, width=70) + '\n'
            s += s3  

    for field in extra_fields:
        if field in entry:
            s1 = '  {0} ='.format(field)
            s2 = entry[field]
            s3 = '{0:17s}{{{1}}},'.format(s1, s2)
            s3 = textwrap.fill(s3, subsequent_indent=' '*18, width=70) + '\n'
            s += s3  

    s += '}\n\n'
    return s

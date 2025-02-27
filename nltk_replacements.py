import xml.etree.ElementTree as ElementTree
from nltk.corpus.reader.childes import CHILDESCorpusReader
import re

ccr = CHILDESCorpusReader("","") #just to be able to use the function

def get_age(NS, fileid, speaker="CHI", month=True):
    xmldoc = ElementTree.parse(fileid).getroot()
    for pat in xmldoc.findall(f".//{{{NS}}}participants/{{{NS}}}participant"):
        try:
            if pat.get("id") == speaker:
                age = pat.find(f".//{{{NS}}}age").text
                if month:
                    age = ccr.convert_age(age)
                return age
        # some files don't have age data
        except (TypeError, AttributeError) as e:
            return "Could not find age"

#ifndef XMLPARSE.PY
#define XMLPARSE.PY
#!/usr/bin/python
# -*- coding: utf-8 -*-

import locale
import piksemel

language = locale.getdefaultlocale()[0].split("_")[0]

doc = piksemel.parse("/home/pars/workspace/pisi-index.xml") #Parsing .xml file

for tags in doc.tags("Package"):
    
    print "Name : ",tags.getTagData("Name")
    
    for lang in tags.tags("Description"):
    
        if language == lang.getAttribute("xml:lang"):
        
            print "Description : ",lang.firstChild().data()
    
    print "Version : ",tags.getTag("History").getTag("Update").getTagData("Version") 
    print "Date : ",tags.getTag("History").getTag("Update").getTagData("Date")
    print "-------------------------------------------------------------------------"


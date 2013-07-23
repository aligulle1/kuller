#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys

import urllib
import lzma
import bz2
import piksemel


def setUrl(which):
    dict = {
            '2009' : 'http://packages.pardus.org.tr/pardus/2009/test/i686/pisi-index.xml.bz2',
            '2011' : 'http://packages.pardus.org.tr/pardus/2011/test/x86_64-debug/pisi-index.xml.xz',
            'Corporate2' : 'http://packages.pardus.org.tr/pardus/corporate2/devel/x86_64-debug/pisi-index.xml.xz'
     }

    #default 2009
    return dict.get( which, dict['2009'])


def downloadFile( ):
    try:
        response = urllib.urlopen(url)

    except  IOError:
        print "Name or service not known"

    global data
    data = response.read()
    response.close()


def getFileType( ):
    if url.endswith("xz"):
        file_type = "lzma"

    elif url.endswith("bz2"):
        file_type = "bz2"

    else:
        print "unknown filetype"
        exit(1)

    return file_type



def getDocument():
    global document

    file_type =  getFileType()

    if file_type == "lzma" :
        cmp_data = lzma.decompress( data )

    elif file_type == "bz2" :
        cmp_data = bz2.decompress( data )

    else:
        print "not support filetype for decompress"
        exit(1)

    document = piksemel.parseString(cmp_data)


def getObsolitePackageList():
    global document

    obsolete_package_list = []

    package_elements = document.getTag("Distribution").getTag("Obsoletes").tags("Package")

    for package in package_elements:
        package_name = package.firstChild().data()
        obsolete_package_list.append( package_name )

    return obsolete_package_list



form = """
        Package Name  : %s
        Debug Package : %s
    """

if __name__ == "__main__":
    data = None
    document = None
    which_release = None
    len_dbginfo = len("-dbginfo")

    if len(sys.argv) > 1 :
        which_release = sys.argv[1]

    url = setUrl(which_release)

    downloadFile()
    getDocument()

    obsolete_package_list =  getObsolitePackageList()

    package_elements = document.tags( "Package" )

    for package in package_elements:
        package_src_name = package.getTag( "Source" ).getTagData( "Name" )
        package_name =  package.getTagData("Name")

        if package_src_name in obsolete_package_list or package_name[:-len_dbginfo] in obsolete_package_list :
            packageURI = package.getTagData( "PackageURI" )

            print form % (package_name, packageURI)
            


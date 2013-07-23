#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import re
import glob
import shutil

import piksemel
import zipfile
import tarfile
import lzma


class Handler(object):
    file_name = None
    nod_tree = None

    def __init__(self):
        print "base class init"

    def fix(self, file_data):
        self.nod_tree = piksemel.parseString(file_data)
        self.fixElementsData()   # hook method
        self.xmltoString()
        self.reproduceFile()

    def xmltoString(self):
        self.nod_tree =  self.nod_tree.toPrettyString()

    def reproduceFile(self):
        f = open( self.file_name, "w")
        f.write(self.nod_tree)
        f.close()


class MetadataXML(Handler):
    packagename = None
    havechange = 0

    def __init__(self):
        self.file_name = "metadata.xml"

    def fixElementsData(self):
        paths = self.nod_tree.getTag("Package").getTag("Files").tags("Path")
        for path in paths:

            path_data = fixedPath( path.firstChild().data()[1:] + "/" )
            if path_data :
                path.setData( path_data)
                self.havechange = 1
            else :
                path.hide()

        self.nod_tree.getTag("Package").getTag("Architecture").setData("x86_64")

        self.setPackageName()

    def setPackageName(self):
        package_node = self.nod_tree.getTag("Package")
        name         = package_node.getTag("Source").getTagData("Name")
        version      = package_node.getTag("History").tags("Update").next().getTagData("Version")
        architecture = package_node.getTagData("Architecture")

        self.packagename = "%s-%s-p11-%s.pisi" % ( name, version, architecture)


class FilesXML(Handler):
    def __init__(self):
        self.file_name = "files.xml"

    def fixElementsData(self):
        files_node = self.nod_tree.tags("File")

        for file_el in files_node:
            fixed_path = fixedPath( "/" + file_el.getTagData("Path"))

            if fixed_path :
                file_el.getTag("Path").setData(fixed_path)
            else:
                file_el.hide()


class InstallTAR():
    def extractInstallTarXZ(self, lzma_archive, output):
        lzma_file = lzma.LZMAFile(lzma_archive, "r")
        output = open(output, "w")
        output.write(lzma_file.read())
        output.close()
        lzma_file.close()

    def createTarArchive( self, source_directory, tar_name):
        tf = tarfile.open(tar_name, mode='w')

        dir_list = os.listdir( source_directory )
        dir_list.sort()

        for dir_name in dir_list:
            tf.add( os.path.join( source_directory, dir_name) , arcname=dir_name)

        tf.close()

    def reproduceInstallTar(self, old_tar, new_tar ):
        temporary_path = "install"

        """create temporary directory"""
        makeDir(temporary_path)

        old_tar = tarfile.open(old_tar, mode='r')

        """get members installTAr"""
        members =  old_tar.getmembers()
        members.sort()

        """extract tar's members to correct scope"""
        for member in members:
            fixed_path =  fixedPath(member.name)

            if fixed_path :
                member.name = fixed_path
                old_tar.extract(member, temporary_path)

        """create tar archive"""
        self.createTarArchive(temporary_path, new_tar)

        old_tar.close()

    def garbageCollect(self):
        os.unlink("old.tar")
        os.unlink("install.tar.xz")
        shutil.rmtree("install")

    def fix(self, fileTarXZ):
        self.extractInstallTarXZ( fileTarXZ , "old.tar")
        self.reproduceInstallTar("old.tar", "install.tar")
        self.garbageCollect()

        #FIXME: use pyliblzma
        os.system("xz -9 install.tar")


def makeDir(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    if os.makedirs(path):
        print "%s directory don't created"

def fixedPath( data) :
    for pattern in [r'/usr/lib/',
                    r'/lib/',
                ]:
        regex = re.compile(pattern)

        if regex.search(data) :
            path = "%s32/" % pattern[:-1]
            return regex.sub(path, data)

    for pattern in [r'/usr/bin/',
                   r'/bin/',
                   ]:
        regex = re.compile(pattern)

        if regex.search(data) :
            path = "%s32/" % pattern
            return regex.sub(path, data)

    return None


def createPisifor64Arc(package):
    """create and change temporary directory"""
    makeDir(".tmp")
    os.chdir(".tmp")

    """extract package to temporary directory"""
    zip_file = zipfile.ZipFile(package)
    zip_file.extractall()
    zip_file.close()

    """read and fix metadata and filesxml datas"""
    metadata_handler.fix( file("metadata.xml").read())

    if metadata_handler.havechange == 0:
        print "%s  package, which has got neither library and binary files wasn't created" % metadata_handler.packagename
        return
    else:
        metadata_handler.havechange = 0

    files_handler.fix( file( "files.xml" ).read())
    install_handler.fix("install.tar.xz" )

    """reproduce pisi package- zipArchive"""
    packagename = os.path.join(dest_directory, metadata_handler.packagename)
    zip_file = zipfile.ZipFile(packagename, "w" )

    for root, dirs, files in os.walk("."):
        for name in files:
            file_path = os.path.join(root, name)
            zip_file.write(file_path, arcname=file_path.split("/", 1)[1])   #remove directory name
    zip_file.close()


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "Usage: \n%s  <pisi_packages_directory> <destination_directory>" % sys.argv[0]
        sys.exit(1)

    if not os.path.exists(sys.argv[1]):
        print "%s does not exists" % sys.argv[1]
        sys.exit(1)

    pisi_directory = os.path.realpath( sys.argv[1] )
    dest_directory = os.path.realpath( sys.argv[2] )

    """create dest-directory"""
    makeDir(dest_directory)

    """create instances"""
    metadata_handler = MetadataXML()
    files_handler = FilesXML()
    install_handler = InstallTAR()

    for pisi in glob.glob1( pisi_directory, "*i686.pisi" ):
        createPisifor64Arc( os.path.join(pisi_directory, pisi) )


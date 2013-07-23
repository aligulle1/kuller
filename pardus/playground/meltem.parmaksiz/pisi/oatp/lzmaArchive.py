#!/usr/bin/python
# -*- coding: utf-8 -*-

import lzma

def unpackLZMA(lzma_archive, output):
    lzma_file = lzma.LZMAFile(lzma_archive, "r")
    output = open(output, "w")
    output.write(lzma_file.read())
    output.close()
    lzma_file.close()


compressformat= "xz"
compresslevel=9

def compressLZMA(data, archive_name):                     #file("install.tar").read()
    options = {"format":    compressformat,
               "level":     compresslevel}

    lzmaobj = lzma.LZMACompressor()
    lzmaobj.reset(options)
    #compress_data = lzmaobj.compress(data)

    fileobj = lzma.LZMAFile(archive_name , "w", options = options)
    fileobj.write( lzmaobj.compress(data) )
    fileobj.close()



if __name__ == "__main__":
    #unpackLZMA("install.tar.xz", "meltem.tar")
    compressLZMA( file("meltem.tar").read(), "meltem.tar.xz" )



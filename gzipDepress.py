#!/usr/bin/env python
# encoding=utf-8
import zlib
import StringIO, gzip

'''def compress(infile, dst, level=9):
    infile = "/home/caidong/00000001"
    dst = "/home/caidong/1.txt"
    infile = open(infile, 'rb')
    dst = open(dst, 'wb')
    compress = zlib.compressobj(level)
    data = infile.read(1024)
    while data:
        dst.write(compress.compress(data))
        data = infile.read(1024)
    dst.write(compress.flush())'''

'''def decompress(infile, dst):'''
infile = "/home/caidong/00000001"
dst = "/home/caidong/1.html"
infile = open(infile, 'rb')
dst = open(dst, 'wb')
'''decompress = zlib.decompressobj()
data = infile.read(1024)
while data:
        dst.write(decompress.decompress(data))
        data = infile.read(1024)
dst.write(decompress.flush())
'''
decompressed_data=zlib.decompress(infile.read(), 16+zlib.MAX_WBITS)
print decompressed_data
'''data = infile
compressedstream = StringIO.StringIO(data)
gziper = gzip.GzipFile(fileobj=compressedstream)
data2 = gziper.read()   # 读取解压缩后数据
print data2'''

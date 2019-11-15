import urllib.request
import zlib
from random import randint
from LZW import lzw_compress
from LZW import lzw_decompress
url = "http://gutenberg.pglaf.org/1/6/6/1661/1661.txt"
sh = urllib.request.urlopen(url).read().decode('utf-8')
sh_length = len(sh)
rnd = ''.join([chr(randint(0,126)) for k in range(sh_length)])


def zipped(text):
    return len(zlib.compress(text.encode("ascii")))


print("Исходный размер:", sh_length)
print("Сжатие до :",zipped(sh))
print("Сжатие до случайного файла:", zipped(rnd))


text =  "ABCCCDAAD"
compressed = lzw_compress(text)
print('\nУпаковано: %s \n' %compressed)

print('\nРаспаковано string : %s' % lzw_decompress(compressed))
print('Исходная строка : %s' % text)




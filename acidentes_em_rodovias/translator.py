#!/usr/bin/env python
# coding: utf-8

"""
 Script to helps on translate some code's methods from
 portuguese to english.
 """

from multiprocessing import Pool
from mock import MagicMock
from goslate import Goslate
import fnmatch
import logging
import os
import re
import urllib2

_MAX_PEERS = 30

try:
    os.remove('traducoes.log')
except OSError:
    pass
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('traducoes.log')
logger.addHandler(handler)


def fileWalker(ext, dirname, names):
    """
    Find the files with the correct extension
    """
    pat = "*" + ext[0]
    for f in names:
        if fnmatch.fnmatch(f, pat):
            ext[1].append(os.path.join(dirname, f))


def encontre_text(file):
    """
    find on the string the works wich have '_' on it
    """
    text = file.read().decode('utf-8')
    return re.findall(r"\w+(?<=_)\w+", text)
    #return re.findall(r"\"\w+\"", text)


def traduza_palavra(txt):
    """
        Translate the word/phrase to english
    """
    try:
        # try connect with google
        response = urllib2.urlopen('http://74.125.228.100', timeout=2)
        pass
    except urllib2.URLError as err:
        print "No network connection "
        exit(-1)
    if txt[0] != '_':
        txt = txt.replace('_', ' ')
    txt = txt.replace('media'.decode('utf-8'), 'média'.decode('utf-8'))
    gs = Goslate()
    #txt = gs.translate(txt, 'en', gs.detect(txt))
    txt = gs.translate(txt, 'en', 'pt-br')  # garantindo idioma tupiniquim
    txt = txt.replace(' en ', ' br ')
    return txt.replace(' ', '_')  # .lower()


def subistitua(file, txt, novo_txt):
    """
    should rewrite the file with the new text in the future
    """
    text = file.read()
    print '%s -> %s' % (txt, novo_txt)
    text = text.replace(txt.encode('utf-8'), novo_txt.encode('utf-8'))
    file.seek(0)  # rewind
    file.write(text)


def magica(File):
    """
    Thread Pool. Every single thread should play around here with
    one element from list os files
    """
    global _DONE
    if _MAX_PEERS == 1:  # inviavel em multithread
        logger.info('\n---- File %s' % File)
    with open(File, "r+") as file:
        list_txt = encontre_text(file)
        for txt in list_txt:
            novo_txt = traduza_palavra(txt)
            if txt != novo_txt:
                logger.info('%s -> %s [%s]' % (txt, novo_txt, File))
            subistitua(file, txt, novo_txt)
        file.close()
    print File.ljust(70) + '[OK]'.rjust(5)

if __name__ == '__main__':
    try:
        response = urllib2.urlopen('http://www.google.com.br', timeout=1)
    except urllib2.URLError as err:
        print "No network connection "
        exit(-1)
    root = './app'
    ex = ".py"
    files = []
    os.path.walk(root, fileWalker, [ex, files])

    print '%d files found to be translated' % len(files)
    try:
        if _MAX_PEERS > 1:
            _pool = Pool(processes=_MAX_PEERS)
            result = _pool.map_async(magica, files)
            result.wait()
        else:
            result = MagicMock()
            result.successful.return_value = False
            for f in files:
                pass
                magica(f)
            result.successful.return_value = True
    except AssertionError, e:
        print e
    else:
        pass
    finally:
        if result.successful():
            print 'Translated all files'
        else:
            print 'Some files was not translated'

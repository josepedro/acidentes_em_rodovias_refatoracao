#!/usr/bin/env python
# coding: utf-8

"""
 Script to helps on translate some code's methods from
 portuguese to english.
 """


from multiprocessing import Pool
from goslate import Goslate
import fnmatch
import os
import re

_MAX_PEERS = 50


def fileWalker(ext, dirname, names):
    """
    Find the files with the correct extension
    """
    pat = "*" + ext[0]
    for f in names:
        if fnmatch.fnmatch(f, pat):
            ext[1].append(os.path.join(dirname, f))


def encontre_text(arquivo):
    """
    find on the string the works wich have '_' on it
    """
    text = open(arquivo).read()
    return re.findall(r"\w+(?<=_)\w+", text)


def traduza_palavra(txt):
    """
        Translate the word/phrase to english
    """
    if txt[0] != '_':
        txt = txt.replace('_', ' ')
    gs = Goslate()
    #txt = gs.translate(txt, 'en', gs.detect(txt))
    txt = gs.translate(txt, 'en', 'pt-br')  # garantindo idioma tupiniquim
    return txt.replace(' ', '_').lower()


def subistitua(txt, novo_txt):
    """
    should rewrite the file with the new text in the future
    """
    print '%s -> %s' % (txt, novo_txt)


def magica(File):
    """
    Thread Pool. Every single thread should play around here with
    one element from list os files
    """
    #print '\n---- File %s' % File #inviavel em multithread
    list_txt = encontre_text(File)
    for txt in list_txt:
        novo_txt = traduza_palavra(txt)
        subistitua(txt, novo_txt)

if __name__ == '__main__':
    root = './app'
    ex = ".py"
    files = []
    os.path.walk(root, fileWalker, [ex, files])
    #print files
    _pool = Pool(processes=_MAX_PEERS)
    result = _pool.map_async(magica, files[:8])
    result.wait()
    #for File, i in zip(files, range(3)):

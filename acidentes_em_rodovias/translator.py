#!/usr/bin/env python
# coding: utf-8

"""
 Script to helps on translate some code's methods from
 portuguese to english.
 """

from multiprocessing import Pool
from goslate import Goslate
import fnmatch
import logging
import os
import re

_MAX_PEERS = 30

os.remove('traducoes.log')
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
    text = file.read()
    return re.findall(r"\w+(?<=_)\w+", text)
    #return re.findall(r"\"\w+\"", text)


def traduza_palavra(txt):
    """
        Translate the word/phrase to english
    """
    if txt[0] != '_':
        txt = txt.replace('_', ' ')
    txt = txt.replace('media', 'média')
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
    text.replace(txt, novo_txt)
    file.seek(0)  # rewind
    file.write(text)


def magica(File):
    """
    Thread Pool. Every single thread should play around here with
    one element from list os files
    """
    #print '\n---- File %s' % File #inviavel em multithread
    with open(File, "r+") as file:
        list_txt = encontre_text(file)
        for txt in list_txt:
            novo_txt = traduza_palavra(txt)
            logger.info('%s -> %s [%s]' % (txt, novo_txt, File))
            #subistitua(file, txt, novo_txt)
        file.close()
    print File.ljust(70) + '[OK]'.rjust(5)

if __name__ == '__main__':
    root = './app'
    ex = ".py"
    files = []
    os.path.walk(root, fileWalker, [ex, files])

    _pool = Pool(processes=_MAX_PEERS)
    result = _pool.map_async(magica, files)
    result.wait()

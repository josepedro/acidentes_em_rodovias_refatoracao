#!/usr/bin/env python
# coding: utf-8


from goslate import Goslate
import fnmatch
import os
import re


def fileWalker(ext, dirname, names):
    '''
    checks files in names'''
    pat = "*" + ext[0]
    for f in names:
        if fnmatch.fnmatch(f, pat):
            ext[1].append(os.path.join(dirname, f))


def find_text(arquivo):
    #return raw_input('Entre com o texto a ser traduzido: ')
    #tesouros = ()
    text = open(arquivo).read()
    return re.findall(r"\w+(?<=_)\w+", text)


def traduza(txt):
    txt = txt.replace('_', ' ')
    gs = Goslate()
    txt = gs.translate(txt, 'en', gs.detect(txt))
    return txt.replace(' ', '_')


def subistitua(txt, novo_txt):
    print '%s -> %s' % (txt, novo_txt)


if __name__ == '__main__':
    root = './app'
    ex = ".py"
    files = []
    os.path.walk(root, fileWalker, [ex, files])
    #print files
    for File in files:
        print '---- File %s' % File
        list_txt = find_text(File)
        for txt in list_txt:
            novo_txt = traduza(txt)
            subistitua(txt, novo_txt)

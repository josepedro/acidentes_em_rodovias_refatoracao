#!/usr/bin/env python
# coding: utf-8

from HTMLParser import HTMLParser
from os import listdir as ls


class AllIds(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.inLink = False
        self.dataArray = []
        self.count = 0
        self.lasttag = None
        self.lastname = None
        self.lastvalue = None
        self.ids = ""

    def handle_starttag(self, tag, attrs):
        self.inLink = False
        if tag == 'div':
            for name, value in attrs:
                if name == 'id':
                    self.count += 1
                    self.inLink = True
                    self.lasttag = tag
                    self.ids += value+"\n"

    def handle_endtag(self, tag):
        if tag == "div":
            self.inlink = False

if __name__ == '__main__':
    parser = AllIds()
    fout = open("VARIABLES-HTML.md", "w")
    fout.write("#Variables in html files\n\n")

    files = ls('./app/views')
    files.remove('robots.txt')

    for file_name in files:
        parser = AllIds()
        f = open("app/views/%s" % file_name, "r")
        parser.feed(f.read())
        fout.write("###%s\n" % file_name)
        fout.write(parser.ids)
        fout.write("\n\n")

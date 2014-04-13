from HTMLParser import HTMLParser


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
	f = open("app/views/acidentes_sexo.html","r")
	fout = open("VARIABLES-HTML.md", "w")
	parser.feed(f.read())
	print parser.ids
	fout.write(parser.ids)

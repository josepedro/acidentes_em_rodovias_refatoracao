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
	fout = open("VARIABLES-HTML.md", "w")
	fout.write("#Variables in html files\n\n")

	parser = AllIds()
	f = open("app/views/acidentes_sexo.html","r")
	parser.feed(f.read())
	fout.write("###acidentes_sexo.html\n")
	fout.write(parser.ids)
	fout.write("\n\n")

	parser = AllIds()
	f = open("app/views/br_acidentes.html","r")
	parser.feed(f.read())
	fout.write("###br_acidentes.html\n")
	fout.write(parser.ids)
	fout.write("\n\n")

	parser = AllIds()
	f = open("app/views/causas_acidentes.html","r")
	parser.feed(f.read())
	fout.write("###causas_acidentes.html\n")
	fout.write(parser.ids)
	fout.write("\n\n")

	parser = AllIds()
	f = open("app/views/footer.html","r")
	parser.feed(f.read())
	fout.write("###footer.html\n")
	fout.write(parser.ids)
	fout.write("\n\n")

	parser = AllIds()
	f = open("app/views/header.html","r")
	parser.feed(f.read())
	fout.write("###header.html\n")
	fout.write(parser.ids)
	fout.write("\n\n")

	parser = AllIds()
	f = open("app/views/header.html","r")
	parser.feed(f.read())
	fout.write("###header.html\n")
	fout.write(parser.ids)
	fout.write("\n\n")


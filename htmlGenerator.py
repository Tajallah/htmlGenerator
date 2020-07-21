import string

outline = open("outline", "r").readlines()
sideBar = open("sideBar.html", "a+")
contentBlock = open("contentBlock.html", "a+")

letters = string.ascii_lowercase

#sideBar functions
def subParse(string, counter, subcounter):
    formatted = string.replace("-", "").replace("\n", "")
    formatted = "<li><a href=\"#s" + str(counter) +  letters[subcounter] + "\">" + formatted + "</a></li>\n"
    return formatted

def sideBarParse(string, counter, subcounter):
    if string[0] is not "-":
        return "<h1><a href=\"#section" + str(counter) + "\">" + string.replace("\n", "") + "</a></h1>\n"
    else:
        return subParse(string, counter, subcounter)

#contentBlock functions
def topicParse(string, counter, subcounter):
    formatted = string.replace("-", "")
    formatted = "<div id=\"s" + str(counter) +  letters[subcounter] + "\"></div><br>\n<h1>" + str(subcounter+1) + ". " + formatted.replace("\n", "") + "</h1>\n<p>[Paste Conetent Here]</p>\n\n"
    return formatted

def contentParse(string, counter, subcounter):
    if string[0] is not "-":
        return "<div id=\"section" + str(counter) + "\"></div>\n<h2>" + string.replace("\n", "") + "</h2>\n"
    else:
        return topicParse(string, counter, subcounter)

def addTitle(title):
    sideBar.write("<h3><a href =\"#top\">" + title + "</a></h3>\n<ul>\n")
    contentBlock.write("<div id=\"top\"></div><br>\n")

#navbar boilerplate
sideBar.write("<style>html{scroll-behavior: smooth;}\ndiv.fixed {position: fixed;bottom: 60;left: 20;width: 500px;}</style>\n<div id=\"sidenav\" class=\"fixed\">\n")

counter = 1
subcounter = -1
countSwitch = False
for i in range(len(outline)):
    line = outline[i]
    if line[0] is ">":
        addTitle(line)
    if line[0] is "-":
        if subcounter is -1:
            sideBar.write("<ul>\n")
        subcounter += 1
        countSwitch = True
    elif countSwitch is True and line[0] is not "-" and line[0] is not ">":
        if subcounter is not -1:
            sideBar.write("</ul>\n")
        counter += 1
        subcounter = -1
    sideBar.write(sideBarParse(line, counter, subcounter))
    contentBlock.write(contentParse(line, counter, subcounter))
sideBar.write("</ul></ul></div>")

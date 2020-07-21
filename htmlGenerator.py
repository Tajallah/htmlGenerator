outline = open("outline", "r").readlines()
sidebar = open("sidebar.html", "a+")
contentBlock = open("content.html", "a+")

subc

def subParse(string, counter):
    subcounter = 0
    formatted = string
    while string[0] is "-":
        formatted = <>

def topParse(string, counter):
    if string[0] is not "-":
        return "<div id=\"section" + str(counter) + "\">" + string + "<div>"
    else:
        subParse(string)

for line in outline

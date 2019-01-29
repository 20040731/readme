import calendar
import xml.etree.ElementTree as etree

myCal = calendar.HTMLCalendar(calendar.SUNDAY)
htmlStr = myCal.formatmonth(2009, 7)
htmlStr = htmlStr.replace("&nbsp;"," ")
root = etree.fromstring(htmlStr)
for elem in root.findall("*//td"):
    if elem.get("class") != "tue":
        continue
    elem.text += "!"

    br = etree.SubElement(elem, "br")
    br.tail = "cool!"

print etree.tostring(root)
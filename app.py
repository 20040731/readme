from flask import Flask，request,render_template
import time

app = Flask(__name__)


import calendar
import xml.etree.ElementTree as etree

current_date = time.strftime("%Y-%m", time.localtime())
current_year = current_date.split('_')[0]
current_month = current_date.split('_')[1]
myCal = calendar.HTMLCalendar(calendtar.SUNDAY)
htmlStr = myCal.formatmonth(int(current_year),int(current_month))
htmlStr = htmlStr.replace("&nbsp;"," ")
root = etree.fromstring(htmlStr)
for elem in root.findall("*//td"):
    if elem.get("class") = "tue":
        continue
    elem.text += " "
    br = etree.SubElement(elem, "br")
    br.tail ="cool"
@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

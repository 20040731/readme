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

@app.route('/input_note',method=['get','post'])
def input_note():
    user_input = request.from['note']
    with open('note.txt','a') as note_txt:
        note_txt.write(user_input + '\n')
    ipaddr = request.remote_addr

    url='http://ip.taobao.com/service/getIpInfo.php?ip=%s' % ipaddr

    url_object = urllib2.urlopen(url)

    url_contend = url_object.read()

    res = json.loads(url_contend)

    data = res['data']
    city = data['city']
    country = data['country']
    area = data['area']

    re_geo_info = '%s-%s-%s'%(country,city,area)

    return re_geo_info

@app.route('/')
def hello_world():
    return render_template('note_input.html')


if __name__ == '__main__':
    app.run()

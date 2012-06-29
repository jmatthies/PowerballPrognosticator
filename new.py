#!/usr/bin/python
from operator import itemgetter
from datetime import date
from datetime import time
import calendar
import datetime
import MySQLdb as mdb
#import sys
import cgi
import cgitb
from jon import least_common
from jon import most_common
cgitb.enable()

print "Content-type: text/html\n\n";
print "<html><head>";
print "<title>Powerball Prognosticator</title>";
print"<script src='http://code.jquery.com/jquery-latest.js'></script>"

print """
<style ="text/css">
</style>
</head><body>
<div id="container">
"""
form = cgi.FieldStorage()

dat=datetime.datetime.today()
d1=datetime.timedelta(days=1)
d2=datetime.timedelta(days=2)
if ("tdate" in form):
 a=form["tdate"].value
 d=date(int(a[:4]),int(a[6:]),int(a[4:6]))
 dat=datetime.datetime.combine(d, time())

if ("nextday" in form):
 dat=dat+datetime.timedelta(days=1)
 
dow=dat.weekday()
if (dow==2 or dow==5):
 dat=dat
elif dow==0:
 dat=dat+d2
elif dow==1:
 dat=dat+d1
elif dow==3:
 dat=dat+d2
elif dow==4:
 dat=dat+d1
elif dow==6:
 dat=dat+d2+d1
m=dat.month
d=dat.day
Mth=dat.strftime("%B")
dow=dat.weekday()
if dow==5: dow="Sat"
else: dow="Wed"

if ("priorday" in form):
 d1=datetime.timedelta(days=1)
 d2=datetime.timedelta(days=2)
 dow=dat.weekday()
 if dow==0:
  dat=dat-d1
 elif dow==1:
  dat=dat-d2-d1
 elif dow==2:
  dat=dat-d2-d2
 elif dow==3:
  dat=dat-d1
 elif dow==4:
  dat=dat-d2
 elif dow==5:
  dat=dat-d2-d1
 elif dow==6:
  dat=dat-d1
 m=dat.month
 Mth=dat.strftime("%B")
 d=dat.day
 dow=dat.weekday()
 if dow==5: dow="Sat"
 else: dow="Wed"



sep='"'
print '<form method="get">'
td=dat.strftime("%Y%d%m")
print '<input type=hidden id="tdate" name="tdate" value='+td+'>'
print "<TABLE border=1>"

nextday_button='<input type=submit name="nextday" id="nextday" value="Next Drawing" />'
priorday_button='<input type=submit name="priorday" id="priorday" value="Prior Drawing" />'
print '<TR><TH colspan=10>%s Next Drawing: (%s) %2d/%2d/%2d %s</TH></TR>' %(priorday_button,dow,dat.month,dat.day,dat.year,nextday_button)
print "</FORM>"
print"<TR>"
print '<TH class="Header" COLSPAN=5>Least Common</TH>'
print '<TH class="Header" COLSPAN=5>Most Common</TH></TR>'
print"<TR>"
ret=least_common.least_common(0,0,0,"",0)
for num,times in ret.iteritems():
 if (len(str(num))==1): num="&nbsp;"+num
 print "<TD><span class="+sep+"Number"+sep+" title='%s'>%s</span></TD>" %(times, num)

ret=most_common.most_common(0,0,0,"",0)
for num,times in ret.iteritems():
 print "<TD><span class="+sep+"Number"+sep+" span title='Used %s times'>%s</span></TD>" %(times, num)
print "</TR>\n"

print"<TR>"
print '<TH class="Header" COLSPAN=5>Least Common in '+Mth+'</TH>'
print '<TH class="Header" COLSPAN=5>Most Common in '+Mth+'</TH></TR>'
print"<TR>"

ret=least_common.least_common(m,0,0,"",0)
for num,times in ret.iteritems():
 print "<TD><span class="+sep+"Number"+sep+" span title='%s'>%s</span></TD>" %(times, num)

ret=most_common.most_common(m,0,0,"",0)
for num,times in ret.iteritems():
 print "<TD><span class="+sep+"Number"+sep+" span title='Used %s times'>%s</span></TD>" %(times, num)
print "</TR>\n"




print"<TR>"
print '<TH class="Header" COLSPAN=5>Least Common for Calendar day:%d</TH>' %(d)
print '<TH class="Header" COLSPAN=5>Most Common for Calendar day:%d</TH></TR>' %(d)
print"<TR>"
ret=least_common.least_common(0,d,0,"",0)
for num,times in ret.iteritems():
 print "<TD><span class="+sep+"Number"+sep+" span title='%s'>%s</span></TD>" %(times, num)
ret=most_common.most_common(0,d,0,"",0)
for num,times in ret.iteritems():
 print "<td><span class="+sep+"Number"+sep+" span title='Used %s times'>%s</span></TD>" %(times, num)
print "</TR>\n"

print"<TR>"
print '<TH class="Header" COLSPAN=5>Least Common for Day of Week:%s</TH>' %(dow)
print '<TH class="Header" COLSPAN=5>Most Common for Day of Week:%s</TH></TR>' %(dow)
print"<TR>"
ret=least_common.least_common(0,0,0,dow,0)
for num,times in ret.iteritems():
 print "<TD><span class="+sep+"Number"+sep+" span title='%s'>%s</span></TD>" %(times, num)
ret=most_common.most_common(0,0,0,dow,0)
for num,times in ret.iteritems():
 print "<td><span class="+sep+"Number"+sep+" span title='Used %s times'>%s</span></TD>" %(times, num)
print "</TR>\n"


print"<TR>"
print '<TH class="Header" COLSPAN=5>Least Common for %s, %d</TH>' %(Mth,d)
print '<TH class="Header" COLSPAN=5>Most Common for %s, %d</TH></TR>' %(Mth,d)
print"<TR>"
ret=least_common.least_common(m,d,0,"",0)
for num,times in ret.iteritems():
 print "<TD><span class="+sep+"Number"+sep+" span title='%s'>%s</span></TD>" %(times, num)
ret=most_common.most_common(m,d,0,"",0)
for num,times in ret.iteritems():
 print "<td><span class="'%s'" span title='Used %s times'>%s</span></TD>" %("Number",times, num)
print "</TR>\n"


print """
</body></html>


<script>
$("#least").click(function () { $(this).toggle(); });
</script>
"""

#!/usr/bin/python
from operator import itemgetter
import calendar
import datetime
import MySQLdb as mdb
#import sys
#import cgi
#import cgitb
#from jon import js
from jon import var
from jon import least_used
from jon import most_common
#js.print_js()
print "Content-type: text/html\n\n";
print "<html><head>";
print "<title>Powerball Prognosticator</title>";
print"<script src='http://code.jquery.com/jquery-latest.js'></script>"

#form = cgi.FieldStorage()
#Noun1=var.create("Noun1",0,"str")
#Noun2=var.create("Noun2",1,"str")
#Noun3=var.create("Noun3",400,"str")
#Type=var.create("Type","wb","str")

print """
<style ="text/css">
</style>
</head><body>
<div id="container">
"""
m=datetime.datetime.today().month
Mth=datetime.datetime.today().strftime("%B")
dat=datetime.datetime.today()
dow=datetime.datetime.today().weekday()
d1=datetime.timedelta(days=1)
d2=datetime.timedelta(days=2)
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
d=dat.day
dow=dat.weekday()
if dow==5: dow="Sat"
else: dow="Wed"


sep='"'
print "<TABLE border=1>"



print"<TR>"
print '<TH class="Header" COLSPAN=5>Least Common</TH>'
print '<TH class="Header" COLSPAN=5>Most Common</TH></TR>'
print"<TR>"
ret=least_used.least_used(0,0,0,"",0)
for num,times in ret.iteritems():
 if (len(str(num))==1): num="&nbsp;"+num
 print "<TD><span class="+sep+"Number"+sep+" title=%s'>%s</span></TD>" %(times, num)

ret=most_common.most_common(0,0,0,"",0)
for num,times in ret.iteritems():
 print "<TD><span class="+sep+"Number"+sep+" span title='Used %s times'>%s</span></TD>" %(times, num)
print "</TR>\n"

print"<TR>"
print '<TH class="Header" COLSPAN=5>Least Common in '+Mth+'</TH>'
print '<TH class="Header" COLSPAN=5>Most Common in '+Mth+'</TH></TR>'
print"<TR>"

ret=least_used.least_used(m,0,0,"",0)
for num,times in ret.iteritems():
 print "<TD><span class="+sep+"Number"+sep+" span title=%s'>%s</span></TD>" %(times, num)

ret=most_common.most_common(m,0,0,"",0)
for num,times in ret.iteritems():
 print "<TD><span class="+sep+"Number"+sep+" span title='Used %s times'>%s</span></TD>" %(times, num)
print "</TR>\n"




print"<TR>"
print '<TH class="Header" COLSPAN=5>Least Common for Calendar day:%d</TH>' %(d)
print '<TH class="Header" COLSPAN=5>Most Common for Calendar day:%d</TH></TR>' %(d)
print"<TR>"
ret=least_used.least_used(0,d,0,"",0)
for num,times in ret.iteritems():
 print "<TD><span class="+sep+"Number"+sep+" span title=%s'>%s</span></TD>" %(times, num)
ret=most_common.most_common(0,d,0,"",0)
for num,times in ret.iteritems():
 print "<td><span class="+sep+"Number"+sep+" span title='Used %s times'>%s</span></TD>" %(times, num)
print "</TR>\n"

print"<TR>"
print '<TH class="Header" COLSPAN=5>Least Common for Day of Week:%s</TH>' %(dow)
print '<TH class="Header" COLSPAN=5>Most Common for Day of Week:%s</TH></TR>' %(dow)
print"<TR>"
ret=least_used.least_used(0,0,0,dow,0)
for num,times in ret.iteritems():
 print "<TD><span class="+sep+"Number"+sep+" span title=%s'>%s</span></TD>" %(times, num)
ret=most_common.most_common(0,0,0,dow,0)
for num,times in ret.iteritems():
 print "<td><span class="+sep+"Number"+sep+" span title='Used %s times'>%s</span></TD>" %(times, num)
print "</TR>\n"


print"<TR>"
print '<TH class="Header" COLSPAN=5>Least Common for %s, %d</TH>' %(Mth,d)
print '<TH class="Header" COLSPAN=5>Most Common for %s, %d</TH></TR>' %(Mth,d)
print"<TR>"
ret=least_used.least_used(6,23,0,"",0)
for num,times in ret.iteritems():
 print "<TD><span class="+sep+"Number"+sep+" span title=%s'>%s</span></TD>" %(times, num)
ret=most_common.most_common(6,23,0,"",0)
for num,times in ret.iteritems():
 print "<td><span class="+sep+"Number"+sep+" span title='Used %s times'>%s</span></TD>" %(times, num)
print "</TR>\n"


print """
</body></html>


<script>
$("#least").click(function () { $(this).toggle(); });
</script>
"""

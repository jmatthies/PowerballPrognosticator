#!/usr/bin/python
from operator import itemgetter
import calendar
import MySQLdb as mdb
import sys
import cgi
import cgitb

form = cgi.FieldStorage()
sep='"'

def least_common (month,day,year,dow,jackpot):
 con = None
 
 try:
 
  con = mdb.connect('localhost', 'jmat_viewer', 'a~@DVv4-P4ma', 'jmat_pb');
  cur = con.cursor()

  Msql=""
  if (month!=0):
   Msql=" AND Month(date)=%d" %(month)
  Dsql=""
  if (day!=0):
   Dsql=" AND Day(date)=%d" %(day)
  Dowsql=""
  if (dow!=""):
   Dowsql=" AND Dow like '%"+dow+"%'"

  count={}
  Last_used={}
  for i in range(1,60):
   Ball=str(i)
   #if (Type=="wb"):
   # Main_sql='(WB1='+Ball+' or WB2='+Ball+' OR WB3='+Ball+' or WB4='+Ball+' or WB5='+Ball+')'
   #if (Type=="pb"):
   # Main_sql='PB='+Ball
   #count=sorted(count.iteritems(), key=itemgetter(1), reverse=True)
   Main_sql='(WB1='+Ball+' or WB2='+Ball+' OR WB3='+Ball+' or WB4='+Ball+' or WB5='+Ball+')'
  
   #Sql='SELECT * FROM `numbers` where '+Main_sql+' AND Prize>='+Noun2+' AND Prize<='+Noun3+Dow_sql+Months_sql+Dim_sql+" ORDER BY DATE DESC LIMIT 0,1"
   Sql='SELECT * FROM `numbers` where '+Main_sql+Msql+Dsql+Dowsql+' ORDER BY DATE DESC LIMIT 0,1'
   #print "SQL IS : ",Sql,"|"
   #print "<BR>"
   cur.execute(Sql)
   rows = cur.fetchall()
   from datetime import date
   today = date.today()
   last=0
   if cur.rowcount==0:
     last=0
     Last_used[Ball]=(last, "")

   for row in rows:
     seen=row[1]
     last=today-seen
     wb1=str(row[2])
     wb2=str(row[3])
     wb3=str(row[4])
     wb4=str(row[5])
     wb5=str(row[6])
     pb=str(row[7])
     pb='<Font color="red">'+pb+'<font>'
     dow=" ("+str(row[8])+") "
     date="%2d/%2d/%2d" %(seen.month, seen.day, seen.year) 
     prize=str(row[12])
     delta=str(row[13])
     Pb_info=date+dow+str(last)
     Last_used[Ball]=(int(last.days), Pb_info)

  ct=0
  ret={}
  for x in sorted(Last_used,key=lambda x: Last_used[x], reverse=True):
   ct=ct+1
   K=str(Last_used[x])
   L=K.split(",")
   if ct<=5:
    ret[x]=L[1][2:]
    #print "%2s: %20s" %(x,L)
    #print "%2s: %20s" %(x,L[1][2:])

    
 except mdb.Error, e:
  
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
    
 finally:    
        
    if con:    
        con.close()
 return ret 
 
 
# end function least_common





#ret=least_common(0,2,0,"",0)
#for num,since in sorted(ret.iteritems()):
# print num,since
#print
#ret=least_common(2,0,0,"",0)
#for num,since in sorted(ret.iteritems()):
# print num,since
#ret=least_common(0,0,0,"Wed",0)
#for num,since in sorted(ret.iteritems()):
# print num,since

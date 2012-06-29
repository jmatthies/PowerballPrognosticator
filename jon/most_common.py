#!/usr/bin/python
from operator import itemgetter
import calendar
import MySQLdb as mdb
import sys
import cgi
import cgitb

form = cgi.FieldStorage()
sep='"'

def most_common (month,day,year,dow,jackpot):
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
   Main_sql='(WB1='+Ball+' or WB2='+Ball+' OR WB3='+Ball+' or WB4='+Ball+' or WB5='+Ball+')'
  
   Sql='SELECT COUNT(*) FROM `numbers` where '+Main_sql+Msql+Dsql+Dowsql
   #print "SQL IS : ",Sql,"|"
   #print "<BR>"
   cur.execute(Sql)
   rows = cur.fetchall()
   if cur.rowcount==0:
     count[Ball]=0
   for row in rows:
    count[Ball]=row[0]

  # end for loop
  count=sorted(count.iteritems(), key=itemgetter(1), reverse=True)
  ct=0
  ret={}
  for j,v in count:
   ct=ct+1
   Pbcount=str(v)
   Pbnum=str(j)
   if ct<=5:
    #print Pbnum+" Found "+Pbcount+" times"
    ret[Pbnum]=Pbcount

    
 except mdb.Error, e:
  
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
    
 finally:    
        
    if con:    
        con.close()
 return ret 
 
 
# end function most_common





#ret=most_common(0,2,0,"",0)
#for num,count in sorted(ret.iteritems()):
# print num,count
#print
#ret=most_common(2,0,0,"",0)
#for num,count in sorted(ret.iteritems()):
# print num,count
#print
#ret=most_common(0,0,0,"Wed",0)
#for num,count in sorted(ret.iteritems()):
# print num,count
#print

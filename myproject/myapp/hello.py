#


from datetime import date, datetime, timedelta
from django.utils import formats

f_date = date(2018, 2, 21)
l_date = date(2018, 7, 11)

delta = l_date - f_date
print(delta.days+2)

act_level = [1,1.12,1.27,1.54]
b = 152*act_level[0]
print(b)
#date_format = "%m/%d/%Y"
#date_joined = datetime.now().date()
#print(date_joined)
#start_date = date(2018, 2, 2)
#start_date.strftime('%B %d,%Y')
#x = datetime.strptime(start_date, '%B %d,%Y')
#print(start_date)
#new_date = start_date.date()
#print(new_date)
#for i in range(0,32):
  #  f_date = f_date + timedelta(days=1)
 #   print(f_date)
 #   if(f_date==date_joined):
   #     print("found")
  #      break

#a = date_joined[1:4]
#k=date_joined.strftime('%Y/%m/%d')
#a = k[0:4]
#b = k[5:7]
#c= k[8:10]
#l_date = date(int(a), int(b), int(c))
#print((f_date-l_date).days)
#print(a,' ',b,' ',c)

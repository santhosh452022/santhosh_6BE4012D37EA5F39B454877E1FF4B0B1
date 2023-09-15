year=int(input("Enter the Number:"))
  
 
if(year % 400==0and year % 100!=0) or year %4==0:
  
  print("Given year is Leap year")
else:
  
  print("Given year is not a Leap year")
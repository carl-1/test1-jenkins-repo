#!/usr/bin/python
import time
import webbrowser
import os
import turtle
import calc


def getTranStr(s1):
	s2 = s1.translate(str.maketrans('','','0123456789'))
	return s2
	
def add_nos(n1, n2):
	sum = n1 - n2
	print("The sum of the nos is : ",calc.mul(n1, n2))
	

def call_Me() :	#define functions at the start, before it can be used in your program
	print("Calling the first function...")
	file_list = os.listdir() 	#by default, take the current dir for listing, path can also be passed
	print(file_list)
	for file_name in file_list :
		print(file_name)
		t_fname = file_name.translate(str.maketrans('','',"0123456789"))
		print(t_fname)
		#os.rename(file_name, t_fname)
		
def draw_square():
  scr = turtle.Screen()
  scr.bgcolor("red")
  draw = turtle.Turtle()
  #change attrs of the turtle
  draw.shape("turtle")
  draw.color("blue")
  draw.speed(2)
  #change directions
  draw.forward(100)
  draw.right(90) # turn right 90 deg.
  draw.forward(100)
  draw.right(90)
  draw.forward(100)
  draw.right(90)
  draw.forward(100)
  draw_circle = turtle.Turtle()
  draw_circle.shape("arrow")
  draw_circle.color("green")
  draw_circle.circle(100)
  scr.exitonclick()
  print("Done with square drawing...")
  
print("Starting program at : "+time.ctime())
#time.sleep(10)
#webbrowser.open("https://www.youtube.com/watch?v=YJC6ldI3hWk")

count = 3
while(count > 0):	#ident the code below the loop start point to indicate the following code belongs to the loop struct
	print("Calling the loop the time..count")
	count = count - 1
	
print("End of loop..")
call_Me()
#draw_square()
add_nos(n2=2,n1=3)
ret_val = getTranStr("ajshj18900")
print("The translated string is : ",ret_val)

for i in range(3):#0,1,2 for range(1,3) = 1,2 => i,i+1,i+2...j-1
  print("For looping using index",i, "using range ",3)

raw_input("Press any key to exit..")
print("Done with program execution..")
# Modifying this comment to test post-commit build action of the Jenkins build
print ("Attempting another try to get the SCm polling working")


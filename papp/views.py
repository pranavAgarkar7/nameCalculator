from django.shortcuts import render, redirect
from django.http import HttpResponse
from papp.models import user_data
import socket
import datetime
import pytz
# Create your views here.

# Universal values here.
a=1
b=2
c=3
d=4
e=5
f=6
g=7
h=8
i=9
j=10
k=11
l=12
m=13
n=14
o=15
p=16
q=17
r=18
s=19
t=20
u=21
v=22
w=23
x=24
y=25
z=26

def index(request):



	activelink = 'active'
	return render(request, 'papp/index.html')

def reasult(request):
	val1 = request.GET["name"]
	############## Addition ################
	l = val1.lower()
	n = [ord(x) - 96 for x in l]
	print(n)

	#Initialize array
	arr = n;
	sum = 0;

	#Loop through the array to calculate sum of elements
	for i in range(0, len(arr)):
	   sum = sum + arr[i];

	print("Sum of all the elements of an array: " + str(sum));

	############# Multiplaction ###########
	m = val1.lower()
	o = [ord(x) - 96 for x in m]
	print(o)

	arr = n;
	into = 1;

	for i in range(0, len(arr)):
		into = into * arr[i];

	print("Multiplaction of all the elements of an array: " + str(into));

	current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))

	hostname = socket.gethostname()
	IPAddr = socket.gethostbyname(hostname)

	ins = user_data(name=val1, Ip=IPAddr, host_name = hostname, dateTime1=current_time)
	ins.save()

	return render(request, 'papp/index.html', {'reasult2':sum, 'result3':into, 'Value':val1})
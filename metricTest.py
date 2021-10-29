#CODE SOURCE: SOFTWARE ARCHITECTURE WITH PYTHON 

"""
2 Module metricTest.py
3
4 Metric example - Module which is used as a testbed for static
checkers.
5 This is a mix of different functions and classes doing
different things.
6
7 """
8 import random
9
10 def fn(x, y):
11 """ A function which performs a sum """
12 return x + y
13
14 def find_optimal_route_to_my_office_from_home(start_time,
15 expected_time,
16 favorite_route='SBS1K',
17 favorite_option='bus'):
18
19
20 d = (expected_time – start_time).total_seconds()/60.0
21
22 if d<=30:
23 return 'car'
24
25 # If d>30 but <45, first drive then take metro
26 if d>30 and d<45:
27 return ('car', 'metro')
28
29 # If d>45 there are a combination of optionsWriting Modifiable and Readable Code
[ 68 ]
30 if d>45:
31 if d<60:
32 # First volvo,then connecting bus
33 return ('bus:335E','bus:connector')
34 elif d>80:
35 # Might as well go by normal bus
36 return random.choice(('bus:330','bus:331',':'.
join((favorite_option,
37 favorite_route))))
38 elif d>90:
39 # Relax and choose favorite route
40 return ':'.join((favorite_option,
41 favorite_route))
42
43
44 class C(object):
45 """ A class which does almost nothing """
46
47 def __init__(self, x,y):
48 self.x = x
49 self.y = y
50
51 def f(self):
52 pass
53
54 def g(self, x, y):
55
56 if self.x>x:
57 return self.x+self.y
58 elif x>self.x:
59 return x+ self.y
60
61 class D(C):
62 """ D class """
63
64 def __init__(self, x):
65 self.x = x
66
67 def f(self, x,y):
68 if x>y:
69 return x-y
70 else:Chapter 2
[ 69 ]
71 return x+y
72
73 def g(self, y):
74
75 if self.x>y:
76 return self.x+y
77 else:
78 return y-self.x

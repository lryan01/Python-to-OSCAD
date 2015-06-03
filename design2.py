from pyopenscad import *
import math


def design():
	cylinder = str(Cylinder(150, 20))
	sphere = Sphere(2)	
	code = ''
	list1 = cylinder
	list2 = ''
	color = ('color("darkviolet")', 'color("DeepPink")', 'color("orchid")', 'color("turquoise")')
	
	for i in range(1,38):
		list2 += color[0]
		list2 += translate(sphere, 20*math.cos(math.radians(i*10)), 20*math.sin(math.radians(i*10)), i*4)
		list2 += color[1]
		list2 += rotate(120, 0, 0, 1)
		list2 += translate(sphere, 20*math.cos(math.radians(i*10)), 20*math.sin(math.radians(i*10)), i*4)
		if i % 2 == 1:
			list2 += color[2]
			list2 += rotate(180, 0, 0, 1)
			list2 += translate(sphere, 20*math.cos(math.radians(i*10)), 20*math.sin(math.radians(i*10)), i*4)
		else: 
			list2 += color[3]
			list2 += rotate(300, 0, 0, 1)
			list2 += translate(sphere, 20*math.cos(math.radians(i*10)), 20*math.sin(math.radians(i*10)), i*4)
			
	code += list2
	
	for i in range(1,38):
		list1 += rotate(60, 0, 0, 1) 
		list1 += translate(sphere, 20*math.cos(math.radians(i*10)), 20*math.sin(math.radians(i*10)), i*4)
		list1 += rotate(240, 0, 0, 1)
		list1 += translate(sphere, 20*math.cos(math.radians(i*10)), 20*math.sin(math.radians(i*10)), i*4)
	code += difference(list1)
	
	return code
		
design = design()
	
save('design.scad', design)
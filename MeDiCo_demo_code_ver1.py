
# Andrew Stretton, 19-Oct-17 for Team MeDiCo 
# Biomaker Challenge 2017, University of Cambridge
# This code is released under the [MIT License](http://opensource.org/licenses/MIT).

from PIL import Image				# for JPG cropping
from scipy import misc				# for image/array manipulation
import matplotlib.pyplot as plt		# for 'plotting' the arrays, as images
import numpy as np					# for doing some maths on the arrays
from datetime import datetime		# for calculating the time script runs
from skimage import color			# from sci-kit image, for RGBtoLAB conv.
from colormath.color_objects import LabColor		#correct format for delta_E calc
from colormath.color_diff import delta_e_cie2000	#calculates delta_E (color dif)
startTime = datetime.now()

	# IMAGE CROPPING-----------------------------------------------------------
img = Image.open("imageN1.jpg")		# loads camera image, NB image taken on phone, then resized	
testIMG = img.crop((270, 330, 1650, 530))		# crops image to test strip only, (x1,y1,x2,y2) ie. TL & BR coords
testIMG.save("testIMG.jpg")

	# COORIDINATES-----------------------------------------------------------
coord_sec1 = (0,0,120,200)		# manually enter each ROI
coord_sec2 = (180,0,300,200)
coord_sec3 = (360,0,480,200)
coord_sec4 = (540,0,660,200)
coord_sec5 = (720,0,840,200)
coord_sec6 = (900,0,1020,200)	# standard test strip is light
coord_sec7 = (1080,0,1200,200)	# standard test strip is light
coord_sec8 = (1240,0,1380,200)

sec1 = testIMG.crop(coord_sec1)		# possible to use dic of coords and loop???
sec1.save("sec1.jpg")
sec2 = testIMG.crop(coord_sec2)			
sec2.save("sec2.jpg")
sec3 = testIMG.crop(coord_sec3)	
sec3.save("sec3.jpg")
sec4 = testIMG.crop(coord_sec4)	
sec4.save("sec4.jpg")
sec5 = testIMG.crop(coord_sec5)
sec5.save("sec5.jpg")
sec6 = testIMG.crop(coord_sec6)
sec6.save("sec6.jpg")
sec7 = testIMG.crop(coord_sec7)	
sec7.save("sec7.jpg")
sec8 = testIMG.crop(coord_sec8)
sec8.save("sec8.jpg")

number_sec = 8						# number of sections to image
number_slices = 3					# number of slices, one for each RGB

a = range(1,number_sec + 1)
b = range(0, number_slices)
RGB = []							# empty list to store RGB values

with open('RGBvalues.txt','w') as file1:	# opens file to store RGBs
	for each in a:							# calculate RGB values & add to list
		jpg = 'sec' + str(each) + '.jpg'
		png = 'sec' + str(each) + '.png'
		misc.imsave(png, misc.imread(jpg))
		q = misc.imread(png)
		R = int(np.average(q[:,:,0]))
		G = int(np.average(q[:,:,1]))
		B = int(np.average(q[:,:,2]))
		R = float(R)/255					#convert to decimal
		G = float(G)/255
		B = float(B)/255
		RGB.append([[[R, G, B]]])			#save as list, need [[[]]] for lab conversion - treats as one pixel image
		line = str(RGB[each-1])
		print>>file1, line
file1.close()

LABvalues = []
with open('LABvalues.txt','w') as file2:
	count2 = 0
	for each in RGB:
		lab = color.rgb2lab(each)
#		print lab
		string_lab = str(lab)
		L_colour = float(string_lab[4:15])		#converts strings to floats
		A_colour = float(string_lab[17:28])		#NB: range -128 to 128 ***
		B_colour = float(string_lab[29:41])		#NB: range -128 to 128 ***
#		print L_colour, A_colour, B_colour			
		LABvalues.append((L_colour,A_colour,B_colour))	#add them to a new list
		line2 = str(LABvalues[count2])
		print>>file2, line2						#prints LAB info to new file
		count2 += 1
file2.close()						# *** potential issue here with '-' signs

LABcolors_TEST = []						#list to store L,A,Bs in format for deltaE
for each in LABvalues:
#	print each[0],each[1],each[2]
	LABcolors_TEST.append(LabColor(each[0],each[1],each[2]))


# colour standards here **********************************************************

#reverse of blank strip
LABcolors_REF1 = [LabColor(lab_l=77.82448837,lab_a=-2.19873635,lab_b=-5.30221706), LabColor(lab_l=84.87175287,lab_a=-2.63715365,lab_b=6.30671387), LabColor(lab_l=85.34899922,lab_a=-1.58271685,lab_b=2.22919077), LabColor(lab_l=83.11182915,lab_a=-8.6988241,lab_b=33.77118438), LabColor(lab_l=80.10215908,lab_a=-7.89989385,lab_b=37.96563966), LabColor(lab_l=73.98526892,lab_a=-7.45339543,lab_b=37.03927342), LabColor(lab_l=58.14674154,lab_a=12.42151923,lab_b=21.32645648), LabColor(lab_l=65.82234803,lab_a=10.10882947,lab_b=-14.55537625)]

#same as test strip
LABcolors_REF2 = [LabColor(lab_l=64.76015657,lab_a=10.57496607,lab_b=-15.6232239), LabColor(lab_l=58.14674154,lab_a=12.42151923,lab_b=21.32645648), LabColor(lab_l=73.97087807,lab_a=-7.56102574,lab_b=37.53439651), LabColor(lab_l=80.08754513,lab_a=-8.00913929,lab_b=38.45517544), LabColor(lab_l=83.11182915,lab_a=-8.6988241,lab_b=33.77118438), LabColor(lab_l=85.34899922,lab_a=-1.58271685,lab_b=2.22919077), LabColor(lab_l=84.61465654,lab_a=-2.11837812,lab_b=5.93634302), LabColor(lab_l=77.89719469,lab_a=-1.86619421,lab_b=-5.18668098)]

LABcolors_REF3 = []					#this segment reverses the order of REF2
count = 7
for each in LABcolors_REF2:
	LABcolors_REF3.append(LABcolors_REF2[count])
	count -= 1


# colour matching here **********************************************************
print
print 'Team MeDiCo | pH test strip interpreter'
print

dict_deviations = {}							#creates dic, color dif from standards

REF1_total = 0
for each in a:
	delta_e = delta_e_cie2000(LABcolors_TEST[each-1],LABcolors_REF1[each-1])	
#	print delta_e
	REF1_total = REF1_total + delta_e
REF1_deviation = REF1_total/len(a)
dict_deviations['pH_a'] = REF1_deviation		#adds to dictionary
print 'pH ref A:' , 'test strip deviation =', REF1_deviation

REF2_total = 0
for each in a:
	delta_e = delta_e_cie2000(LABcolors_TEST[each-1],LABcolors_REF2[each-1])	
#	print delta_e
	REF2_total = REF2_total + delta_e
REF2_deviation = REF2_total/len(a)
dict_deviations['pH_b'] = REF2_deviation		#adds to dictionary
print 'pH ref B:' , 'test strip deviation =', REF2_deviation

REF3_total = 0
for each in a:
	delta_e = delta_e_cie2000(LABcolors_TEST[each-1],LABcolors_REF3[each-1])	
#	print delta_e
	REF3_total = REF3_total + delta_e
REF3_deviation = REF3_total/len(a)
dict_deviations['pH_c'] = REF3_deviation		#adds to dictionary
print 'pH ref C:' , 'test strip deviation =', REF3_deviation
print
#print 'pH dictionary:' , dict_deviations

import operator
sorted_dict = sorted(dict_deviations.items(), key=operator.itemgetter(1))
sorted_dict_low = sorted_dict[0]
sample_pH = sorted_dict_low[0]

print '****** RESULT ******'
print 'test strip pH =',sample_pH
print 
print
print "run time: ", datetime.now() - startTime	#print time taken
print

#!/usr/bin/env python
import time
from lib_robotis import *
dyn = USB2Dynamixel_Device('/dev/ttyUSB0')
r1 = Robotis_Servo( dyn, 1 )
r2 = Robotis_Servo( dyn, 2)
r3 = Robotis_Servo( dyn, 3)
r4 = Robotis_Servo( dyn, 4)
r5 = Robotis_Servo( dyn, 5)
r6 = Robotis_Servo( dyn, 6)
r7 = Robotis_Servo( dyn, 7)
r8 = Robotis_Servo( dyn, 8)
r9 = Robotis_Servo( dyn, 9)
r10 = Robotis_Servo( dyn, 10)
r11 = Robotis_Servo( dyn, 11)
r12 = Robotis_Servo( dyn, 12)
r13 = Robotis_Servo( dyn, 13)
r14 = Robotis_Servo( dyn, 14)
r15 = Robotis_Servo( dyn, 15)
r16 = Robotis_Servo( dyn, 16)
r17 = Robotis_Servo( dyn, 17)
r18 = Robotis_Servo( dyn, 18)


r1.disable_torque()
r2.disable_torque()
r3.disable_torque()
r4.disable_torque()
r5.disable_torque()
r6.disable_torque()
r7.enable_torque()
r8.enable_torque()
r9.enable_torque()
r10.enable_torque()
r11.enable_torque()
r12.enable_torque()
r13.enable_torque()
r14.enable_torque()
r15.enable_torque()
r16.enable_torque()
r17.enable_torque()
r18.enable_torque()

k = input()
time.sleep(3)
print "start"
i = 0 
f1 = open('datastorebioloidparabola11.txt','w')

while(i<800):
	ang4 = r4.read_angle()
	ang6 = r6.read_angle()
	f1.write('%f, %f\n' % (ang4, ang6))	
#	print i	
#	time.sleep(0.6)
	i = i + 1
	
f1.close()
print 'done 1'
k = input()
time.sleep(3)
print "start"
i = 0 
f1 = open('datastorebioloidparabola12.txt','w')

while(i<800):
	ang4 = r4.read_angle()
	ang6 = r6.read_angle()
	f1.write('%f, %f\n' % (ang4, ang6))	
#	print i	
#	time.sleep(0.6)
	i = i + 1
	
f1.close()
print 'done 1'
k = input()
time.sleep(3)
print "start"
i = 0 
f1 = open('datastorebioloidparabola13.txt','w')

while(i<800):
	ang4 = r4.read_angle()
	ang6 = r6.read_angle()
	f1.write('%f, %f\n' % (ang4, ang6))	
#	print i	
#	time.sleep(0.6)
	i = i + 1
	
f1.close()
print 'done 1'
k = input()
time.sleep(3)
print "start"
i = 0 
f1 = open('datastorebioloidparabola14.txt','w')

while(i<800):
	ang4 = r4.read_angle()
	ang6 = r6.read_angle()
	f1.write('%f, %f\n' % (ang4, ang6))	
#	print i	
#	time.sleep(0.6)
	i = i + 1
	
f1.close()
print 'done 1'
k = input()
time.sleep(3)
print "start"
i = 0 
f1 = open('datastorebioloidparabola15.txt','w')

while(i<800):
	ang4 = r4.read_angle()
	ang6 = r6.read_angle()
	f1.write('%f, %f\n' % (ang4, ang6))	
#	print i	
#	time.sleep(0.6)
	i = i + 1
	
f1.close()
print 'done 1'
k = input()
time.sleep(3)
print "start"
i = 0 
f1 = open('datastorebioloidparabola16.txt','w')

while(i<800):
	ang4 = r4.read_angle()
	ang6 = r6.read_angle()
	f1.write('%f, %f\n' % (ang4, ang6))	
#	print i	
#	time.sleep(0.6)
	i = i + 1
	
f1.close()
print 'done 1'
k = input()
time.sleep(3)
print "start"
i = 0 
f1 = open('datastorebioloidparabola17.txt','w')

while(i<800):
	ang4 = r4.read_angle()
	ang6 = r6.read_angle()
	f1.write('%f, %f\n' % (ang4, ang6))	
#	print i	
#	time.sleep(0.5)
	i = i + 1
	
f1.close()
print 'done 1'



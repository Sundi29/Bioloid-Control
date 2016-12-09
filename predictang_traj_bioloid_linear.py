from lib_robotis import *
from sympy import *
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

f1 = open('predictangleft.txt', 'r');
f2 = open('predictangright.txt', 'r');
r4.move_angle(0.70563116, blocking = True)
r6.move_angle(1.518641, blocking = True)
r3.move_angle(-0.434628, blocking = True)
r5.move_angle(-1.50330117, blocking = True)
print 'start'
i = 0
for line in f1:
	line1 = line[0:(len(line)-1)]
	line1 = line1.split(', ')
	line1 = [float(line1[0]), float(line1[1])]
	if(len(line1) == 2):
		if(i>0):
			Xn11 = Xn11.row_insert(i,Matrix([[float(line1[0]), float(line1[1])]]))
		else:
			Xn11 = Matrix([[float(line1[0]), float(line1[1])]])
		i = i + 1
	
i = 0
for line in f2:
	line1 = line[0:(len(line)-1)]
	line1 = line1.split(', ')
	line1 = [float(line1[0]), float(line1[1])]
	if(len(line1) == 2):
		if(i>0):
			Xn21 = Xn21.row_insert(i,Matrix([[float(line1[0]), float(line1[1])]]))
		else:
			Xn21 = Matrix([[float(line1[0]), float(line1[1])]])
		i = i + 1

i = 0
maxdata = max(len(Xn11.col(0)), len(Xn21.col(0)))
while(i<maxdata):
	if(i<len(Xn11.col(0))):
		r4.move_angle(Xn11[i,0], blocking = True)
		r6.move_angle(Xn11[i,1], blocking = False)
	if(i<len(Xn21.col(0))):
		r3.move_angle(Xn21[i,0], blocking = False)
		r5.move_angle(Xn21[i,1], blocking = True)
	i = i + 1
	
r6.move_angle(math.radians(87.5773), blocking = False)
r5.move_angle(math.radians(-97.2625), blocking = False)	
f1.close()


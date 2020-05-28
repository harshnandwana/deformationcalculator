import numpy as np
import matplotlib.pyplot as pyp
from anastruct import SystemElements

print("Created by Harsh Nandwana, Arpit Chechani, Varnit Kashyap")
print("ORCiD ID : https://orcid.org/0000-0002-4877-545X ")
f = open(r"material data.txt", "a+")
print("Material selection")
g=2
p=1


def dw():
	fname = "material data.txt"
	lst=list()
	n=list()
	z=list()
	y=list()
	n1=[]
	z1=[]
	y1=[]
	fh = open(fname)
	for line in fh:
		line.rstrip()
		lst=line.split()
		n.append(lst[0])
		z.append(lst[2])
		y.append(lst[3])
	for words in n:
		n1.append(words)
	for numb in z:
		numb=float(numb)
		z1.append(numb)
	for values in y:
		values=float(values)
		y1.append(values)
	print(y1)
	fig, ax = pyp.subplots()
	ax.scatter(z1, y1)
	for i, txt in enumerate(n1):
	    ax.annotate(txt, (z1[i], y1[i]))
	#pyp.figure("Deformation vs Mass")
	pyp.suptitle("credit ORCiD ID: https://orcid.org/0000-0002-4877-545X", fontsize=8)
	pyp.ylabel('deformation in mm')
	pyp.xlabel('mass g')
	pyp.savefig('deformation vs mass.png')
	pyp.show()
#################################################################
while g!=0:
	x=np.arange(210,250,10)
	x2=np.arange(0,285,10)
	x3=np.arange(0,285,10)
	mn=input("Enter material name		>//")
	E=input("Enter value of E(young's modulus) in MPa		>//")
	E=int(E)
	#E=215000
	L=285
	Fu=10.37
	dens=input("Enter density in kg/m3		>//")
	dens=float(dens)
	dens=dens/1000000
	ss = SystemElements(EA=E*(3.14*(20**2-18**2)/4), EI=2700*E)
	I=2700
	Fd=6
	i=0
	j=0
	y=(Fu/(E*I))*((x2**2)/6)*(3*L-x2)
	z=(Fd/(E*I))*((x2**2)/6)*(3*L-x2)
	y2=(-1)*(Fu/(E*I))*((x**2)/6)*(3*L-x)

	V=3.14*(20**2-18**2)*350/4

	pyp.plot(x2,(z-y))
	mass=V*dens
	#pyp.plot(x2,(z-y+10))#x,y
	#pyp.plot(x2,(z-y-10))
	#pyp.plot(x2,y2)
	pyp.xlabel('length in mm')
	pyp.ylabel('deformation in mm')
	mass=str(mass)
	x='Deformation of '+ mn
	x=x+' having mass ='+mass+' gram'
	#pyp.figure("Length vs deformation curve")
	pyp.title(x)
	pyp.suptitle("credit ORCiD ID: https://orcid.org/0000-0002-4877-545X", fontsize=8)
	#pyp.title(mass)
	#pyp.legend()
	mns=mn+'.png'
	pyp.savefig(mns)
	pyp.show()
	#########################################
	D=((Fu*(250**3)/(3*E*I))+(Fu*(250**2)*(285-250))/(2*E*I))-((Fd*(210**3)/(3*E*I))+(Fd*(210**2)*(285-210))/(2*E*I))
	#print("deformation>>//			",D,"mm")
	#####################################
	if p==1:
		St=input("Do you want to see structure (Y/N)		>//")
		Rn=input("Do you want to see Reactions (Y/N)		>//")
		ss.add_element(location= [210, 0])
		ss.add_element(location=[[210, 0], [250, 0]])
		ss.add_element(location=[[250, 0], [285, 0]])
		ss.add_support_fixed(node_id=1)
		ss.point_load(Fy=-6,Fx=-7, node_id=2)
		ss.point_load(Fy=10.37, node_id=3)
		ss.solve()
		if St=='Y' or St=='y':
			ss.show_structure()
			pyp.savefig('Structure.png')
		if Rn=='Y' or Rn=='y':
			ss.show_reaction_force()
			pyp.savefig('Reactions.png')

	#ss.show_displacement()
	E=str(E)
	D=str(D)
	k=mn+"  "+E+"  "+mass+" "+D+"\n"
	f.write(k)
	f.close()
	#print(len(z))
	#print('mass=',mass)
	grdw=input("if you want deformation vs mass graph then press (Y/N)		>//")
	if grdw=="Y" or grdw=="y":
		dw()
	p=p+1
	g=input("enter 0 to stop else press any other number		>//")
	g=int(g)
#############%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

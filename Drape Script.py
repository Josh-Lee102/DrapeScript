import Rhino
import scriptcontext
import rhinoscriptsyntax as rs
import time
    
#print("Make Sure Your Model Is Centered")
#print("Also Make Sure You Select the Top View (Press Anywhere in the Window)")
#print("Press the 'Esc' Key When You Are Done") 
#time.sleep(3600)

#Create Point in the Center of Body
vc1 = "_VolumeCentroid"
rs.Command(vc1, True)

#Move Body To Origin
def MoveOne():
    a ="Vertical=No"
    move1 = "_Move {0}".format(a)
    rs.Command(move1, True)
MoveOne()

#This step is to make sure the model is centered in Rhino ^

#Set View to Top
def SetViewOne():
    a ="CPlane"
    b ="Top"
    sv1 = "_SetView {0} {1}".format(a,b)
    rs.Command(sv1, True)
SetViewOne()

print("We are draping over the model to make sure we get that curve in the middle of the mouth")
time.sleep(5)

def DrapeOne():
    # drape options
    a = "AutoSpacing=No"
    b = "U"
    c = "8"
    d = "V"
    e = "8"
    #f = "AutoDetectMaxDepth=No"
    # 3d points
    #pt0 = Rhino.Geometry.Point3d(-60,-60,0)
    #pt1 = Rhino.Geometry.Point3d(50,50,0)
    # command
    cmd = "_Drape {0} {1} {2} {3} {4}".format(a,b,c,d,e)
    result = rs.Command(cmd, True)
    if result:
        drape_srf = rs.LastCreatedObjects(select=True)[0]
    else:
        print "No result"
    
DrapeOne()

#Create the first low resolution drape in order to get a nice curve ^

#Surface To Mesh
m1 = "_Mesh"
rs.Command(m1, True)

#Delete Surface
d1 = "_Delete"
rs.Command(d1, True)

print("We are moving the drape we just created so we can get the curve in the middle.")
time.sleep(4)

#Select Drape
s1 = "_Select"
rs.Command(s1, True)

#Move Drape To Align Surfaces
def MoveTwo():
    a = "Vertical = Yes"
    move2 = "_Move {0}".format(a)
    rs.Command(move2, True)
MoveTwo()

print("Draw a line around the middle part so that the only part remaining is the middle.")
time.sleep(3)

#Align the drape with the original model to get the curve in the middle ^

#Polyline on Mesh
plm1 = "_PolylineOnMesh"
rs.Command(plm1, True)

#Draw a line on the first drape to trim it ^

#Clear Selection
sn1 = "_SelNone"
rs.Command(sn1,True)

print("Hide the Original Model")
time.sleep(1)

#Hide Original Model
h1 = "_Hide"
rs.Command(h1, True)

#Mesh Split
ms1 = "MeshSplit"
rs.Command(ms1, True)

#Clear Selection
sn2 = "_SelNone"
rs.Command(sn2,True)

print("Delete the border")
time.sleep(1)

#Select Original Body
s2 = "_Select"
rs.Command(s2, True)

#Delete Surface
d2 = "_Delete"
rs.Command(d2, True)

#Delete the other part outer part of the drape ^

#Show Original Body
sh1 = "_Show"
rs.Command(sh1, True)

#Set View to Top
def SetViewTwo():
    a ="CPlane"
    b ="Top"
    sv2 = "_SetView {0} {1}".format(a,b)
    rs.Command(sv2, True)
SetViewTwo()

print("We are doing another drape over the entire model to get the full shape.")
time.sleep(3)

def DrapeTwo():
    # drape options
    a = "AutoSpacing=No"
    b = "U"
    c = "70"
    d = "V"
    e = "70"
    #f = "AutoDetectMaxDepth=No"
    # 3d points
    #pt0 = Rhino.Geometry.Point3d(-60,-100,0)
    #pt1 = Rhino.Geometry.Point3d(100,100,0)
    # command
    cmd = "_Drape {0} {1} {2} {3} {4}".format(a,b,c,d,e)
    result = rs.Command(cmd, True)
    if result:
        drape_srf = rs.LastCreatedObjects(select=True)[0]
    else:
        print "No result"
    
DrapeTwo()

#Another Drape except this one is higher resolution so that it can capture the shape of the teeth ^

#Surface To Mesh
m2 = "_Mesh"
rs.Command(m2, True)

#Move Drape To Align Surfaces With Gumball
#def MoveTwo():
    #a = "Vertical = Yes"
    #move1 = "_Move {0}".format(a)
    #rs.Command(move1, True)
#MoveTwo()

#Clear Selection
sn3 = "_SelNone"
rs.Command(sn3,True)

#Select Original Body
#s3 = "_Select"
#rs.Command(s3, True)

#Delete Surface
#d3 = "_Delete"
#rs.Command(d3, True)

#Hide Original Model + 1st Drape
h2 = "_Hide"
rs.Command(h2, True)

#Polyline on Mesh
plm2 = "_PolylineOnMesh"
rs.Command(plm2, True)

#Draw a line on the mesh to trim the 2nd drape ^ 

#Clear Selection
sn4 = "_SelNone"
rs.Command(sn4,True)

#Select Original Body
s3 = "_Select"
rs.Command(s3, True)

#Delete Surface
d3 = "_Delete"
rs.Command(d3, True)

#Delete the mesh (not the other body) (i'm not sure why mesh split doesn't work on the mesh but this is the only way I could get it to work ^

#Mesh Split
ms2 = "_MeshSplit"
rs.Command(ms2, True)

#Clear Selection
sn5 = "_SelNone"
rs.Command(sn5,True)

#Select Original Body
s4 = "_Select"
rs.Command(s4, True)

#Delete Surface
d4 = "_Delete"
rs.Command(d4, True)

#Delete the outer part of the mesh ^

#Offset Mesh 
#by 2mm (Or By However Much You Want the Thickness to be) 
#(Only Stay in Positive Numbers)
om1 = "_OffsetMesh"
rs.Command(om1, True)

#Show Original Body
s2 = "_Show"
rs.Command(s2, True)

#Set View to Top
def SetViewThree():
    a ="World"
    b ="Perspective"
    sv3 = "_SetView {0} {1}".format(a,b)
    rs.Command(sv3, True)
SetViewThree()

#Show only in Perspective
p1 = "_MaxViewPort"
rs.Command(p1, True)

#Set the view to full screen perspective view in order to view the model 
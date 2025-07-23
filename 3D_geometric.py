import numpy
def translationMatrix(tx=0, ty=0, tz=0):
    return numpy.matrix([[1,0,0,tx],
    [0,1,0,ty],
    [0,0,1,tz],
    [0,0,0,1 ]])
matrix=translationMatrix(1,1,1)
print("translation matrix \n",matrix)

def rotationMatrix(degree):
    theta = numpy.radians(degree)
    c,s=numpy.cos(theta),numpy.sin(theta)
    return numpy.matrix([[1,0,0,0],
    [0,c,-s,0],
    [0,s,c,0],
    [0,0,0,1]])
    matrix=rotationMatrix(30)
print(" 3d rotation matrix for rotating about y axis \n",matrix)

def rotationMatrix(degree):
    theta = numpy.radians(degree)
    c,s=numpy.cos(theta),numpy.sin(theta)
    return numpy.matrix([[c,-s,0,0],
    [s,c,0,0],
    [0,0,1,0],
    [0,0,0,1]])
matrix=rotationMatrix(30)
print("3d rotation matrix for rotating about z axis\n",matrix)
import numpy

def scalingMatrix(sx=1, sy=1, sz=1):
    return numpy.matrix([
        [sx, 0,  0,  0],
        [0,  sy, 0,  0],
        [0,  0,  sz, 0],
        [0,  0,  0,  1]
    ])

matrix = scalingMatrix(2, 3, 4)
print("scaling matrix \n",matrix)
-------------------------------------------------
ouput
translation matrix 
 [[1 0 0 1]
 [0 1 0 1]
 [0 0 1 1]
 [0 0 0 1]]
 3d rotation matrix for rotating about y axis 
 [[1 0 0 1]
 [0 1 0 1]
 [0 0 1 1]
 [0 0 0 1]]
3d rotation matrix for rotating about z axis
 [[ 0.8660254 -0.5        0.         0.       ]
 [ 0.5        0.8660254  0.         0.       ]
 [ 0.         0.         1.         0.       ]
 [ 0.         0.         0.         1.       ]]
scaling matrix 
 [[2 0 0 0]
 [0 3 0 0]
 [0 0 4 0]
 [0 0 0 1]]


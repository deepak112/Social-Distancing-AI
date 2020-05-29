#!/usr/bin/env python

'''
Contains functions to calculate center for all bounding boxes and transform prespective for all points,
calculate distance between humans, calculate width and height scale ratio for bird eye view,
and calculates number of humans at risk, low risk, no risk according to closeness.
'''

__title__           = "utills.py"
__Version__         = "1.0"
__copyright__       = "Copyright 2020 , Social Distancing AI"
__license__         = "MIT"
__author__          = "Deepak Birla"
__email__           = "birla.deepak26@gmail.com"
__date__            = "2020/05/29"
__python_version__  = "3.5.2"

# imports
import cv2
import numpy as np

# Function to calculate center for all bounding boxes and transform prespective for all points.
def get_transformed_points(boxes, mi):
    
    bottom_points = []
    for box in boxes:
        #pnts = np.array([[[int(box[0]+(box[2]*0.5)),int(box[1]+box[3])]]] , dtype="float32")
        pnts = np.array([[[int(box[0]+(box[2]*0.5)),int(box[1]+(box[3]*0.5))]]] , dtype="float32")
        bd_pnt = cv2.perspectiveTransform(pnts, mi)[0][0]
        pnt = [int(bd_pnt[0]), int(bd_pnt[1])]
        bottom_points.append(pnt)
        
    return bottom_points

# Function calculates distance between two points(humans). distance_w, distance_h represents number
# of pixels in 180cm length horizontally and vertically. We calculate horizontal and vertical
# distance in pixels for two points and get ratio in terms of 180 cm distance using distance_w, distance_h.
# Then we calculate how much cm distance is horizontally and vertically and then using pythagoras
# we calculate distance between points in terms of cm. 
def cal_dis(p1, p2, distance_w, distance_h):
    
    h = abs(p2[1]-p1[1])
    w = abs(p2[0]-p1[0])
    
    dis_w = float((w/distance_w)*180)
    dis_h = float((h/distance_h)*180)
    
    return int(np.sqrt(((dis_h)**2) + ((dis_w)**2)))

# Function calculates distance between all pairs and calculates closeness ratio.
def get_distances(boxes1, bottom_points, distance_w, distance_h):
    
    distance_mat = []
    bxs = []
    
    for i in range(len(bottom_points)):
        for j in range(len(bottom_points)):
            if i != j:
                dist = cal_dis(bottom_points[i], bottom_points[j], distance_w, distance_h)
                #dist = int((dis*180)/distance)
                if dist <= 150:
                    closeness = 0
                    distance_mat.append([bottom_points[i], bottom_points[j], closeness])
                    bxs.append([boxes1[i], boxes1[j], closeness])
                elif dist > 150 and dist <=180:
                    closeness = 1
                    distance_mat.append([bottom_points[i], bottom_points[j], closeness])
                    bxs.append([boxes1[i], boxes1[j], closeness])       
                else:
                    closeness = 2
                    distance_mat.append([bottom_points[i], bottom_points[j], closeness])
                    bxs.append([boxes1[i], boxes1[j], closeness])
                
    return distance_mat, bxs
 
# Function gives scale for birds eye view               
def get_scale(W, H):
    
    dis_w = 400
    dis_h = 600
    
    return float(dis_w/W),float(dis_h/H)
    
# Function gives count for humans at high risk, low risk and no risk    
def get_count(distances_mat):

    r = []
    g = []
    y = []
    
    for i in range(len(distances_mat)):

        if distances_mat[i][2] == 0:
            if (distances_mat[i][0] not in r) and (distances_mat[i][0] not in g) and (distances_mat[i][0] not in y):
                r.append(distances_mat[i][0])
            if (distances_mat[i][1] not in r) and (distances_mat[i][1] not in g) and (distances_mat[i][1] not in y):
                r.append(distances_mat[i][1])
                
    for i in range(len(distances_mat)):

        if distances_mat[i][2] == 1:
            if (distances_mat[i][0] not in r) and (distances_mat[i][0] not in g) and (distances_mat[i][0] not in y):
                y.append(distances_mat[i][0])
            if (distances_mat[i][1] not in r) and (distances_mat[i][1] not in g) and (distances_mat[i][1] not in y):
                y.append(distances_mat[i][1])
        
    for i in range(len(distances_mat)):
    
        if distances_mat[i][2] == 2:
            if (distances_mat[i][0] not in r) and (distances_mat[i][0] not in g) and (distances_mat[i][0] not in y):
                g.append(distances_mat[i][0])
            if (distances_mat[i][1] not in r) and (distances_mat[i][1] not in g) and (distances_mat[i][1] not in y):
                g.append(distances_mat[i][1])
   
    return (len(r),len(y),len(g))

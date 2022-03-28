#!/usr/bin/env python3

import rospy
import numpy as np
import cv2

from robot_visiualization_lectures.msg import XYZarray, SphereParams
from cv_bridge import CvBridge

points_received = False
points = np.array([])

# topic /xyz_cropped_ball
def point_callback(array):
	# Allow reassignment of global variables
	global points_received
	global points
	# Save the given data
	points = array
	points_received = True


def get_sphere_params(data):
	pass
	

if __name__ == "__main__":
	# initialize ros node
	rospy.init_node('robotics_lab5', anonymous=True)
	# declare pub and sub
	point_sub = rospy.Subscriber('xyz_cropped_ball', XYZarray, point_callback)
	point_pub = rospy.Publisher('/sphere_params', SphereParams, queue_size=1)
	
	# set the frequency to 10 ms
	rate = rospy.Rate(10)
	
	# main loop for publishing
	while not rospy.is_shutdown():
		# make sure we've received data to work on
		if points_received:
			# Get sphere params from data then publish them
			point_pub.publish(get_sphere_params(points))
		rate.sleep()



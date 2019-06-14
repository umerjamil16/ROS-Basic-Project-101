#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def callback(msg):
  arr = msg.ranges
#  print arr
  print "Right 80 Val:" + str(arr[80])
  print "Mid 90 Val: " + str(arr[360])
  print "Left 100 Val: " + str(arr[640])
  mid_val = arr[360]
  right_val = arr[80]
  left_val = arr[640]
  if mid_val < 2:
    pub.publish(move(-0.4,0,0,0,0,-0.7))
  else:
    pub.publish(move(0.4,0,0,0,0,0))





rospy.init_node('topics_quiz_node')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(2)

def move(x1, y1, z1, x2, y2, z2):
    val_msg = Twist()
    val_msg.linear.x = x1
    val_msg.linear.y = y1
    val_msg.linear.z = z1

    val_msg.angular.x = x2
    val_msg.angular.y = y2
    val_msg.angular.z = z2
    print "move func"
    return val_msg

while not rospy.is_shutdown():
  rate.sleep()
  sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)
  #rospy.spin()

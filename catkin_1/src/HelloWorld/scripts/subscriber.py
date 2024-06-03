#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def subscriber_callback(data):
    rospy.loginfo("I heard: %s", data.data)

def subscriber():
    rospy.init_node('subscriber_node', anonymous=True)
    rospy.Subscriber('hello_topic', String, subscriber_callback)
    rospy.spin()

if __name__ == '__main__':
    subscriber()


#!/usr/bin/env python3
import rospy

if __name__=="__main__":
    rospy.init_node("test_node") ##for including ros functionality

    rospy.loginfo("Test node has been started")
    # rospy.loginfo("Hello from test node")
    # rospy.logwarn("This is a warning")
    # rospy.logerr("This is an error")

    # rospy.sleep(1.0)    ##pause for 1 sec

    # rospy.loginfo("End of program")

    ###print something after every "x" seconds

    rate = rospy.Rate(10) ##change frequency here

    while not rospy.is_shutdown(): ##do something as long as the node is alive
        rospy.loginfo("Hello")
        rate.sleep() ##run loop every 0.1sec (10x)
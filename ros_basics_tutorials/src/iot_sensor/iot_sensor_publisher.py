#!/usr/bin/env python3
import rospy
from ros_basics_tutorials.msg import IOTSensor
import random

#we need to initialize the node
rospy.init_node('iot_sensor_publisher_node', anonymous=True)

#create a new publisher. we specify the topic name, then type of message then the queue size
pub = rospy.Publisher('iot_sensor_topic', IOTSensor, queue_size=10)

#set the loop rate
rate = rospy.Rate(1) # 1hz

#keep publishing until a Ctrl-C is pressed
i = 0
while not rospy.is_shutdown():
    iot_sensor = IOTSensor()
    iot_sensor.id = 1
    iot_sensor.name="iot_parking_01"
    iot_sensor.temperature = 24.33 + (random.random()*2)
    iot_sensor.humidity = 33.41+ (random.random()*2)
    rospy.loginfo("I publish:")
    rospy.loginfo(iot_sensor)
    pub.publish(iot_sensor)
    rate.sleep()
    i=i+1


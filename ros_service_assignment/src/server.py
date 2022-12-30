#!/usr/bin/env python3

from ros_service_assignment.srv import RectangleAreaService
from ros_service_assignment.srv import RectangleAreaServiceRequest
from ros_service_assignment.srv import RectangleAreaServiceResponse

import rospy

def rectangle_area_callback(req):
    print("Returning area of a rectangle [%s * %s = %s]"%(req.length, req.breadth, (req.length * req.breadth)))
    return RectangleAreaServiceResponse(req.length * req.breadth)

def rectangle_area_server():
    rospy.init_node('rectangle_area_server_node')
    s = rospy.Service('rectangle_area_service', RectangleAreaService, rectangle_area_callback)
    print("Ready to calculate the area of a rectangle.")
    rospy.spin()
    
if __name__ == "__main__":
    rectangle_area_server()
#!/usr/bin/env python3

import sys
import rospy
from ros_service_assignment.srv import RectangleAreaService
from ros_service_assignment.srv import RectangleAreaServiceRequest
from ros_service_assignment.srv import RectangleAreaServiceResponse

def request_rectangle_area(x, y):
    rospy.wait_for_service('rectangle_area_service')
    try:
        add_two_ints = rospy.ServiceProxy('rectangle_area_service', RectangleAreaService)
        server_response = add_two_ints(x, y)
        return server_response.area
    except rospy.ServiceException(e):
        print("Service call failed: %s"%e)

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = float(sys.argv[1])
        y = float(sys.argv[2])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting the area of a rectangle of width %s and height %s"%(x, y))
    print("area of the rectangle of length %s and breadth %s = %s"%(x, y, request_rectangle_area(x, y)))
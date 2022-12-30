#!/usr/bin/env python3
import rospy
from ros_basics_tutorials.srv import AddTwoInts
from ros_basics_tutorials.srv import AddTwoIntsRequest
from ros_basics_tutorials.srv import AddTwoIntsResponse

def handle_add_two_ints(request):
    print ("Returning [%s + %s = %s]"%(request.a, request.b, (request.a + request.b)))
    return AddTwoIntsResponse(request.a + request.b)

def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
    print ("Ready to add two ints.")
    rospy.spin()
    
if __name__ == "__main__":
    add_two_ints_server()
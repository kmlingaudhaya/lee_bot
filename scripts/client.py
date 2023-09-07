#!/usr/bin/env python

from __future__ import print_function

from service_node.srv import AddTwoInts
import rospy

def add_two_ints_client():
    rospy.wait_for_service('add_two_ints')
    
    try:
        add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
        
        # Prompt the user for input values
        x = int(input("Enter the first integer (x): "))
        y = int(input("Enter the second integer (y): "))
        
        resp1 = add_two_ints(x, y)
        print("Result: %s + %s = %s" % (x, y, resp1.sum))
        
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)

if __name__ == "__main__":
    rospy.init_node('add_two_ints_client')
    add_two_ints_client()

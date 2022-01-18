#!/usr/bin/env python
import math

import rospy
from geometry_msgs.msg import Twist


def move_x(distance):
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel = Twist()
    t0 = rospy.Time.now().to_sec()
    current_distance = 0
    speed = 0.4
    vel.linear.x = speed
    vel.linear.y = 0
    vel.linear.z = 0
    vel.angular.x = 0
    vel.angular.y = 0
    vel.angular.z = 0

    while current_distance < distance:
        velocity_publisher.publish(vel)
        t1 = rospy.Time.now().to_sec()
        current_distance = speed * (t1 - t0)
    vel.linear.x = 0
    velocity_publisher.publish(vel)


def rotate_z(angle):
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    speed = 0.4
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = speed

    t0 = rospy.Time.now().to_sec()
    current_distance = 0
    while current_distance < angle:
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_distance = speed * (t1 - t0)
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)


def draw_square(linear_vel, angular_vel):
    rospy.init_node('turtle1', anonymous=True)
    rate = rospy.Rate(0.5)

    while True:
        move_x(linear_vel)
        rate.sleep()
        rotate_z(math.radians(angular_vel))
        rate.sleep()


if __name__ == '__main__':
    try:
        draw_square(5, 90)
    except rospy.ROSInterruptException:
        pass

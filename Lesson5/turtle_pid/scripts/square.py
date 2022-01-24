#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math


class Turtle:
    Kp = 10
    Ki = 0.01
    Kd = 1
    Angle = math.radians(90)
    Side_time = rospy.Duration(3)

    def __init__(self):
        rospy.init_node('turtle_controller', anonymous=True)
        self.vel_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.pose_sub = rospy.Subscriber('/turtle1/pose', Pose, self.current_angle)

        self.com_vel = Twist()
        self.current_pose = Pose()
        self.current_ang = self.current_pose.theta
        self.com_vel.linear.x = 1
        self.angle_destination = 0
        self.rate = rospy.Rate(10)

    def current_angle(self, data):
        self.current_ang = data.theta

    def draw_square(self):
        old_angle = 0
        time = rospy.get_rostime()
        I = 0
        while not rospy.is_shutdown():
            if rospy.get_rostime() > time + self.Side_time:
                time = rospy.get_rostime()
                self.angle_destination = self.angle_destination + self.Angle
                
                if self.angle_destination < math.radians(-180):
                    self.angle_destination += math.radians(360)
                if self.angle_destination > math.radians(180):
                    self.angle_destination -= math.radians(360)

            err = self.angle_destination - self.current_ang
            if err < math.radians(-180):
                err += math.radians(360)
            if err > math.radians(180):
                err -= math.radians(360)

            #rospy.loginfo("%s %s %s", self.angle_destination, self.current_ang, err)
            
            P = self.Kp * err
            I += self.Ki * err
            D = self.Kd * (self.current_ang - old_angle)

            self.com_vel.angular.z = P + I + D
            
            old_angle = self.current_ang
            
            self.vel_pub.publish(self.com_vel)
            self.rate.sleep()


if __name__ == '__main__':
    try:
        x = Turtle()
        x.draw_square()
    except rospy.ROSInterruptException:
        pass

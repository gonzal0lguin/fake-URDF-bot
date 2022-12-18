#!/usr/bin/env python3

import rospy
import smach
from move_base_msgs.msg import MoveBaseActionGoal
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan


class Start(smach.State):
    """
    Starting state. Only for machine loading
    """
    def __init__(self):
        smach.State.__init__(self, outcomes=[], input_keys=[], output_keys=[])
    
    def execute(self, ud):
        pass

class WaitingForGoal(smach.state):
    """
    Receives the new goal pose and processes it. Latches robot in place
    while no command is received.
    """
    def __init__(self):
        smach.State.__init__(self, outcomes=[], input_keys=[], output_keys=[])
    
    def execute(self, ud):
        pass

class Navigating(smach.State):
    """
    Performs the call to GoalServer and monitors the state of the robot. If 
    a stuck instance is detected recovery will be triggered.
    """
    def __init__(self):
        smach.State.__init__(self, outcomes=[], input_keys=[], output_keys=[])
    
    def execute(self, ud):
        pass

class StuckRecovery(smach.State):
    """
    Rotates robot until sensors get clared out pf the stuck zone on the
    local costmap.
    """
    def __init__(self):
        smach.State.__init__(self, outcomes=[], input_keys=[], output_keys=[])
    
    def execute(self, ud):
        pass

class Orienting(smach.State):
    """
    Experimental state. Sometimes is better to orient robot before navigating,
    when goals are behind the usable areaa of sensors.
    """
    def __init__(self):
        smach.State.__init__(self, outcomes=[], input_keys=[], output_keys=[])
    
    def execute(self, ud):
        pass


def getInstance(robot):
    pass

def main():
    rospy.init_node('navigation_state_machine_node')
    # sm = getInstance('robot lol')
    # outcome = sm.execute()



if __name__=='__main__':
    main()
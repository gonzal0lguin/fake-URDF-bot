#!/usr/bin/env python3

import rospy
import smach
import smach_ros


class Waiting(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['success', 'failed'],
                                input_keys=['x', 'y'], output_keys=['t1', 't2'])

    def execute(self, ud):
        rospy.loginfo('Starting machine')

        ud.t1 = ud.x + 1
        ud.t2 = ud.y - 1

        return 'success'


class Working(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['success', 'working'],
                                input_keys=['t1', 't2'], output_keys=['t1', 't2'])

    def execute(self, ud):
        if ud.t1 < 5:
            t1 = input("enter value of t1")
            ud.t1 = int(t1)
            rospy.loginfo(f'Machine still executing task: {ud.t1}')
            return 'working'
        
        else:
            rospy.loginfo('Process done')
            return 'success'

# class End(smach.State):
#     def __init__(self):
#         smach.State.__init__(self, outcomes=['success'])
 

def getInstance():
    sm = smach.StateMachine(outcomes=['success', 'failed'])
    sm.userdata.x = 0
    sm.userdata.y = 2

    with sm:

        smach.StateMachine.add('Waiting', Waiting(), 
            transitions={'success':'Working', 'failed':'Waiting'})
        
        smach.StateMachine.add('Working', Working(), 
            transitions={'success':'success', 'working':'Working'})
    
    return sm


def main():
    rospy.init_node('smach_test')
    sm = getInstance()
    outcome = sm.execute()

if __name__ == '__main__':
    main()

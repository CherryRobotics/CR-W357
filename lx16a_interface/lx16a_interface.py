#!/usr/bin/env python
import rospy
import lewansoul_lx16a

SERIAL_PORT='SERIAL_PORT_ID'

controller = lewansoul_lx16a.ServoController(
    serial.Serial(SERIAL_PORT, 115200,timeout=1)
)


def callback(data):
    commands = data.positions # Get array of positions, move to positions
    for i, command in enumerate(commands):
        controller.servo(i).move_prepare(command)
    controller.move_start()

def listener():
    rospy.init_node('motor_recieve')
    rospy.Subscriber("motor_send", lx16a_command, callback)
    rospy.spin()

if if __name__ == "__main__":
    listener()
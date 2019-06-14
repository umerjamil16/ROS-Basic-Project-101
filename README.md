# ROS Basic Project 101

In this little project(Part of a coursework of [The Construct Sim Robot Ignite Academy](http://www.theconstructsim.com/)), I wrote a code to make the **kobuki** robot avoid the wall that is in front of him. To help achieve this, I did the following:

1.  Created a Publisher that writes into the  **/cmd_vel**  topic in order to move the robot.
2.  Created a Subscriber that reads from the  **/kobuki/laser/scan topic**. This is the topic where the laser publishes its data.
3.  Depending on the readings received from the laser's topic, the data sending to the /cmd_vel topic was manipulated, in order to avoid the wall. The data that is published into the /kobuki/laser/scan topic has a large structure. Running following command in the terminal will reveal the msg struct of LaserScan
```
rosmsg show sensor_msgs/LaserScan
```
Output:
```
std_msgs/Header header
  uint32 seq
  time stamp
  string frame_id
float32 angle_min
float32 angle_max
float32 angle_increment
float32 time_increment
float32 scan_time
float32 range_min
float32 range_max
float32[] ranges <-- Used only this one
float32[] intensities
```

The size of 'ranges' array is 720. This means that for coverage of 180 degrees, there are 720 elements. Therefore, for 1 degree, there are 04 array elements.

The mid, left and right most values of sensor readings can be obtained as follows:

```
mid_val = msg.ranges[360]
right_val = msg.ranges[80]
left_val = msg.ranges[640]
```

The complete project can be launched from terminal using the following command:

```
roslaunch topics_quiz topics_quiz.launch
```

#include "ros/ros.h"
#include <iostream>
#include "std_msgs/String.h"
using namespace std;
std_msgs::String command;
string temp;
ros::Publisher pub;
void callback(const std_msgs::String &msg){
	temp=msg.data;
}

void commander(string komenda){
    command.data=komenda;
        pub.publish(command);
        cout<<"Komenda: "<<command.data<<endl;
        ros::Duration(3).sleep();
        ros::spinOnce();
}

int main(int argc, char **argv) {
	
    ros::init(argc, argv, "voice_commander");
    ros::NodeHandle n; 
    ros::Subscriber sub = n.subscribe("/voice_reco", 1000, callback);
    pub = n.advertise<std_msgs::String>("ur_controller/order",100);
    ros::Rate loop_rate(100);
	while (ros::ok()) {
		
		if (temp == "move forward" || temp == "move forwards") commander("moveForward");
		else if(temp == "move backwards" || temp == "move back" || temp == "move backward") commander("moveBackwards");
		else if(temp == "move left" || temp == "turn left") commander("moveLeft");
		else if(temp == "move right" || temp == "turn right") commander("moveRight"); 
		else if(temp == "go to the initial position" || temp == "go to initial position") commander("moveInit");
		else if(temp == "move place" || temp == "move to place" || temp == "move to the place") commander("movePlace");
		command.data="";
		temp="";
		ros::spinOnce();
		loop_rate.sleep();
	}
	
    return 0;
}

//Including libraries
#include <ros.h> // ros_lib library
#include "MS5837.h" //Barometer Library
#include <Wire.h>

//Including msgs
#include <std_msgs/String.h>
#include <barometer/Barometer.h>

// Creating variable for the barometer
MS5837 barometer_sensor;

// Creating variables related to ROS
ros::NodeHandle node_handler;
barometer::Barometer barometer_message;
ros::Publisher barometer_topic("barometer_topic", &barometer_message);

void setup(){

  // Initalizing Node
  node_handler.initNode();
  node_handler.advertise(barometer_topic);

  // Initializing Barometer
  barometer_init();

}

void loop() {

  barometer_reading();

  node_handler.spinOnce();
}

// Function for initialzing the barometer
void barometer_init(){
  Wire.begin();

  while(!barometer_sensor.init()){
    delay(3000);
  }

  // Setting the fluid density for the barometer
  // Air ~ 1.23, Freshwater ~ 997, Seawater ~ 1029
  barometer_sensor.setFluidDensity(997);
}

// Function for reading and publishing barometer data.
void barometer_reading(){
  barometer_sensor.read();
  barometer_message.depth = barometer_sensor.depth();
  barometer_message.temperature = barometer_sensor.temperature();
  barometer_topic.publish(&barometer_message);
}

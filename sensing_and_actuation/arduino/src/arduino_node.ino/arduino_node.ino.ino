//Including libraries
#include <ros.h> // ros_lib library
#include "MS5837.h" //Barometer Library
#include <Wire.h>
#include "ping1d.h"

//Including msgs
#include <std_msgs/String.h>
#include <robosub_messages/Barometer.h>
#include <robosub_messages/Sonar.h>
static const uint8_t arduinoRxPin = 18;
static const uint8_t arduinoTxPin = 19;

// Creating variable for the barometer
MS5837 barometer_sensor;
static Ping1D sonar { Serial1 };

// Creating variables related to ROS
ros::NodeHandle node_handler;
robosub_messages::Barometer barometer_message;
ros::Publisher barometer_topic("barometer_topic", &barometer_message);
robosub_messages::Sonar sonar_message;
ros::Publisher sonar_topic("sonar_topic", &sonar_message);

void setup(){
  
  // Initalizing Node
  node_handler.initNode();
  node_handler.advertise(barometer_topic);

  // Initializing Barometer
  barometer_init();
  
  sonar_init();
  
}

void loop() {

  barometer_reading();
  sonar_reading();
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

void sonar_init(){
  Serial1.begin(115200);
  node_handler.getHardware()->setBaud(115200);
  while(!sonar.initialize()){
    node_handler.advertise(sonar_topic);
  }
}
void sonar_reading(){
  if(sonar.update()){
    sonar_message.distance = sonar.distance();
    sonar_message.confidence = sonar.confidence();
    sonar_topic.publish(&sonar_message);
    
  }
}

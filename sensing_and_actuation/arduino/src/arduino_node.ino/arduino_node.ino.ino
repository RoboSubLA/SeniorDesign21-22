#include <ros.h>
#include <std_msgs/String.h>
#include "MS5837.h"
#include <Wire.h>

#include <barometer/Barometer.h>
MS5837 barometer_sensor;

ros::NodeHandle node_handler;
barometer::Barometer barometer_message;
ros::Publisher barometer_topic2("barometer_topic", &barometer_message);

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

void barometer_init(){
  Wire.begin();

  while(!barometer_sensor.init()){
    delay(3000);
  }

  barometer_sensor.setFluidDensity(997);
}

void barometer_reading(){
  barometer_sensor.read();
  barometer_message.depth = barometer_sensor.depth();
  barometer_message.temperature = barometer_sensor.temperature();
  barometer_topic2.publish(&barometer_message);
}

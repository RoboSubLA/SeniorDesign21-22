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
  node_handler.advertise(sonar_topic);

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
    delay(1000);
  }
  Serial.print("Barometer Initialized");

  // Setting the fluid density for the barometer
  // Air ~ 1.23, Freshwater ~ 997, Seawater ~ 1029
  barometer_sensor.setFluidDensity(997);
}

// Function for reading and publishing barometer data.
void barometer_reading(){
  barometer_sensor.read();
  barometer_message.depth = barometer_sensor.depth();
  Serial.print(barometer_sensor.depth());
  
  barometer_message.temperature = barometer_sensor.temperature();
  barometer_topic.publish(&barometer_message);
}

void sonar_init(){
  Serial1.begin(115200);
  Serial.begin(5700);
  
  while(!sonar.initialize()){
    Serial.println("\nPing device failed to initialize!");
    Serial.println("Are the Ping rx/tx wired correctly?");
    Serial.print("Ping rx is the green wire, and should be connected to Arduino pin ");
    Serial.print(arduinoTxPin);
    Serial.println(" (Arduino tx)");
    Serial.print("Ping tx is the white wire, and should be connected to Arduino pin ");
    Serial.print(arduinoRxPin);
    Serial.println(" (Arduino rx)");
    delay(2000);
  }
  Serial.print("Sonar Initialized");
}
void sonar_reading(){
  if(sonar.update()){
    sonar_message.distance = sonar.distance();
    Serial.print(sonar.distance());
    sonar_message.confidence = sonar.confidence();
    sonar_topic.publish(&sonar_message);
    
  }
}

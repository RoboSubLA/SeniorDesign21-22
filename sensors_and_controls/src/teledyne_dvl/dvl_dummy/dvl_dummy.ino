/*
 * rosserial Publishing DVL sensor data
 */

#include <ros.h>
// INCLUDE NECESSARY LIBRARY FOR SENSORS

int xvel = 0;
int yvel = 0;
int zvel = 0;
int xpos = 0;
int ypos = 0;
int zpos = 0;
int yaw = 0;
int pitch = 0;
int roll = 0;
int depth = 0;
String s = ",";

void setup() {
  //SHOULD INITIALIZE SENSORS BELOW IN THE SETUP
  //Set serial baudrate to the same in dvl_driver.py
  Serial.begin(115200);
}

void loop() {
  //USE LOOP TO CONSTANTLY GET SENSOR DATA AND PUBLISH IT
  //SHOULD HAVE A DELAY AS TO HOW OFTEN IT SHOULD GET DATA

  
  
  //Serial printing to computer. Currently printing DUMMY DATA
  //Printing dummy data in the form of xpos, ypos, zpos, yaw, pitch, roll, depth
  Serial.println(xvel + s + yvel + s + zvel + s + xpos + s + ypos + s + zpos + s + yaw + s + pitch + s + roll);

  //Randomly adding 
  xvel = xvel + random(-1, 2);
  yvel = yvel + random(-1, 2);
  zvel = zvel + random(-1, 2);
  xpos = xpos + random(-5, 6);
  ypos = ypos + random(-5, 6);
  zpos = zpos + random(-5, 6);
  yaw = yaw + random(-3, 4);
  pitch = pitch + random(-3, 4);
  roll = roll + random(-3, 4);
  
  delay(3000);
}

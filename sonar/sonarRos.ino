
#include <ros.h>
#include <std_msgs/Float32.h>

#include "ping1d.h"

static const uint8_t arduinoRxPin = 18;
static const uint8_t arduinoTxPin = 19;

static Ping1D ping { Serial1 };

static const uint8_t ledpin = 13;

ros::NodeHandle  nh;

#mm distance
std_msgs::Float32 data;
ros::Publisher chatter("chatter", &data);

#inches distance
std_msgs::Float32 inches;
ros::Publisher chatte("chatte", &inches);

#confidence 
std_msgs::Float32 confidence;
ros::Publisher chatt("chatt", &confidence);


void setup()
{
  Serial1.begin(115200);
  Serial.begin(115200);
  nh.getHardware()->setBaud(115200);
  nh.initNode();
  ping.initialize();
  nh.advertise(chatter);
  nh.advertise(chatte);
  nh.advertise(chatt);
}

void loop()
{
  if(ping.update()){
    Serial.print(ping.distance());
  data.data = ping.distance();
  chatter.publish( &data );
  
  
  inches.data = ping.distance() / 25.4;
  chatte.publish( &inches );
  
  confidence.data = ping.confidence();
  chatt.publish( &confidence );
  
  //processes callbacks when you tell it
  nh.spinOnce();
  delay(1000);
  }
}

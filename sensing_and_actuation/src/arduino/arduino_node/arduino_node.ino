//Including libraries
#include <ros.h> // ros_lib library
#include "MS5837.h" //Barometer Library
#include <Wire.h>
#include "ping1d.h" //Sonar library
#include <PID_v1.h> 
#include <Servo.h>


//Including msgs
#include <std_msgs/String.h>
#include <robosub_messages/Barometer.h>
#include <robosub_messages/Sonar.h>

//Start thrusters as servos and set Pins**
Servo front_left_vertical_thruster;
Servo front_left_horizontal_thruster;
Servo front_right_vertical_thruster;
Servo front_right_horizontal_thruster;
Servo back_left_vertical_thruster;
Servo back_left_horizontal_thruster;
Servo back_right_vertical_thruster;
Servo back_right_horizontal_thruster;

double front_left_vertical_thruster_value;
double front_left_horizontal_thruster_value;
double front_right_vertical_thruster_value;
double front_right_horizontal_thruster_value;
double back_left_vertical_thruster_value;
double back_left_horizontal_thruster_value;
double back_right_vertical_thruster_value;
double back_right_horizontal_thruster_value;

int front_left_vertical_thruster_pin = 5;
int front_left_horizontal_thruster_pin = 6;
int front_right_vertical_thruster_pin = 7;
int front_right_horizontal_thruster_pin = 8;
int back_left_vertical_thruster_pin = 9;
int back_left_horizontal_thruster_pin = 10;
int back_right_vertical_thruster_pin = 11;
int back_right_horizontal_thruster_pin = 12;


double H_distance_input, H_distance_output, H_distance_setpoint;
double barometer_input, barometer_output, barometer_setpoint;

double X_angle_input, X_angle_output, X_angle_setpoint;
double Y_angle_input, Y_angle_output, Y_angle_setpoint;
double Z_angle_input, Z_angle_output, Z_angle_setpoint;
double temp_input;
unsigned long lastUnstable = 0;

double H_distance_kP = 1;            //****
double H_distance_kI = 0;            //****
double H_distance_kD = 0;            //****
double barometer_kP = 300;           //****   400 might be too high
double barometer_kI = 0;             //****
double barometer_kD = 0;             //****

double X_angle_kP = 3.5;              //****
double X_angle_kI = 0.0005;           //****
double X_angle_kD = 4;                //****
double Y_angle_kP = 3.5;              //****
double Y_angle_kI = 0.0005;           //****
double Y_angle_kD = 4;                //****
double Z_angle_kP = 3.5;              //****
double Z_angle_kI = 0.0005;           //****
double Z_angle_kD = 4;                //****

PID H_distance_PID  (&H_distance_input, &H_distance_output, &H_distance_setpoint,
                     H_distance_kP, H_distance_kI, H_distance_kD, DIRECT);
PID barometer_PID  (&barometer_input, &barometer_output, &barometer_setpoint,
                    barometer_kP, barometer_kI, barometer_kD, DIRECT);

PID X_angle_PID    (&X_angle_input, &X_angle_output, &X_angle_setpoint,
                     X_angle_kP, X_angle_kI, X_angle_kD, DIRECT);
PID Y_angle_PID    (&Y_angle_input, &Y_angle_output, &Y_angle_setpoint,
                    Y_angle_kP, Y_angle_kI, Y_angle_kD, DIRECT);
PID Z_angle_PID    (&Z_angle_input, &Z_angle_output, &Z_angle_setpoint,
                    Z_angle_kP, Z_angle_kI, Z_angle_kD, DIRECT);

// Sonar Pin Variables
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
ros::Subscriber<robosub_messages::ControlCommand> sub("controlCommand", Outputs);

void setup(){
  // Initalizing Node
  node_handler.initNode();
  node_handler.advertise(barometer_topic);
  node_handler.advertise(sonar_topic);

  // Initializing Sensors & Controls
  barometer_init();
  sonar_init();
  //thrusters_init()
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

//Attaches thrusters and initializes PIDs
void thrusters_init() {
  front_left_vertical_thruster.attach(front_left_vertical_thruster_pin);
  front_left_horizontal_thruster.attach(front_left_horizontal_thruster_pin);
  front_right_vertical_thruster.attach(front_right_vertical_thruster_pin);
  front_right_horizontal_thruster.attach(front_right_horizontal_thruster_pin);
  back_left_vertical_thruster.attach(back_left_vertical_thruster_pin);
  back_left_horizontal_thruster.attach(back_left_horizontal_thruster_pin);
  back_right_vertical_thruster.attach(back_right_vertical_thruster_pin);
  back_right_horizontal_thruster.attach(back_right_horizontal_thruster_pin);

  H_distance_PID.SetMode(AUTOMATIC);
  barometer_PID.SetMode(AUTOMATIC);
  X_angle_PID.SetMode(AUTOMATIC);
  Y_angle_PID.SetMode(AUTOMATIC);
  Z_angle_PID.SetMode(AUTOMATIC);

  H_distance_PID.SetOutputLimits(-300.00, 300.00);     //assuming max power is +-300
  barometer_PID.SetOutputLimits(-300.00, 300.00);     //assuming max power is +-300
  X_angle_PID.SetOutputLimits(-100.00, 100.00);
  Y_angle_PID.SetOutputLimits(-100.00, 100.00);
  Z_angle_PID.SetOutputLimits(-100.00, 100.00);

  H_distance_input = 0;              //The distance input will always be 0

  H_distance_setpoint = 0;           //****
  barometer_setpoint = 0.15;         //****
  X_angle_setpoint = 0;              //****
  Y_angle_setpoint = 0;              //****
  Z_angle_setpoint = 0;              //****
}

//Calculates PIDs and sends Outputs
void Outputs(const robosub_messages::ControlCommand& controls_data) {
  X_angle_setpoint = controls_data.yaw_set;
  Y_angle_setpoint = controls_data.pitch_set;
  Z_angle_setpoint = controls_data.roll_set;
  H_distance_setpoint = controls_data.distance_set;
  barometer_setpoint = controls_data.depth_set;

  Path_Optimization();
  H_distance_PID.Compute();
  barometer_PID.Compute();
  X_angle_PID.Compute();
  Y_angle_PID.Compute();
  Z_angle_PID.Compute();
  Mixer();

  Serial_Print_Thruster_Values();
  front_left_vertical_thruster.writeMicroseconds(front_left_vertical_thruster_value);
  front_left_horizontal_thruster.writeMicroseconds(front_left_horizontal_thruster_value);
  front_right_vertical_thruster.writeMicroseconds(front_right_vertical_thruster_value);
  front_right_horizontal_thruster.writeMicroseconds(front_right_horizontal_thruster_value);
  back_left_vertical_thruster.writeMicroseconds(back_left_vertical_thruster_value);
  back_left_horizontal_thruster.writeMicroseconds(back_left_horizontal_thruster_value);
  back_right_vertical_thruster.writeMicroseconds(back_right_vertical_thruster_value);
  back_right_horizontal_thruster.writeMicroseconds(back_right_horizontal_thruster_value)
}


//Takes Error and Chooses which Direction to turn
void Path_Optimization() {
  double half_circle_pos = 180.00;
  double half_circle_neg = -180.00;
  double X_angle_error = X_angle_setpoint - X_angle_input;

  if (X_angle_error > half_circle_pos) {
    X_angle_error = X_angle_error - 360;
  }
  else if (X_angle_error < half_circle_neg) {
    X_angle_error = X_angle_error + 360;
  }
  
  X_angle_setpoint = X_angle_error + X_angle_input;
}



//Takes PID outputs and makes pwm for Thrusters
void Mixer() {

  // 8 Thrusters
  front_left_vertical_thruster_value = 1500 + barometer_output + Y_angle_output - Z_angle_output;
  front_left_horizontal_thruster_value = 1500 + H_distance_output + X_angle_output;
  front_right_vertical_thruster_value = 1500 + barometer_output + Y_angle_output + Z_angle_output;
  front_right_horizontal_thruster_value = 1500 + H_distance_output + X_angle_output;
  back_left_vertical_thruster_value = 1500 + barometer_output - Y_angle_output - Z_angle_output;
  back_left_horizontal_thruster_value = 1500 + H_distance_output + X_angle_output;
  back_right_vertical_thruster_value = 1500 + barometer_output - Y_angle_output + Z_angle_output;
  back_right_horizontal_thruster_value = 1500 + H_distance_output + X_angle_output;


  // 6 Thrusters
  //final_left_thruster_value = 1500 + H_distance_output + X_angle_output;
  //final_right_thruster_value = 1500 + H_distance_output - X_angle_output;
  //final_front_right_thruster_value = 1500 + barometer_output + Y_angle_output + Z_angle_output;
  //final_front_left_thruster_value = 1500 + barometer_output + Y_angle_output - Z_angle_output;
  //final_back_left_thruster_value = 1500 + barometer_output - Y_angle_output - Z_angle_output;
  //final_back_right_thruster_value = 1500 + barometer_output - Y_angle_output + Z_angle_output;
}

//Print All Thrusters Values
void Serial_Print_Thruster_Values() {
  Serial.print("FrontLeft_Horisontal_Thruster: ");
  //Serial.print(final_front_left_horizontal_thruster_value);
  Serial.print("-------");
  Serial.print("Right: ");
  //Serial.print(final_right_thruster_value);
  Serial.print("-------");
  Serial.print("FrontRight: ");
  //Serial.print(final_front_right_thruster_value);
  Serial.print("----");
  Serial.print("FrontLeft: ");
  //Serial.print(final_front_left_thruster_value);
  Serial.print("----");
  Serial.print("BackLeft: ");
  //Serial.print(final_back_left_thruster_value);
  Serial.print("----");
  Serial.print("BackRight: ");
  //Serial.print(final_back_right_thruster_value);
  Serial.print("----");
}

bool isStabilized() {
  if ((abs(X_angle_setpoint - X_angle_input) < 5) && (abs(Y_angle_setpoint - Y_angle_input) < 5) &&
      (abs(Z_angle_setpoint - Z_angle_input) < 5) && (abs(barometer_setpoint - barometer_input) < 0.1524) &&
      (H_distance_setpoint == 0)) 
      {
        if ((millis() - lastUnstable) > 3000) {
          return true;
        }
        return false;
      }
  lastUnstable = millis();
  return false;
}

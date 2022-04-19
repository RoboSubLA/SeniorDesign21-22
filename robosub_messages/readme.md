# Robosub Messages
We use this package to create all our message files.

## How to add a message
1. Create your `<Mymessage>.msg` file in the `msg` folder
2. Inside `CMakeLists.txt` find 
  ```
  add_message_files(
        FILES
        message.msg
        ...
        ...
        (add your message file here)
    )
 ```
 3. Your msg is now ready to be used by other packages, just make sure `robosub_messages` is added as a dependency.

## Current Messages

### Barometer.msg
| Field name                        | Type      |
| ----------------------------------| ----------|
| depth                             | float32   |
| temperature                       | float32   |

### Hydrophones.msg
| Field name                        | Type      |
| ----------------------------------| ----------|
| direction                         | int32     |

### Sonar.msg
| Field name                        | Type      |
| ----------------------------------| ----------|
| distance                          | float32   |
| confidence                        | float32   |

### IMU.msg
| Field name                        | Type      |
| ----------------------------------| ----------|
| roll                              | int32     |
| pitch                             | int32     |
| yaw                               | int32     |

### DVL.msg
| Field name                        | Type      |
| ----------------------------------| ----------|
| roll                              | int32     |
| pitch                             | int32     |
| yaw                               | int32     |
| x_translation                     | float32   |
| y_translation                     | float32   |


### CV.msg
| Field name                        | Type      |
| ----------------------------------| ----------|
| targetSeen                        | bool      |
| targetDis                         | float32   |
| xOffset                           | float32   |
| yOffset                           | float32   |

### gate.msg
| Field name                        | Type      |
| ----------------------------------| ----------|
| gateSeen                          | bool      |
| gateDis                           | float32   |
| gatediscentr                      | float32   |

### test.msg
| Field name                        | Type      |
| ----------------------------------| ----------|
| imu                               | bool      |
| barometer                         | bool      |
| sonar                             | bool      |
| hydrophones                       | bool      |
| dvl                               | bool      |
| cv                                | bool      |

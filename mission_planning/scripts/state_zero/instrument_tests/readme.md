# How to structure tests

### as a single testing node/ independent package
    monitors all the different topics
    sends the message as a custom package
        bool imu
        bool bar
        bool cv

    can be expanded to add more sensors or other things to monitor


### as a stat to state to transition to to perform checks
    can be called between transitions




gate distance distancefromcenter

cv.msg
    gateSeen 
    gatedis
    gatediscenter

    targetSeen
    targetDis
    targetdiscenter

gate.msg
    seen = false
    dis = -99
    center = -99
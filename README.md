# Raspberry Pi - RC car controller
The program esc.py enables you to control a classic RC car with a Raspberry Pi and a PCA9685 servo controller.
To read more about my project just visit my blog for more details and pictures: 

https://custom-build-robots.com/raspberry-pi-roboter/autonom-fahrendes-raspberry-pi-ki-roboter-auto-software/9777

The picture below shows my RC car I build out of electronic components I already had or which I bought in China.

![Raspberry Pi robots](https://custom-build-robots.com/wp-content/uploads/2018/02/Autonom_fahrendes_Raspberry_Pi_KI_Roboter_Auto_model-300x200.jpg)

The ESC is a very cheap one from Amazon but it works very well in my rc car.

![Raspberry Pi robots](https://custom-build-robots.com/wp-content/uploads/2018/02/Autonom_fahrendes_Raspberry_Pi_KI_Roboter_Auto_ESC_1-300x200.jpg)

The program "esc.py" shows a text menue which explains which keys are used to control the steering servo and the dc motor.
The dc motor is connetected with the channel 0 of the PCA9685 board. The steering servo is conntected with the channel 1 of the servo controller.

The picture below shows the python program to control the RC car.

![Raspberry Pi robots](https://custom-build-robots.com/wp-content/uploads/2018/02/Python_RC_car_controller-300x95.jpg)

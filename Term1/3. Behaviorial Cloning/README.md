# Behaviorial-Cloning Project

## Model Architecture and Training Strategy

### Model Architecture:
For LeNet architecture car was drifting off the road, so I tried more powerful architecture from NVIDIA end to end driving paper. In my
model I used 3 convolution layers with 5x5 kernel size followed by 3 more convolution layer with 3x3 kernel size followed by 4 fully 
connected layers. The last fully connected layer is of size 1 to predict steering angle. At beginning data is normalized in the model 
using a Keras lambda layer and cropped using keras cropped layer. The model includes RELU layers to introduce nonlinearity.

### Attempts to reduce over fitting in the model:
First training on above model showed very high mean squared error(mse), loss between training and validation set resulted in car drifting
off the road coz of over fitting. To reduce over fitting, I increased number of data points and introduced dropout and pooling layers in
model which. This strategy resulted in reducing mse loss at the end car successfully completed lap.

### Model parameter tuning
The model used an adam optimizer, so the learning rate was not tuned manually.

### Appropriate training data
I used all 3 camera images to train my model. I changed steering angle correction factor from 0.2 to 0.4 which showed lot improvement in
driving. While recording data I tried to keep car in middle of road. I let the car drift to the edge of the road and recover before a 
crash occurs. I took 2 laps of center lane and one lap of track from opposite direction. I got around 4825 data points for training my 
model.

Center view | Left view | Right view
------------ | ------------- | -------------
![alt_text-1](https://github.com/oalahurikar/Behaviorial-Cloning/blob/master/Images%20and%20Graphs/Camera%20Center.jpg) | ![alt_text-2](https://github.com/oalahurikar/Behaviorial-Cloning/blob/master/Images%20and%20Graphs/Camera%20Left.jpg) | ![alt_text-3](https://github.com/oalahurikar/Behaviorial-Cloning/blob/master/Images%20and%20Graphs/Camera%20Right.jpg) 

### Solution Design Approach
In designing model architecture I was looking to minimize over fitting and converging solution as fast as possible on given data. My first approach was to use simple model (LeNet) and then I used more powerful model from NVIDIA paper which showed a lot of improvement compared to earlier architecture, after minimizing over fitting and lot of tweaks my car able to complete track. 

### Final Model Architecture and analysis.
Following is final model architecture. 

![alt_text-1](https://github.com/oalahurikar/Behaviorial-Cloning/blob/master/Images%20and%20Graphs/CNN%20Arcitecture.png) 

For above architecture at first I used 2048 data points for training which resulted in over fitting as shown in figure 2, to minimize over fitting I captured more training data and change in strategy of data logging explained in ‘Appropriate training data’ section. For 4825 data points I got result shown in figure 3.

MSE with small data | MSE with Large data (Final solution)
------------ | -------------
![alt_text-1](https://github.com/oalahurikar/Behaviorial-Cloning/blob/master/MSE%20Error1.png) | ![alt_text-2](https://github.com/oalahurikar/Behaviorial-Cloning/blob/master/MSE%20Error2.png)

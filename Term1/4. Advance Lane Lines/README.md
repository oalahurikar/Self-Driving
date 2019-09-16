# Advance-Lane-Lines
Advance Lane Line Detection for Self driving car
# Preprocessing: 
With original training data set results of network was over fitted. Because some image class had few no of images. After adding additional
images to class with lacking images network accuracy improved a lot. I first trained network on normalized color images, in next attempt I 
gray scaled images and normalized it. I found there is not much difference in accuracy but gray scaled image helped to train network faster.  
# Model Architecture
I used LeNet CNN architecture with 2 convolutional layers and 3 fully connected layers. First I just used max pooling and my accuracy
was about 91 % for 30 epochs, but top 5 probabilities showed me some of images predicted wrong because of over fitting. So I introduce drop out, which resolved over fitting issue, also helped to predict top 5 probabilities in reasonable range.  Due to gray scaling my network needed 32x32x1 input images.
# Model Training
I used Adam optimizer which did better than gradient descent optimizer. I tried different learning rate(From 0.01 to 0.001), drop out
percentage(50 to 70), Batch size (from 100 to 250). But I found 0.001 of learning rate and 120 batch size showed best performance. 
I also used drop outs at conv1, fc1 and fc2. Tuned drop out percentage from 50 to 70 % at last found best performance at conv1 and fc1
with dropout rate of 70 percent.
# Solution Approach
Additional images of classes with short of images showed much improved accuracy. Normalizing and gray scaling improved accuracy as well
and also helped to reduce training time. After changing hyper parameters and changing drop out locations in CNN model I end up with 95 
percent accuracy after 30 epochs.
# Performance on New Images
My model predicts all images with accuracy of 83 % except stop sign. I am assuming the sign image angle is affecting model prediction. Prospective transform might resolve this issue.
Model Certainty - Softmax Probabilities
Answer: In top 5 probabilities my model predicts Yield, no entry and general caution signs confidently. For dangerous curve to right sign it predicts by 65 % then 35 % for slippery road and 5 % for children crossing and surprisingly all three images are in triangular form. Model predicts 60 Kmh sign by 80 % which is far higher than reaming 4 probabilities. 


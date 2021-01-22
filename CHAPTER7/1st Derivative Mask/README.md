<h1> ● Sobel Mask </h1>
<br>
   
## 1) 1D / 2D Gaussian Distribution
After getting gradient magnitude and direction, a full scan of image is done to remove any unwanted pixels which may not constitute the edge. For this, at every pixel, pixel is checked if it is a local maximum in its neighborhood in the direction of gradient. Check the image below:   

<p align="center"><img src="https://i0.wp.com/www.adeveloperdiary.com/wp
-content/uploads/2019/05/How-to-implement-Sobel-edge-detection-using-Python-from-scratch-adeveloperdiary.com-sobel-sobel-operator.jpg?resize=744%2C356"></img></p>      


When standard deviation gets bigger, the height of distribution gets lower and the width of it gets fatter. This means that the blurring effect will become weaker since
the center coefficient has no big difference with surrounding ones.   
And needless to say, when std_dev gets smaller, thick blurring effect we get.
        
        
## 2) Consisting Gaussian Smoothing Kernel(Mask)
Each coefficient of kernel(= each element of mask matrix) is set based on Gaussian Distribution above. Also, so as to keep the brightness of the input image the same after smoothing, we should make a sum of kernel(mask) coefficients become '1'. See the matrix below:

<p align="center"><img src="https://www.tutorialspoint.com/dip/images/sobel3.jpg"></img></p> 

After passing convolution process, this filter eventually smooths the image!

```python
import cv2
Blurred = cv2.GaussianBlur(image, ksize, 0)

cv2.imshow("Gaussian Filtering", Blurred)
cv2.waitKey(0)
```

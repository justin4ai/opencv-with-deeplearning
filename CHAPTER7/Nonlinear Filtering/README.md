<h1> ● Gaussian Smoothing Filter </h1>
<br>
   
## 1) 1D / 2D Gaussian Distribution
After getting gradient magnitude and direction, a full scan of image is done to remove any unwanted pixels which may not constitute the edge. For this, at every pixel, pixel is checked if it is a local maximum in its neighborhood in the direction of gradient. Check the image below:   

<p align="center"><img src="https://matthew-brett.github.io/teaching/_images/smoothing_intro-3.png"></img>
<img src="https://i2.wp.com/theailearner.com/wp-content/uploads/2019/05/normal4.png?resize=625%2C368&ssl=1"></img></p>      


Point A is on the edge ( in vertical direction). Gradient direction is normal to the edge. Point B and C are in gradient directions. So point A is checked with point B and C to see if it forms a local maximum. If so, it is considered for next stage, otherwise, it is suppressed ( put to zero).

In short, the result you get is a binary image with "thin edges" (like the figure on the right).
(Best description in [this link](https://www.youtube.com/watch?v=7mEiTU-XgCo&feature=youtu.be) (1:02:02))   
        
        
## 2) Consisting Gaussian Smoothing Kernel(Mask)
Each coefficient of kernel(= each element of mask matrix) is set based on Gaussian Distribution above. Also, so as to keep the brightness of the input image the same after smoothing, we should make a sum of kernel(mask) coefficients become '1'. See the matrix below:

<p align="center"><img src="https://homepages.inf.ed.ac.uk/rbf/HIPR2/figs/gausmask.gif"></img></p> 

After passing convolution process, this filter eventually smooths the image!

```python
import cv2
Blurred = cv2.GaussianBlur(image, ksize, 0)

cv2.imshow("Gaussian Filtering", Blurred)
cv2.waitKey(0)
```

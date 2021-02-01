<h1> Canny Edge Detection </h1>
<div align="center">한국어</div>
<br>
   
## 1) Noise elimination through *Gaussian Blurring*
Since edge detection is susceptible to noise in the image, first step is to remove the noise in the image with a 5x5 Gaussian filter.    
[Gaussian filter](https://github.com/AhnJunYeong0319/PoseEstimation/tree/main/CHAPTER7/Nonlinear%20Filtering)?
   
<br>   

## 2) Detect direction and intensity of pixel gradient using *Sobel mask*
Smoothened image is then filtered with a Sobel kernel in both horizontal and vertical direction to get first derivative in horizontal direction ( **Gx**) and vertical direction ( **Gy**). From these two images, we can find edge gradient and direction for each pixel as follows:   

<p align="center"><img src="https://www.programmersought.com/images/370/f6924c211ad02af5c0d54b29c6ced3a2.JPEG"></img></p>   

Gradient direction is always perpendicular to edges. It is rounded to one of four angles representing vertical, horizontal and two diagonal directions.   

[Sobel mask](https://github.com/AhnJunYeong0319/PoseEstimation/tree/main/CHAPTER7/1st%20Derivative%20Mask)?   
   
<br>   

## 3) Non-maximum suppression (left-top -> right-bottom)
After getting gradient magnitude and direction, a full scan of image is done to remove any unwanted pixels which may not constitute the edge. For this, at every pixel, pixel is checked if it is a local maximum in its neighborhood in the direction of gradient. Check the image below:   

<p align="center"><img src="https://docs.opencv.org/master/nms.jpg"></img>
<img src="https://developer.ibm.com/recipes/wp-content/uploads/sites/41/2019/11/non-max-suppression.png"></img></p>      


Point A is on the edge ( in vertical direction). Gradient direction is normal to the edge. Point B and C are in gradient directions. So point A is checked with point B and C to see if it forms a local maximum. If so, it is considered for next stage, otherwise, it is suppressed ( put to zero).

<u>In short, the result you get is a binary image with "thin edges" (like the figure on the right)</u>.
(Best description in [this link](https://www.youtube.com/watch?v=7mEiTU-XgCo&feature=youtu.be) (1:02:02))   
        
<br>   

## 4) Determine edges using *Hysteresis threshold*
This stage decides whether they are actual edges or not. For this, we need two threshold values, minVal and maxVal. Any edges with intensity gradient more than maxVal are sure to be edges and those below minVal are sure to be non-edges, so discarded. Those who lie between these two thresholds are classified edges or non-edges based on their connectivity. If they are connected to "sure-edge" pixels, they are considered to be part of edges. Otherwise, they are also discarded. See the image below:

<p align="center"><img src="https://docs.opencv.org/master/hysteresis.jpg"></img></p> 

The edge A is above the maxVal, so considered as "sure-edge". Although edge C is below maxVal, it is connected to edge A, so that also considered as valid edge and we get that full curve. But edge B, although it is above minVal and is in same region as that of edge C, it is not connected to any "sure-edge", so that is discarded. So it is very important that we have to select minVal and maxVal accordingly to get the correct result.

This stage also removes small pixels noises on the assumption that edges are long lines.

<u>So what we finally get in this process is strong edges in the image</u>.   

<br>
<br>
&lt;English Resources&gt;<br>
<ul>
        <li>https://www.youtube.com/watch?v=17cOHpSaqi0</li>
        <li>https://www.cs.ubc.ca/~lsigal/425_2018W2/Lecture8.pdf</li>
        <li>https://towardsdatascience.com/canny-edge-detection-step-by-step-in-python-computer-vision-b49c3a2d8123</li>
        <li>https://www.youtube.com/watch?v=7mEiTU-XgCo&feature=youtu.be (1:02:02)</li><br>
</ul>
&lt;Korean Resources&gt;<br>
<ul>
        <li>https://carstart.tistory.com/188</li>
        <li>https://m.blog.naver.com/PostView.nhn?blogId=jinsoo91zz&logNo=220511441402&proxyReferer=http:%2F%2Fm.blog.naver.com%2Fjinsoo91zz%2F220511441402</li>
        <li>https://m.blog.naver.com/PostView.nhn?blogId=jinsoo91zz&logNo=220511441402&proxyReferer=http:%2F%2Fm.blog.naver.com%2Fjinsoo91zz%2F220511441402</li>
</ul>

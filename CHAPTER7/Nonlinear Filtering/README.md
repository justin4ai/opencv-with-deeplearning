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
This stage decides which are all edges are really edges and which are not. For this, we need two threshold values, minVal and maxVal. Any edges with intensity gradient more than maxVal are sure to be edges and those below minVal are sure to be non-edges, so discarded. Those who lie between these two thresholds are classified edges or non-edges based on their connectivity. If they are connected to "sure-edge" pixels, they are considered to be part of edges. Otherwise, they are also discarded. See the image below:

<p align="center"><img src="https://homepages.inf.ed.ac.uk/rbf/HIPR2/figs/gausmask.gif"></img></p> 

The edge A is above the maxVal, so considered as "sure-edge". Although edge C is below maxVal, it is connected to edge A, so that also considered as valid edge and we get that full curve. But edge B, although it is above minVal and is in same region as that of edge C, it is not connected to any "sure-edge", so that is discarded. So it is very important that we have to select minVal and maxVal accordingly to get the correct result.

This stage also removes small pixels noises on the assumption that edges are long lines.

So what we finally get is strong edges in the image.   

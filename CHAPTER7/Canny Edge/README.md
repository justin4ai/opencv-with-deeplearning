## 1) Noise elimination through *Gaussian Blurring*
## 2) Detect direction and intensity of pixel gradient using *Sobel mask*
        에지의 방향과 기울기의 방향은 수직!
## 3) Non-maximum suppression

![img](https://docs.opencv.org/master/nms.jpg)   
현재 화소와 선택된 두 화소의 에지 강도를 비교하여 최대치가 아니면 억제, 최대치인 것만 에지로 결정 (좌측 상단 -> 우측 하단)
(Best description in [this link](https://www.youtube.com/watch?v=7mEiTU-XgCo&feature=youtu.be) (1:02:02))
        
## 4) Determine edges using *Hysteresis threshold*
![asd](https://docs.opencv.org/master/hysteresis.jpg)



<br>
<br>
&lt;English Materials&gt;<br>
<ul>
        <li>https://www.youtube.com/watch?v=17cOHpSaqi0</li>
        <li>https://www.cs.ubc.ca/~lsigal/425_2018W2/Lecture8.pdf</li>
        <li>https://towardsdatascience.com/canny-edge-detection-step-by-step-in-python-computer-vision-b49c3a2d8123</li>
        <li>https://www.youtube.com/watch?v=7mEiTU-XgCo&feature=youtu.be (1:02:02)</li><br>
</ul>
&lt;Korean Materials&gt;<br>
<ul>
        <li>https://carstart.tistory.com/188</li>
        <li>https://m.blog.naver.com/PostView.nhn?blogId=jinsoo91zz&logNo=220511441402&proxyReferer=http:%2F%2Fm.blog.naver.com%2Fjinsoo91zz%2F220511441402</li>
        <li>https://m.blog.naver.com/PostView.nhn?blogId=jinsoo91zz&logNo=220511441402&proxyReferer=http:%2F%2Fm.blog.naver.com%2Fjinsoo91zz%2F220511441402</li>
</ul>


```C++
#include<iostream>
int main() 
{ 
    std::cout <<"Hello, World!!"<< std::endl;
}
```

```python
for i in range(3):
    print(i)
```

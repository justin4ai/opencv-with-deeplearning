<h1> 캐니 에지 검출 </h1>
<div align="center"><a href="https://github.com/AhnJunYeong0319/PoseEstimation/blob/main/CHAPTER7/Canny%20Edge/README.md">English</a></div>
<br>
   
## 1) 가우시안 블러링을 사용한 노이즈 제거
에지 검출은 이미지 속의 노이즈에 크게 영향받기 때문에, 첫 단계는 5x5 가우시안 필터로 이미지 속 노이즈를 제거하는 것입니다.
[가우시안 필터란](https://github.com/AhnJunYeong0319/PoseEstimation/tree/main/CHAPTER7/Nonlinear%20Filtering)?
   
<br>   

## 2) 소벨 마스크를 이용한 방향 및 화소 기울기 강도 검출
블러된 이미지는 이제 1차 세로 방향 미분값 ( **Gy**) 과 가로 방향 미분값 ( **Gx**) 을 구하기 위해서, 소벨 마스크를 통해 가로 / 세로 방향 모두로 필터링됩니다. 아래의 두 수식으로부터 각 화소의 에지 기울기와 방향을 구할 수 있습니다.

<p align="center"><img src="https://www.programmersought.com/images/370/f6924c211ad02af5c0d54b29c6ced3a2.JPEG"></img></p>   

기울기 방향은 항상 에지와 수직입니다. 대략 네 방향을 지칭하게 되는데요, 수직, 수평, 그리고 대각으로 두 방향입니다.   

[소벨 마스크란](https://github.com/AhnJunYeong0319/PoseEstimation/tree/main/CHAPTER7/1st%20Derivative%20Mask)?   
   
<br>   

## 3) 비최대치 억제 (좌상단 -> 우하단)
기울기 강도와 방향을 구한 뒤, 엣지를 구성하지 않는 - 즉 우리가 원치 않은 - 화소를 제거하는 풀 스캔이 작동됩니다. 이 비최대치 억제를 위해서,
모든 화소에서 화소는 근방의 기울기 방향에서 지역 최대치 (local maximum) 인지 검사받습니다. 아래 그림을 확인하세요!

<p align="center"><img src="https://docs.opencv.org/master/nms.jpg"></img>
<img src="https://developer.ibm.com/recipes/wp-content/uploads/sites/41/2019/11/non-max-suppression.png"></img></p>      

점 A는 수직 방향으로 엣지에 놓여있습니다. 기울기 방향은 엣지에 맞습니다. 점 B와 C는 기울기 방향에 있습니다. 따라서 점 A는 점 B와 C를 통해 지역 최대치를 형성하는지 검사당합니다. 만약 그렇다면, 점 A는 다음 단계로 넘어가지만, 그렇지 않다면 억제됩니다 (0이 됩니다).

<u>한 마디로, 당신이 얻는 결과는 오른쪽 사진처럼 "얇은 엣지"를 가진 이진 이미지입니다.</u>
([이 링크](https://www.youtube.com/watch?v=7mEiTU-XgCo&feature=youtu.be) (1:02:02)에 아주 잘 설명되어있습니다.)   
        
<br>   

## 4) 이력 임계값으로 에지 검출
이 단계에선 진짜 에지인지 아닌지를 결정합니다. 이를 위해서, 우리는 두 가지 임계값이 필요합니다 - minVal과 maxVal. maxVal보다 높은 기울기 강도를 가진 에지는 에지로서 인정받고, minVal보다 낮은 강도를 가진 에지는 비(非)에지로 결정되어 버려집니다. 이 두 임계값 사이에 있는 에지들은 그들의 연결성에 기반하여 에지인지 아닌지 결정됩니다. 만약 '확실한 에지' 화소들과 연결되어있었다면, 에지의 일부로 인정받습니다. 아니라면 버려지겠죠? 아래 그림을 확인하세요.


<p align="center"><img src="https://docs.opencv.org/master/hysteresis.jpg"></img></p> 

에지 A는 maxVal보다 위에 있어, '확실한 에지'로 인정받았습니다. 에지 C는 maxVal보단 아래있지만, 에지 A와 연결되어있기 때문에 타당한 에지로 인정받았고 우리는 풀 커브를 얻게 됩니다. 하지만 에지 B는 minVal보단 위에 있고 에지 C와 같은 위치에 있으나, 그 어떤 '확실한 에지'와도 연결되지 않아 버려집니다. 따라서 우리가 minVal과 maxVal을 적절히 정하는 것은 올바른 결과를 얻기 위해선 매우 중요하겠죠.   

또한 이 절차는 에지가 긴 선형이라는 가정 하에 작은 픽셀단위 노이즈도 없애줍니다.


<u>따라서 우리가 이 과정에서 최종적으로 얻게 되는 것은 강력한 에지겠죠</u>.   

<br>
<br>
&lt;영어 자료&gt;<br>
<ul>
        <li>https://www.youtube.com/watch?v=17cOHpSaqi0</li>
        <li>https://www.cs.ubc.ca/~lsigal/425_2018W2/Lecture8.pdf</li>
        <li>https://towardsdatascience.com/canny-edge-detection-step-by-step-in-python-computer-vision-b49c3a2d8123</li>
        <li>https://www.youtube.com/watch?v=7mEiTU-XgCo&feature=youtu.be (1:02:02)</li><br>
</ul>
&lt;한국어 자료&gt;<br>
<ul>
        <li>https://carstart.tistory.com/188</li>
        <li>https://m.blog.naver.com/PostView.nhn?blogId=jinsoo91zz&logNo=220511441402&proxyReferer=http:%2F%2Fm.blog.naver.com%2Fjinsoo91zz%2F220511441402</li>
        <li>https://m.blog.naver.com/PostView.nhn?blogId=jinsoo91zz&logNo=220511441402&proxyReferer=http:%2F%2Fm.blog.naver.com%2Fjinsoo91zz%2F220511441402</li>
</ul>

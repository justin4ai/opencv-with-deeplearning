import cv2

image = cv2.imread("images/bright.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

dst1 = cv2.add(image, 100)  # saturate 방식
dst2 = cv2.subtract(image, 100)

dst3 = image + 100  # modulo 방식이라 이상함
dst4 = image - 100

cv2.imshow("original image", image)
cv2.imshow("dst1- bright:OpenCV", dst1)
cv2.imshow("dst2- dark:OpenCV", dst2)
cv2.imshow("dst3- bright:numpy", dst3)
cv2.imshow("dst4- dark:numpy", dst4)
cv2.waitKey(0)
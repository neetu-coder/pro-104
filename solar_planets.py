import cv2 

img = cv2.imread("solar-system.jpg")

cv2.putText(
          img,
          "sun",
          (20,300),
          cv2.FONT_HERSHEY_COMPLEX,
          0.5,
          (255,255,255)
        ),
cv2.putText(
          img,
          "mecuryy",
          (100,200),
          cv2.FONT_HERSHEY_COMPLEX,
          0.5,
          (255,255,255)
        ),
cv2.putText(
          img,
          "venus",
          (200,150),
          cv2.FONT_HERSHEY_COMPLEX,
          0.5,
          (255,255,255)
        ),
cv2.putText(
          img,
          "earth",
          (290,290),
          cv2.FONT_HERSHEY_COMPLEX,
          0.5,
          (255,255,255)
        ),
cv2.putText(
          img,
          "mars",
          (395,190),
          cv2.FONT_HERSHEY_COMPLEX,
          0.5,
          (255,255,255)
        ),
cv2.putText(
          img,
          "Jupiter",
          (500,400),
          cv2.FONT_HERSHEY_COMPLEX,
          0.5,
          (255,255,255)
        ),
cv2.putText(
          img,
          "Saturn",
          (800,150),
          cv2.FONT_HERSHEY_COMPLEX,
          0.5,
          (255,255,255)
        ),
cv2.putText(
          img,
          "Uranus",
          (995,300),
          cv2.FONT_HERSHEY_COMPLEX,
          0.5,
          (255,255,255)
        ),
cv2.putText(
          img,
          "Neptune",
          (1100,150),
          cv2.FONT_HERSHEY_COMPLEX,
          0.5,
          (255,255,255)
        )


cv2.imshow("output",img)
cv2.waitKey(0)

cv2.imwrite("solar-system.jpg",img)
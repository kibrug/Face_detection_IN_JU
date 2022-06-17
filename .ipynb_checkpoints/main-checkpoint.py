{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1988b3c3",
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "\n",
    "face_cascade = cv2.CascadeClassifier('face_detector.xml')\n",
    "\n",
    "img = cv2.imread('image.jpg')\n",
    "\n",
    "faces = face_cascade.detectMultiScale(img, 1.1, 4)\n",
    "\n",
    "for (x, y, w, h) in faces: \n",
    "  cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)\n",
    "cv2.imwrite(\"face_detected.png\", img) \n",
    "print('Successfully saved')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

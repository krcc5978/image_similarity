import cv2
from feature_check import FeatureCheck


class FeaturePoint(FeatureCheck):

    def __init__(self):
        self.detector = cv2.AKAZE_create()
        self.bf = cv2.BFMatcher(cv2.NORM_HAMMING)

    def get_score(self, img):
        (target_kp, target_des) = self.detector.detectAndCompute(img, None)
        return target_des

    def check_score(self, score1, score2):
        matches = self.bf.match(score1, score2)
        dist = [m.distance for m in matches]
        if not dist:
            return 10000
        else:
            return sum(dist) / len(dist)

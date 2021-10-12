import cv2
from feature_check import FeatureCheck


class Histgram(FeatureCheck):

    def __init__(self):
        pass

    def get_score(self, img):
        return cv2.calcHist([img], [0], None, [256], [0, 256])

    def check_score(self, score1, score2):
        ret = cv2.compareHist(score1, score2, 0)
        return ret

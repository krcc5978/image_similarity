import cv2
from feature_check import FeatureCheck


class Histgram(FeatureCheck):

    def __init__(self, mode):
        pass

    def get_score(self, img):
        return cv2.calcHist([img], [0], None, [256], [0, 256])

    def check_score(self, score1, score2):
        # 類似性の高いものが1 低いものが0になるため類似度の高いものを0、低いものを1とする
        ret = cv2.compareHist(score1, score2, 0)
        return (1 - ret)*100

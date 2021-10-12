from abc import ABCMeta, abstractmethod


class FeatureCheck(metaclass=ABCMeta):

    # @abstractmethod
    # def __init__(self):
    #     pass

    @abstractmethod
    def get_score(self, img):
        pass

    @abstractmethod
    def check_score(self, score1, score2):
        pass
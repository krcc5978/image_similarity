import imagehash
from PIL import Image
from feature_check import FeatureCheck


class ImageHash(FeatureCheck):

    def __init__(self, mode):
        self.mode = mode
        pass

    def get_score(self, img):
        image_pil = Image.fromarray(img)
        image_pil = image_pil.convert('RGB')

        if self.mode == 'a':
            return imagehash.average_hash(image_pil)
        elif self.mode == 'p':
            return imagehash.phash(image_pil)
        elif self.mode == 'd':
            return imagehash.dhash(image_pil)
        else:
            return imagehash.whash(image_pil)

    def check_score(self, score1, score2):
        return score2 - score1

import os
from glob import glob
import cv2

thresh = 10

if __name__ == '__main__':
    dir_path = 'D:\\t-asai\\project\\git\\movie_module\\new_CAM-J-09_fk_col1\\'

    img_path_list = []
    score_list = []
    result = []

    # TODO ここでどの判定式を使うか条件分岐を行う

    from feature_point import FeaturePoint as a
    # from histgram import Histgram as a
    # from image_hash import ImageHash as a

    check_score = a()

    for extension in ['png', 'jpg']:
        img_path_list.extend(glob(f'{dir_path}/*.{extension}'))

    for i, img_path in enumerate(img_path_list):
        print(img_path)
        img = cv2.imread(img_path)
        score_list.append(check_score.get_score(img))

    for i in range(len(img_path_list)):
        if img_path_list[i] in result:
            continue

        for j in range(i + 1, len(img_path_list)):

            if img_path_list[j] in result:
                continue

            compare_score = check_score.check_score(score_list[i], score_list[j])

            if compare_score < thresh:
                result.append(img_path_list[j])

    for a in result:
        os.remove(a)

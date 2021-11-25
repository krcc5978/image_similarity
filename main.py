import os
import sys
import argparse
from glob import glob
import cv2

parser = argparse.ArgumentParser(description='同一画像削除')

parser.add_argument('--input', help='ディレクトリパス', type=str, required=True)
parser.add_argument('--thresh', help='閾値', type=int, required=True)
parser.add_argument('--model', help='使用モデル', type=str)
parser.add_argument('--mode', help='動作設定', type=str)
parser.add_argument('--move_path', help='削除画像移動先パス（なければ削除）', type=str)

args = parser.parse_args()


if __name__ == '__main__':

    img_path_list = []
    score_list = []
    result = []

    if args.model == 'f':
        from feature_point import FeaturePoint as match_model
    elif args.model == 'h':
        from histgram import Histgram as match_model
    elif args.model == 'i':
        from image_hash import ImageHash as match_model
    else:
        print('適切な使用モデルを選択してください')
        print('f : 特徴点マッチング')
        print('h : ヒストグラムマッチング')
        print('i : 画像ハッシュマッチング')
        sys.exit(0)

    check_score = match_model(args.mode)

    for extension in ['png', 'jpg']:
        img_path_list.extend(glob(f'{args.input}/*.{extension}'))

    print('get score')
    for i, img_path in enumerate(img_path_list):
        print(img_path)
        img = cv2.imread(img_path)
        score_list.append(check_score.get_score(img))

    print('conpare_score')
    for i in range(len(img_path_list)):
        print(img_path_list[i])
        if img_path_list[i] in result:
            continue

        for j in range(i + 1, len(img_path_list)):

            if img_path_list[j] in result:
                continue

            compare_score = check_score.check_score(score_list[i], score_list[j])

            # 距離が近いものを削除用リストに設定
            if compare_score <= args.thresh:
                result.append(img_path_list[j])

    print('file move or delete')
    if args.move_path is None:
        for path in result:
            os.remove(path)
    else:
        os.makedirs(args.move_path, exist_ok=True)
        for path in result:
            file_name = path.split('\\')[-1]
            os.rename(path, '/'.join([args.move_path, file_name]))

from argparse import ArgumentParser
from typing import List, Any

import Mykytea
from tqdm import tqdm


def lcs(s1: List[Any], s2: List[Any]) -> int:
    l1, l2 = len(s1), len(s2)
    if l1 == 0 or l2 == 0:
        return 0

    # memorization of dp[l1][l2]
    dp: List[List[int]] = [[0] * l2 for _ in range(l1)]

    # Fill 0th row
    is_same_found = False
    for i in range(l1):
        if is_same_found or s1[i] == s2[0]:
            dp[i][0] = 1
            is_same_found = True

    # Fill 0th column
    is_same_found = False
    for j in range(l2):
        if is_same_found or s2[j] == s1[0]:
            dp[0][j] = 1
            is_same_found = True

    max_len = 0
    # dp[i][j] stores the maximum length of subsequence of s1[:i+1], s2[:j+1]
    for i in range(0, l1-1):
        for j in range(0, l2-1):
            if s1[i+1] == s2[j+1]:
                dp[i+1][j+1] = dp[i][j] + 1
                max_len = max(dp[i][j], max_len)
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

    return max_len


def main():
    parser = ArgumentParser()
    parser.add_argument('--model', type=str, help='path to trained kytea model')
    parser.add_argument('--test', type=str, help='path to test file')
    args = parser.parse_args()

    with open(args.test) as f:
        tests = [line.strip() for line in f]

    # You can pass arguments KyTea style like following
    # opt = "-deftag UNKNOWN!!"

    # You can also set your own model
    opt = f'-model {args.model}'

    mk = Mykytea.Mykytea(opt)

    l_cor, l_sys, l_lcs = 0, 0, 0
    for line in tqdm(tests):
        s = ''
        for w in line.split():
            first_char, _ = w.split('/')
            s += first_char
            # if len(first_char) == 1:
            #     if s and s[-1] != ' ':
            #         s += ' '
            #     s += first_char + ' '
            # elif len(first_char) == 2:
            #     s += first_char
            # else:
            #     raise ValueError('The length of characters before "/" must be 1 or 2.')

        # print(f'input: {s}')
        # segmented = []
        prediction = [word.tag[0][0][0] for word in mk.getTags(s)]
        # for seq in s.split():
        #     if len(seq) == 1:
        #         segmented.append(seq)
        #         prediction.append(seq)
        #     else:
        #         segmented += mk.getWS(seq)
        #         prediction += [word.tag[0][0][0] for word in mk.getTags(seq)]
        gold = [w.split('/')[1] for w in line.split()]
        # print('segmentation: ' + ' '.join(segmented))
        # print('prediction: ' + ' '.join(prediction))
        # print('gold: ' + ' '.join(gold))
        # print()

        # 評価
        l_cor += len(gold)
        l_sys += len(prediction)
        l_lcs += lcs(prediction, gold)

    recall = l_lcs / l_cor
    precision = l_lcs / l_sys
    f1_score = (2 * recall * precision) / (recall + precision)
    print(f'recall: {recall:0.3} ({l_lcs}/{l_cor})')
    print(f'precision: {precision:0.3} ({l_lcs}/{l_sys})')
    print(f'f1_score: {f1_score:0.3}')


if __name__ == '__main__':
    main()

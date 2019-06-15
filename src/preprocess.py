from argparse import ArgumentParser


def main():
    parser = ArgumentParser()
    parser.add_argument('--input', type=str, help='path to input file')
    parser.add_argument('--output', type=str, help='path to output file')
    args = parser.parse_args()

    with open(args.output, 'w') as fout:
        with open(args.input, 'r') as fin:
            for line in fin:
                if '&' in line or '/' in line:
                    continue
                words = line.strip().split()
                for word in words:
                    word = word.strip(',."')
                    if word:
                        fout.write(f'{word[:2]}/{word} ')
                fout.write('\n')


if __name__ == '__main__':
    main()

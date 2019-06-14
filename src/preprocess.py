from argparse import ArgumentParser


def main():
    parser = ArgumentParser()
    parser.add_argument('--input', type=str, help='path to input file')
    parser.add_argument('--output', type=str, help='path to output file')
    args = parser.parse_args()

    with open(args.output, 'w') as fout:
        with open(args.input, 'r') as fin:
            for line in fin:
                words = line.strip().split()
                fout.write(' '.join(f'{word[:2]}/{word}'for word in words) + '\n')


if __name__ == '__main__':
    main()

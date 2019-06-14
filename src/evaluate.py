import Mykytea


def show_tags(t):
    for word in t:
        out = word.surface + "\t"
        for t1 in word.tag:
            for t2 in t1:
                for t3 in t2:
                    out = out + "/" + str(t3)
                out += "\t"
            out += "\t"
        print(out)


# def list_tags(t):
#     def convert(t2):
#         return t2[0], type(t2[1])
#     return [(word.surface, [[convert(t2) for t2 in t1] for t1 in word.tag]) for word in t]


def main():
    # You can pass arguments KyTea style like following
    opt = "-deftag UNKNOWN!!"
    # You can also set your own model
    # opt = "-model /usr/local/share/kytea/model.bin"
    mk = Mykytea.Mykytea(opt)

    s = "今日はいい天気です。1999"

    # 分かち書きを取得
    for word in mk.getWS(s):
        print(word)

    # 解析結果を文字列で取得
    print(mk.getTagsToString(s))

    # 1位のタグを取得
    t = mk.getTags(s)
    show_tags(t)

    # すべてのタグを取得
    tt = mk.getAllTags(s)
    show_tags(tt)


if __name__ == '__main__':
    main()

import argparse


def get_parse_arguments():
    parser = argparse.ArgumentParser(description='test script')

    parser.add_argument('-f', help="filename", dest="filename", required=True)
    parser.add_argument('-p', help="process new text (to work faster later)", dest="process", const=True, nargs='?')

    parser.add_argument('-t', help="top words in text", dest="top", const=True, nargs='?')
    parser.add_argument('-n', help="number of top (default 5)", dest="value", type=int, default=5)
    parser.add_argument('-w', help="complete information about the use of a given word", dest="word", default='')
    parser.add_argument('-g', help="data on the use of words from a given group", dest="group", const=True, nargs='?')

    args = parser.parse_args()
    args_dict = vars(args)
    print(args_dict)
    return args_dict

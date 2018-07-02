import argparse

parser = argparse.ArgumentParser(prog='ls', usage='%(prog)s [options]')

parser.add_argument('-s', '--sort',  action='store_true', help='display files in order')
parser.add_argument('-f', '--file', action='store_true', help='display just files')
parser.add_argument('-d', '--directory', action='store_true', help='display just directory')
parser.add_argument('-l', '--detail', action='store_true', help='display files information')
parser.add_argument('files', nargs='*', help='the files need to display')

#parser.print_help()
args = parser.parse_args()
print(args)
print(args.detail)
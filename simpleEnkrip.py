from __future__ import print_function
from itertools import cycle
import argparse


def scramble(data, key):
    result = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(data, cycle(key)))
    return result


def main():
    ap = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description='Simple Enkrip Dekrip Program'
    )

    ap.add_argument('-k', '--key', default='R4h4514', help='Key untuk enkripsi')
    ap.add_argument('-i', '--input', required=True, help='Nama file input')
    ap.add_argument('-o', '--output', help='Nama file output', default='output.txt')
    ap.add_argument('-p', '--print', action='store_true', default=False, help='Langsung tampilkan hasil')
    args = vars(ap.parse_args())

    if args['print']:
        print(scramble(args['input'], args['key']))
    else:
        try:
            data = open(args['input'], mode='r', encoding='utf-8').read()
        except FileNotFoundError:
            print('File tidak ditemukan')
            argparse._sys.exit(1)
        except:
            print('Gagal!\nMaaf file tidak didukung')
            argparse._sys.exit(1)

        task = scramble(data, args['key'])
        save = open(args['output'], mode='w', encoding='utf-8')
        save.write(task)
        save.close()


if __name__ == '__main__':
    try:
        FileNotFoundError
    except NameError:
        FileNotFoundError = IOError
    main()

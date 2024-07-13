# -*- coding: utf-8 -*
from __future__ import print_function
import sys,os,re,subprocess

NumRe = re.compile(r'^([0-9]+)\.')

def rename_func(dir_path):
    for f in os.listdir(dir_path):
        sourceF = os.path.join(dir_path,f)
        if os.path.isfile(sourceF):
            bn = os.path.basename(sourceF)
            gp = NumRe.findall(bn)
            if len(gp) > 0:
                dn = os.path.dirname(sourceF)
                dir_name = os.path.basename(dn)
                new_name = os.path.join(dn, f.replace(gp[0], '{}{}'.format(dir_name, gp[0])))
                os.rename(sourceF, new_name)
                print('rename {} to {}'.format(sourceF, new_name))

        elif os.path.isdir(sourceF):
            rename_func(sourceF)


def main():
    pwd = os.getcwd()
    rename_func(pwd)
    pass

if __name__ == "__main__":
    main()
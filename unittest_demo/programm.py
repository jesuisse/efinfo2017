# encoding: utf-8
__author__ = 'pax'

def hallo_welt(name):
    if name == '':
        return "Hallo"
    else:
        return "Hallo " + name

def quadrat(x):
    return x * x

if __name__ == '__main__':
    print(hallo_welt("Homer Simpson"))
    print("Das Quadrat von 5 ist", quadrat(5))

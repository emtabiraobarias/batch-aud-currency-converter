import currencyconverter
import sys

if __name__ == '__main__':
    output = currencyconverter.convert_to_aud('main-input/input.csv', 'main-input/currencyconversiondata.csv')
    for line in output:
        sys.stdout.writelines(','.join([str(x) for x in line]) + '\n')

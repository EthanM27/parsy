#! /usr/bin/python3

import atheris
import sys

with atheris.instrument_imports():
    import parsy


@atheris.instrument_func
def test_input(input_bytes):
    fdp = atheris.FuzzedDataProvider(input_bytes)
    input_string = fdp.ConsumeUnicodeNoSurrogates(sys.maxsize)
    
    for char in input_string:
        ret = parsy.char_from(input_string).parse(char)

        if not ret:
            raise Exception('Expected char not found in input string')

        if not (ret in input_string):
            raise Exception('Found character is not actually in input string')
    
    
    # return input_bytes

def main():
    atheris.Setup(sys.argv, test_input)
    atheris.Fuzz()

if __name__ == "__main__":
    main()

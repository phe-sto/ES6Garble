# -*- coding: utf-8 -*-

import gzip
import sys
from jsmin import jsmin

import unidecode

COMPRESS_OBJ = {
    "yes": True,
    "no": False
}


class GarbleException(Exception):
    pass


def garble(input_path, output_path, compress=False):
    """
    Function garble the JS to the Extreme
       :param input_path: Path of the input JS to garble
       :param output_path: Path of the garbled JS
       :param compress: yes or no describing if conversion needed or not
    """
    # letters / numbers
    symbols = {
        'a': '((!!+[]+"")[+!![]])',
        'b': '((({})+"")[(+!![])+(+!![])])',
        'c': '((({})+"")[(+!![])+(+!![])+(+!![])+(+!![])+(+!![])])',
        'd': '((({})[""]+"")[(+!![])+(+!![])])',
        'e': '((!!+[]+"")[(+!![])+(+!![])+(+!![])+(+!![])])',
        'f': '((!!+[]+"")[+[]])',
        'g': '"\\x67"',
        'h': '"\\x68"',
        'i': '((+!![]/+[]+"")[(+!![])+(+!![])+(+!![])])',
        'j': '((({})+"")[(+!![])+(+!![])+(+!![])])',
        'k': '"\\x6B"',
        'l': '((!!+[]+"")[(+!![])+(+!![])])',
        'm': '"\\x6D"',
        'n': '((+!![]/+[]+"")[+!![]])',
        'o': '((({})+"")[+!![]])',
        'p': '"\\x70"',
        'q': '"\\x71"',
        'r': '((!+[]+"")[+!![]])',
        's': '((!!+[]+"")[(+!![])+(+!![])+(+!![])])',
        't': '((!+[]+"")[+[]])',
        'u': '((!+[]+"")[(+!![])+(+!![])])',
        'v': '"\\x76"',
        'w': '"\\x77"',
        'x': "'x'",
        'y': '((+!![]/+[]+"")[(+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![])])',
        'z': '"\\x7A"',
        'A': '"\\x41"',
        'B': '"\\x42"',
        'C': '"\\x43"',
        'D': '"\\x44"',
        'E': '"\\x45"',
        'F': '"\\x46"',
        'G': '"\\x47"',
        'H': '"\\x48"',
        'I': '((+!![]/+[]+"")[+[]])',
        'J': '"\\x4A"',
        'K': '"\\x4B"',
        'L': '"\\x4C"',
        'M': '"\\x4D"',
        'N': '((+[]/+[]+"")[+[]])',
        'O': '((({})+"")[(+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![])])',
        'P': '"\\x50"',
        'Q': '"\\x51"',
        'R': '"\\x52"',
        'S': '"\\x53"',
        'T': '"\\x54"',
        'U': '"\\x55"',
        'V': '"\\x56"',
        'W': '"\\x57"',
        'X': '"\\x58"',
        'Y': '"\\x59"',
        'Z': '"\\x5A"',
        "(": "'('",
        ")": "')'",
        "{": "'{'",
        "}": "'}'",
        "[": "'['",
        "]": "']'",
        ".": "'.'",
        ";": "';'",
        "@": "'@'",
        "*": "'*'",
        '"': "'\"'",
        "/": "'/'",
        ":": "':'",
        ",": "','",
        "'": '"\'"',
        "=": "'='",
        ">": "'>'",
        "<": "'<'",
        "!": "'!'",
        "$": "'$'",
        "_": "'_'",
        "#": "'#'",
        "+": "'+'",
        "-": "'-'",
        "%": "'%'",
        " ": "' '",
        "?": "'?'",
        "|": "'|'",
        "^": "'^'",
        "&": "'&'",
        "~": "'~'",
        "\n": "'\\n'",
        "\\": "'\\\\'",
        "0": "(+[])",
        "1": "(+!![])",
        "2": "((+!![])+(+!![]))",
        "3": "((+!![])+(+!![])+(+!![]))",
        "4": "((+!![])+(+!![])+(+!![])+(+!![]))",
        "5": "((+!![])+(+!![])+(+!![])+(+!![])+(+!![]))",
        "6": "((+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![]))",
        "7": "((+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![]))",
        "8": "((+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![]))",
        "9": "((+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![]))"
    }

    file_contents = open(input_path, 'r').read()

    file_contents_unicoded = str(file_contents)
    file_contents_ununicoded = unidecode.unidecode(file_contents_unicoded)

    replaced_reserved_1 = file_contents_ununicoded.replace(".deleteExpando", ".replaceLaterExpando");
    replaced_reserved_2 = replaced_reserved_1.replace(".delete", "['delete']");
    replaced_reserved_3 = replaced_reserved_2.replace(".replaceLaterExpando", ".deleteExpando");
    replaced_reserved_4 = replaced_reserved_3.replace(".catch", "['catch']");

    minified = jsmin(replaced_reserved_4, quote_chars="'\"`")

    transformed = []
    output_file = open(output_path, 'w+')
    output_file.write(
        "[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]][([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]](")

    for i in range(len(minified)):
        if i == 0:
            transformed.append(symbols[minified[i]] + "+")
        elif i == len(minified) - 1:
            transformed.append(symbols[minified[i]])
        else:
            transformed.append(symbols[minified[i]] + "+")
    output_file.write("".join(transformed))
    output_file.write(")()")
    output_file.close()

    if compress is False:
        f_in = open(output_path, 'rb')
        f_out = gzip.open(output_path + ".gz", 'wb')
        f_out.writelines(f_in)
        f_out.close()
        f_in.close()


if __name__ == "__main__":
    # execute only if run as a script
    if len(sys.argv) < 3:
        raise GarbleException(
            "please specify an input file, output file and if yes or no you would like to use compression.")
    try:
        garble(sys.argv[1], sys.argv[2], COMPRESS_OBJ[sys.argv[3]])
    except KeyError:
        raise GarbleException("third argument for compression must be yes or no")


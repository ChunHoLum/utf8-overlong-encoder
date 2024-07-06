#!/usr/bin/env python3

import sys
import argparse
from typing import List, Tuple

def to_overlong_utf8(char: str, bytes_count: int) -> bytes:
    ascii_value = ord(char)
    if bytes_count == 2:
        return bytes([0xC0 | (ascii_value >> 6),
                      0x80 | (ascii_value & 0x3F)])
    elif bytes_count == 3:
        return bytes([0xE0 | (ascii_value >> 12),
                      0x80 | ((ascii_value >> 6) & 0x3F),
                      0x80 | (ascii_value & 0x3F)])
    elif bytes_count == 4:
        return bytes([0xF0 | (ascii_value >> 18),
                      0x80 | ((ascii_value >> 12) & 0x3F),
                      0x80 | ((ascii_value >> 6) & 0x3F),
                      0x80 | (ascii_value & 0x3F)])
    else:
        return char.encode('utf-8')

def bytes_to_hex_string(b: bytes) -> str:
    return ''.join(f'\\x{byte:02X}' for byte in b)

def encode_string(input_string: str, byte_length: str) -> List[Tuple[str, str, str]]:
    results = []
    for char in input_string:
        unicode_value = ord(char)
        if byte_length == 'normal':
            encoded = char.encode('utf-8')
        else:
            encoded = to_overlong_utf8(char, int(byte_length))
        
        results.append((
            char,
            f"U+{unicode_value:04X}",
            bytes_to_hex_string(encoded)
        ))
    return results

def print_table(results: List[Tuple[str, str, str]], byte_length: str ) -> None:
    headers = ["Char", "Unicode", f"Encoded ({byte_length}-byte-long)"]
    widths = [4, 8, len(f"Encoded ({byte_length}-byte-long)")]
    
    def print_separator():
        print("+-" + "-+-".join("-" * width for width in widths) + "-+")

    def print_row(columns):
        print("| " + " | ".join(col.ljust(width) for col, width in zip(columns, widths)) + " |")

    print_separator()
    print_row(headers)
    print_separator()
    
    for row in results:
        print_row(row)
    
    print_separator()

def print_string(results: List[Tuple[str, str, str]]):
    bs = ''
    for char, unicode, encoded in results:
        bs += encoded
    print(bs)

def main():
    parser = argparse.ArgumentParser(description="Encode text to UTF-8 or overlong UTF-8.")
    parser.add_argument("input", nargs="?", help="Input string to encode. If not provided, reads from stdin.")
    parser.add_argument("-b", "--byte-length", choices=['normal', '2', '3', '4'], default='normal',
                        help="Byte length for encoding. 'normal' for standard UTF-8, or 2, 3, 4 for overlong encoding.")
    parser.add_argument("-f", "--format", choices=['table', 'string'], default='string',
                        help="Output format. 'table' for tabular format, 'string' for simple string output.")
    
    args = parser.parse_args()

    if args.input:
        input_string = args.input
    else:
        input_string = sys.stdin.read().strip()

    results = encode_string(input_string, args.byte_length)

    if args.format == 'table':
        print_table(results, args.byte_length)
    else:
        print_string(results)

if __name__ == "__main__":
    main()
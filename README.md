# UTF-8 Encoder

## Description

This command-line tool allows you to encode text into UTF-8 or overlong UTF-8 format. It provides options for different byte lengths in encoding and multiple output formats. This tool is useful for educational purposes, debugging, or exploring UTF-8 encoding behaviors.

Key features:

- Encode text to standard UTF-8 or overlong UTF-8 (normal, 2, 3, or 4 bytes)
- Accept input from command line arguments or through pipes
- Output in table or string format

## Installation

1. Ensure you have Python 3.6 or later installed on your system.
2. Copy the `utf8_overlong_encoder.py` script to your local machine.
3. Make the script executable:

```sh
chmod +x utf8_overlong_encoder.py
```

## Usage

`utf8_overlong_encoder.py [-h] [-b {normal,2,3,4}] [-f {table,string}] [input]`

Arguments:

- `input`: The text to encode. If not provided, the script reads from stdin.

Options:

- `-h`, `--help`: Show the help message and exit.
- `-b {normal,2,3,4}`, `--byte-length {normal,2,3,4}`: Byte length for encoding.
  - `normal`: standard UTF-8 (default)
  - `2`, `3`, `4`: overlong encoding with specified number of bytes
- `-f {string,table}`, `--format {string,table}`: Output format.
  - `string`: Display results as simple strings (default)
  - `table`: Display results in a tabular format

## Examples

1. Normal UTF-8 encoding

```sh
./utf8_overlong_encoder.py "../"
# \x2E\x2E\x2F
```

1. Encode a string using standard UTF-8 and display in table format:

```sh
./utf8_overlong_encoder.py "../" -b normal -f table
#+------+----------+----------------------------+
#| Char | Unicode  | Encoded (normal-byte-long) |
#+------+----------+----------------------------+
#| .    | U+002E   | \x2E                       |
#| .    | U+002E   | \x2E                       |
#| /    | U+002F   | \x2F                       |
#+------+----------+----------------------------+
```

2. Encode a string using 3-byte overlong encoding and display as a string:

```sh
./utf8_overlong_encoder.py "../" -b 3 -f string
# \xE0\x80\xAE\xE0\x80\xAE\xE0\x80\xAF
```

3. Pipe input to the script and use 4-byte overlong encoding:

```sh
echo "../" | ./utf8_overlong_encoder.py -b 4 -f string
# \xF0\x80\x80\xAE\xF0\x80\x80\xAE\xF0\x80\x80\xAF
```

### CVE related to UTF8 overlong

https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=overlong+utf

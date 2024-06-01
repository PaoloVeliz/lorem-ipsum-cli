# lorem-ipsum-cli

A Python-based command-line tool to generate Lorem Ipsum text. Customize the number of paragraphs and words per paragraph. The generated text is automatically copied to the clipboard for easy pasting. Perfect for quick placeholder text generation.

## Features

- Generate Lorem Ipsum text with a customizable number of paragraphs and words.
- Automatically copies the generated text to the clipboard.
- Easy to use from the terminal/command line.

## Installation

### Prerequisites

- Python 3.x
- `pyperclip` library

### Install Python Libraries

First, install the required Python library:

```bash
pip install pyperclip
```
## Clone the respository
Clone the repository to your local machine:
```bash
git clone https://github.com/PaoloVeliz/lorem-ipsum-cli.git
cd lorem-ipsum-cli
```

## Usage
### Linux and Mac
1. Make the Script Executable:
```bash
chmod +x lorem_ipsum.py
```

2. Move the Script to a Directory in Your PATH (optional):
```bash
sudo mv lorem_ipsum.py /usr/local/bin/lorem-ipsum
```
3. Run the Script:
```bash
./lorem_ipsum.py -p 2 -l 50
```

Or, if you moved it to /usr/local/bin:
```bash
lorem-ipsum -p 2 -l 50
```

### Windows
1. Create a Batch File:
    Create a new file named lorem-ipsum.bat and add the following line, adjusting the path to the location of lorem_ipsum.py:
```bash
@echo off
python C:\path\to\lorem_ipsum.py %*
```

2. Run the Script:
```bash
lorem-ipsum -p 2 -l 50
```
## Script Options
* `-p`, `--paragraphs`: Number of paragraphs (default: 1)
* `-l`, `--words`: Number of words per paragraph (default: 100)

## Examples
* Generate 1 paragraph with the default 100 words:
```bash
lorem-ipsum
```
* Generate 3 paragraphs with 50 words each:
```bash
lorem-ipsum -p 3 -l 50
```
* Generate 5 paragraphs with 200 words each:
```bash
lorem-ipsum -p 5 -l 200
```

# License
This project is licensed under the MIT License. See the LICENSE file for details.

This README provides a clear description, installation steps, and usage instructions for users on Linux, Mac, and Windows.

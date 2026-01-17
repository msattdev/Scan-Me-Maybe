# Scan-Me-Maybe

A simple QR code generator built with Python.

## Features

- Generate QR codes from text or URLs
- Save QR codes as PNG images with rounded corners (default)
- Multiple style options: Classic or Modern Blue
- High error correction for better scanability
- Custom color support
- Modern, polished UI with ASCII art logo
- Fast and lightweight

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/Scan-Me-Maybe.git
cd Scan-Me-Maybe
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the scanner:
```bash
python3 scanmemaybe.py
```

The program will prompt you to:
1. Enter the data to encode in the QR code
2. Specify a filename (default: `qrcode.png`)
3. Choose a style:
   - **Style 1 (Classic)**: Black and white QR code with rounded corners
   - **Style 2 (Modern Blue)**: Blue and white QR code with padding and rounded corners

This will generate a QR code image with beautiful rounded corners that you can scan with any QR code reader.

## Example

![QR Code Example](qrcode.png)

## Requirements

- Python 3.x
- qrcode
- Pillow (PIL)

## Project Structure

- `scanmemaybe.py` - Main QR code generator script
- `ascii_art.py` - ASCII art definitions for the UI
- `requirements.txt` - Project dependencies
- `README.md` - Project documentation

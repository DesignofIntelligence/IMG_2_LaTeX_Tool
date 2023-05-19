# Description
This project wraps pix2tex into a screenshot tool.

# Usage
Press Ctrl+alt+shift on the top left corner of the image to enter the screenshot mode. then press the same combination again on the bottom right corner of the image, then the latex will be copied to clipboard.
To escape the screenshot mode, you can press escape.

# Installation

Create a conda env named latexocr_trial, then run the following commands.
```
pip install pix2tex pyperclip pyautogui pynput
python -m pip install windows_toasts
```

Run the main.bat
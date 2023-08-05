# Description
This project wraps pix2tex into a screenshot tool.

# Usage
Press Ctrl+alt+shift on the top left corner of the image to enter the screenshot mode. then press the same combination again on the bottom right corner of the image, then the latex will be copied to clipboard.
To escape the screenshot mode, you can press escape.

# Installation

First Install miniconda3 by downloading the file, then run it
```
bash miniconda3_installer.sh
~/miniconda3/bin/conda create --name mathlatex
source ~/anaconda3/etc/profile.d/conda.sh
conda activate mathlatex
```
to take screenshots you need scrot
```bash
sudo apt-get install scrot xclip
```
Then install the following libraries

```
pip install pix2tex pyperclip pyautogui pynput
python -m pip install windows_toasts
```

if you get an error in the first command, you can add the following flag
```
--break-system-packages
```

Run the main.bat

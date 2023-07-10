# colorthon

## easy text color and print text pretty on terminal , cmd , console 

```bash
#windows
pip install colorthon
# linux
pip3 install colorthon
```
### How to import To Project:
```python
from colorthon import console

red = console.red
green = console.green
yellow = console.yellow
white = console.white
blue = console.blue
magenta = console.magenta
cyan = console.cyan
grey = console.grey
# reset or format text color :
reset = console.reset
```
### How To Use Colorthon In My Script:
```python
print(red, 'RED COLOR TEXT', reset)
print(green, "GREEN COLOR TEXT", reset)
print(yellow, 'Yellow Text Color And Format', reset, cyan, 'CYAN COLOR TEXT ', reset)
print(f"{magenta}MAGENTA COLOR TEXT{reset} {white}WHITE NORMAL COLOR TEXT{reset}")
```


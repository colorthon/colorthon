# Colorthon

Colorthon is a powerful Python package that provides a simple and intuitive way to work with colors in the terminal.

## Features

- Easy-to-use syntax for applying colors and background colors to text in the terminal.
- Supports a wide range of colors and background colors.
- Lightweight and efficient implementation.

## Installation

You can install Colorthon using pip:

```shell
pip install colorthon
# linux 
pip3 install colorthon
```

## Usage

To start using Colorthon, import the Colors and Back modules:

```python
from colorthon import Colors, Back

```
Now, you can use the color and background color codes provided by Colorthon. For example, you can define the following color variables:

```python
from colorthon import Colors, Back

# text color
red = Colors.RED
green = Colors.GREEN
blue = Colors.BLUE
black = Colors.BLACK
magenta = Colors.MAGENTA
yellow = Colors.YELLOW
cyan = Colors.CYAN
white = Colors.WHITE
# Text background Color (back text)
on_red = Back.RED
on_green = Back.GREEN
on_blue = Back.BLUE
on_yellow = Back.YELLOW
on_white = Back.WHITE
on_magenta = Back.MAGENTA
on_cyan = Back.CYAN
on_black = Back.BLACK
# Reset Format
reset = Colors.RESET
```

These variables allow you to easily apply colors and background colors to your text. Here's an example usage:

```python
print(f"{red}This text is red.{reset}")
print(f"{green}This text is green.{reset}")
print(f"{on_red}This text has a red background.{reset}")
print(f"{on_green}This text has a green background.{reset}")

```
### Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request. Make sure to read our Contribution Guidelines before getting started.

## License

This project is licensed under the MIT License.
Contact

If you have any questions or need support, feel free to reach out to us at pymmdrza@gmail.com We'd be happy to assist you!


other package :

**_Blockthon_** - _Generate Easy and Fast Private Key & Mnemonic and Decimal , Binary & seed (Bytes)_ , Compress and UnCompress address Bitcoin , Ethereum , TRON, Dogecoin, Litecoin, zcash, Digibyte, Dash, Qtum, Ravencoin, BitcoinGold

programmer and Owner Website : [Mmdrza.Com](https://mmdrza.com)


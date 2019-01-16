# HYPERJSONIFY

### Description

Converts color schemes from [terminal.sexy](https://terminal.sexy/) to a format that is compatible with [hyper.js](https://hyper.is)

### Prerequisites

python3 - `sudo apt install python3`

### Installation

`chmod +x install.sh`

`./install.sh`

### Use

##### Get a file

Go to [terminal.sexy](https://terminal.sexy/) and select or build a color scheme.

Under the `Export` tab, set `Format` to `JSON Scheme`.

Click the `Export` button, then `Download` and save the file.

##### Run the script

`hyperjsonify.py /path/to/filename.txt`

Copy and paste output at top of `.hyper.js`

```javascript
// Future versions of Hyper may add additional config options,
// which will not automatically be merged into this file.
// See https://hyper.is#cfg for all currently supported options.

let tomorrow_dark = {'colors': {'black': '#1d1f21', 'red': '#cc6666', 'green': '#b5bd68', 'yellow': '#f0c674', 'blue': '#81a2be', 'magenta': '#b294bb', 'cyan': '#8abeb7', 'white': '#c5c8c6', 'lightBlack': '#969896', 'lightRed': '#cc6666', 'lightGreen': '#b5bd68', 'lightYellow': '#f0c674', 'lightBlue': '#81a2be', 'lightMagenta': '#b294bb', 'lightCyan': '#8abeb7', 'lightWhite': '#ffffff'}, 'foreground': '#c5c8c6', 'background': '#1d1f21'};
let monokai_dark = {'colors': {'black': '#272822', 'red': '#f92672', 'green': '#a6e22e', 'yellow': '#f4bf75', 'blue': '#66d9ef', 'magenta': '#ae81ff', 'cyan': '#a1efe4', 'white': '#f8f8f2', 'lightBlack': '#75715e', 'lightRed': '#f92672', 'lightGreen': '#a6e22e', 'lightYellow': '#f4bf75', 'lightBlue': '#66d9ef', 'lightMagenta': '#ae81ff', 'lightCyan': '#a1efe4', 'lightWhite': '#f9f8f5'}, 'foreground': '#f8f8f2', 'background': '#272822'};

// Select which scheme you would like to use
let colorscheme = monokai_dark;

module.exports = {
  config: {
```

Make sure to set your `colorscheme` variable!

##### One-Time Configuration

```javascript
// color of the text
foregroundColor: colorscheme['foreground'],

// terminal background color
// opacity is only supported on macOS
backgroundColor: colorscheme['background'],

...

// the full list. if you're going to provide the full color palette,
// including the 6 x 6 color cubes and the grayscale map, just provide
// an array here instead of a color map object
colors: colorscheme['colors'],
```
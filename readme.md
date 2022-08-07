# What is this?
Script that convert and resize svg file to png.

# Why?
To generate icons for Qt projects.


# Dependencies

## Pillow (HPND License)
https://github.com/python-pillow/Pillow

## svglibs (GPL)
https://github.com/deeplook/svglib

```
pip3 install svglib pillow
```

## Example
```python3
python main.py --svg_files_dir svgs --outdir 20x20 --resize_x 20 --resize_y 20
```

# memo
https://standards.freedesktop.org/icon-theme-spec/icon-theme-spec-latest.html

https://www.gnu.org/licenses/license-list.en.html

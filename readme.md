# What is this?
Script that convert and resize svg files to png format.

# Why?
To generate icons for Qt projects.


# Dependencies

## Pillow (HPND License)
https://github.com/python-pillow/Pillow

## svglibs (GNU LGPLv3)
https://github.com/deeplook/svglib

```
pip install svglib pillow
```

## Example
```python3
python main.py --svg_files_dir svgs --outdir 20x20 --resize_x 20 --resize_y 20
```
This will create directory named '20x20' in current direcoty.  
Convert all .svg files to png and resize them to 20*20.  
Then save png files in the created directory.  

# memo
https://standards.freedesktop.org/icon-theme-spec/icon-theme-spec-latest.html

https://www.gnu.org/licenses/license-list.en.html

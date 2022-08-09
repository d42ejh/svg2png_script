from io import BytesIO
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
from PIL import Image
import os
from argparse import ArgumentParser
from pathlib import Path

def parse_args():
    parser=ArgumentParser('TODO')
    parser.add_argument('--svg_files_dir',required=True,dest='svg_dir',help='')
    parser.add_argument('--outdir',required=True,dest='out_dir_name',help='Out put directory name.(  /current direcoty path/out_dir_name  )')
    parser.add_argument('--resize_x',required=True,type=int,dest='resize_x')
    parser.add_argument('--resize_y',required=True,type=int,dest='resize_y')
    return parser.parse_args()

def svg2png(svg_file_path)->BytesIO:
    buffer= BytesIO()
    drawing = svg2rlg(svg_file_path)
    renderPM.drawToFile(drawing, buffer, fmt="PNG")
    return buffer
    

def main():
    args= parse_args()
    svg_dir=Path(args.svg_dir)
    resize_x=args.resize_x
    resize_y=args.resize_y
    out_dir_name=args.out_dir_name

    current_dir=Path(os.curdir)
    assert(current_dir.is_dir() and current_dir.exists())
    # create output dir
    out_dir=current_dir/ out_dir_name
    if out_dir.exists():
        print('[!] {} already exists.'.format(out_dir))
        return
    
    os.mkdir(out_dir)

    if not svg_dir.is_dir() or not svg_dir.exists():
        print('[!] Invalid target svg directory: {}'.format(svg_dir))
        return
    
    for svg_path in svg_dir.glob("*.svg"):
        svg_path:Path=svg_path
        assert(svg_path.is_file())

        
        buffer= svg2png(svg_path)

        #resize png
        img=Image.open(buffer)
        img= img.resize((resize_x,resize_y))
        name=svg_path.stem+'.png'
        out= out_dir.joinpath(name)
        img.save(out)

    print('Done.')
        




    

    



if __name__ =='__main__':
    main()

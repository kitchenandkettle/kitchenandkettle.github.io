from PIL import Image, ImageDraw, ImageFont

W=H=2000
PAPER=(245,240,232); INK=(44,36,22); CLAY=(160,133,94); SAGE=(125,139,111)
SERIF='/usr/share/fonts/liberation/LiberationSerif-Regular.ttf'
SANS='/usr/share/fonts/liberation/LiberationSans-Regular.ttf'
OUT='/home/chels/test/digital-products/homesteaders-almanac'

def make_card(filename,title,subtitle,bullets,note):
    img=Image.new('RGB',(W,H),PAPER); d=ImageDraw.Draw(img)
    tf=ImageFont.truetype(SERIF,140)
    if d.textbbox((0,0),title,font=tf)[2]>1800: tf=ImageFont.truetype(SERIF,105)
    sf=ImageFont.truetype(SERIF,52); bf=ImageFont.truetype(SERIF,48); nf=ImageFont.truetype(SANS,28); brand=ImageFont.truetype(SANS,28)
    th=d.textbbox((0,0),title,font=tf)[3]; sh=d.textbbox((0,0),subtitle,font=sf)[3]; bh=d.textbbox((0,0),'Test',font=bf)[3]; nh=d.textbbox((0,0),note,font=nf)[3]
    total=th+40+sh+40+sum((bh+18) for _ in bullets)+50+nh
    y=(H-total)//2; x=530
    title_width=d.textbbox((0,0),title,font=tf)[2]
    title_x=(W-title_width)//2 if filename.endswith('homesteaders-almanac-image-2.png') else x
    d.text((title_x,y),title,font=tf,fill=INK); y+=th+40
    d.text((x,y),subtitle,font=sf,fill=SAGE); y+=sh+40
    for line in bullets:
        d.text((x,y),line,font=bf,fill=INK); y+=bh+18
    y+=32; d.text((x,y),note,font=nf,fill=SAGE); d.text((100,1920),'Kitchen & Kettle',font=brand,fill=CLAY)
    img.save(filename,'PNG',optimize=True)

make_card(OUT+'/homesteaders-almanac-image.png',"What's Inside","A year at a time, kept in your own words",[
'•  The dates that make a place itself',
'•  Four seasonal pages for weather, work,',
'   harvests, animals, and small observations',
'•  Space for what worked and what changed',
'•  A yearly reflection to carry forward',
'•  A ten-year index for the longer story',
],'11 pages · printable PDF')
make_card(OUT+'/homesteaders-almanac-image-2.png',"A Record, Not a Tracker","For the things worth remembering",[
'•  First frost. First tomato. First snow.',
'•  The winter the hens stopped laying.',
'•  The repair that held — and the one that did not.',
'•  Write by hand or type in the browser.',
'•  Entries save automatically on your device.',
],'Fill-in-your-own · Kitchen & Kettle')

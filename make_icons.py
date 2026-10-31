# Draws the VYTHORA emblem into the PNGs that @capacitor/assets turns into launcher icons and splash screens.
import os
from PIL import Image, ImageDraw, ImageFilter
BG=(5,10,20,255)
L=[(6,8),(28,8),(50,58),(50,94)]; R=[(94,8),(72,8),(50,58),(50,94)]
CORE=[(37,8),(44,8),(50,22),(56,8),(63,8),(50,38)]
LINES=[[(3,26),(10,26),(16,36)],[(3,48),(9,48),(18,64)],[(97,26),(90,26),(84,36)],[(97,48),(91,48),(82,64)]]
def emblem(size,frac,bg):
    S=size*2; im=Image.new('RGBA',(S,S),bg if bg else (0,0,0,0)); u=S*frac/94
    P=lambda pts:[(S/2+(x-50)*u,S/2+(y-51)*u) for x,y in pts]
    glow=Image.new('RGBA',(S,S),(0,0,0,0)); g=ImageDraw.Draw(glow); w=max(2,int(u*1.6))
    g.polygon(P(CORE),fill=(255,40,80,255)); g.line(P([(28,8),(50,58),(72,8)]),fill=(255,40,80,255),width=w)
    for l in LINES: g.line(P(l),fill=(255,51,85,255),width=max(2,int(u*.8)))
    glow=glow.filter(ImageFilter.GaussianBlur(u*2.2)); a=glow.getchannel('A').point(lambda v:int(v*.55)); glow.putalpha(a)
    im=Image.alpha_composite(im,glow); d=ImageDraw.Draw(im)
    d.polygon(P(L),fill=(40,44,56,255)); d.polygon(P(R),fill=(22,25,32,255))
    for poly in (L,R): d.line(P(poly+[poly[0]]),fill=(150,160,178,255),width=max(2,int(u*.5)))
    d.polygon(P(CORE),fill=(216,27,61,255)); d.line(P([(28,8),(50,58),(72,8)]),fill=(255,60,95,255),width=w)
    d.line(P([(50,64),(50,90)]),fill=(255,51,85,255),width=max(2,int(u*.6)))
    for l in LINES: d.line(P(l),fill=(255,51,85,200),width=max(2,int(u*.7)))
    return im.resize((size,size),Image.LANCZOS)
os.makedirs('assets',exist_ok=True)
emblem(1024,.60,BG).save('assets/icon-only.png')
emblem(1024,.46,None).save('assets/icon-foreground.png')
Image.new('RGBA',(1024,1024),BG).save('assets/icon-background.png')
for n in ('splash','splash-dark'): emblem(2732,.20,BG).save('assets/%s.png'%n)
print('icons ok')

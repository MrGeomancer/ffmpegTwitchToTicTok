import ffmpeg


def render_blur(path):
    scalefilt = f'scale={rez['width']}:{rez['length']},setsar=1:1'
    blurfilt = 'boxblur=luma_radius=27'
    blurfilt2 = 'boxblur=luma_power=3'
    blurfilt3 = 'boxblur=chroma_radius=27'
    blurfilt4 = 'boxblur=luma_power=3'
    making_bg = (
        ffmpeg
        .input(path)
        .output(fr'{path}_folder/blured.mp4', vcodec='libx264', vf=f'{scalefilt}, {blurfilt},{blurfilt2}, {blurfilt3},{blurfilt4}')
        .run()
    )


def render(outputs, path, **kwargs):
    if kwargs['cs_to916']:
        render_blur(path,outputs)
    for i in kwargs:
        print(kwargs)
    print(outputs)


rez = {'width':1440,'length':2808}
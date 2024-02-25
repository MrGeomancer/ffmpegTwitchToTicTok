import ffmpeg
import os


def render_crop(path):
    making_neworig = (
        ffmpeg
        .input(path)
        .filter('crop', 1200, 1080, 360, 0)
        .filter('scale', 1440, -1)
        .output(fr'{path}_folder/croped.mp4', vcodec='libx264', crf=22)  # outputs[4] раньше
        .run()
    )

def render_blur(path, blurcroped):
    scalefilt = f'scale={rez['width']}:{rez['length']},setsar=1:1'
    blurfilt = 'boxblur=luma_radius=27'
    blurfilt2 = 'boxblur=luma_power=3'
    blurfilt3 = 'boxblur=chroma_radius=27'
    blurfilt4 = 'boxblur=luma_power=3'

    if blurcroped:
        making_bg = (
            ffmpeg
            .input(fr'{path}_folder/croped.mp4')
            .output(fr'{path}_folder/blured.mp4', vcodec='libx264', vf=f'{scalefilt}, {blurfilt},{blurfilt2}, {blurfilt3},{blurfilt4}')
            .run()
        )
    else:
        making_bg = (
            ffmpeg
            .input(path)
            .output(fr'{path}_folder/blured.mp4', vcodec='libx264', vf=f'{scalefilt}, {blurfilt},{blurfilt2}, {blurfilt3},{blurfilt4}')
            .run()
        )


def overlayall(path, outputs):
    # inputs=[ffmpeg.input(path) for path in outputs]
    # overlay = ffmpeg.input(fr'{path}_folder/blured.mp4').overlay(ffmpeg.input(fr'{path}_folder/croped.mp4').filter('scale', 1440, -1), x='0', y='756')  # only cropedo_rig
    overlay = ffmpeg.input(fr'{path}_folder/blured.mp4').overlay(ffmpeg.input(fr'{path}').filter('scale', 1440, -1), x='0', y='864')  # only cropedo_rig

    overlay = overlay.overlay(
        ffmpeg.input(r'C:\Users\Pekarnya\Videos\Desktop\out4.mp4').filter('trim', duration=f"{ffmpeg.probe(path)['streams'][0]['duration']}"), x='342', y=400)  # add nameing
    overlay = overlay.output(ffmpeg.input(path).audio, fr'{path}_folder/final.mp4', vcodec='libx264', acodec='aac')

    ffmpeg.run(overlay, overwrite_output=True)


def render(outputs, path, **kwargs):
    os.makedirs(fr'{path}_folder/', exist_ok=True)
    print(kwargs)
    if kwargs['cs_crop'] == True:
        print('Начало рендера crop')
        render_crop(path)
    if kwargs['cs_to916'] == True:
        if kwargs['cs_crop'] == True:
            print('Начало рендера блюр из crop')
            render_blur(path, True)
        else: render_blur(path, False)
        print('Начало рендера блюра из оригинала')

    overlayall(path,outputs)
    # for i in kwargs:
    #     print(kwargs)
    print(outputs)


rez = {'width':1440,'length':2808}
import ffmpeg
import os


def render_crop(path, scale, rez_orig):
    # print('scale:',scale)
    # type(scale)
    global rez
    crop_x = rez_orig['width']*scale
    crop_y = rez_orig['height']
    crop_from_x = rez_orig['width']/2-crop_x/2
    scale_to_y = int(rez['width']/crop_x * crop_y)
    overlay_y = str(rez['height']/2 - scale_to_y/2)
    print('overlay_y:', overlay_y)
    print('rez[widthg]', rez['width'])
    making_neworig = (
        ffmpeg
        .input(path)
        .filter('crop', crop_x, crop_y, crop_from_x, 0)
        .filter('scale', rez['width'], scale_to_y)
        .output(fr'{path}_folder/croped.mp4', vcodec='libx264', crf=22)
        .run(overwrite_output=False)
    )

    # overlay = ffmpeg.input(fr'{path}_folder/bg.png').overlay(ffmpeg.input(fr'{path}_folder/croped.mp4').filter('scale', rez['width'], scale_to_y), x='0', y=overlay_y)
    # overlay = overlay.output(fr'{path}_folder/crops_on_bg.mp4', vcodec='libx264')
    # ffmpeg.run(overlay, overwrite_output=True)

    on_bg = (
        ffmpeg
        # .input(fr'{path}_folder/bg.png')
        .input(fr'{path}_folder/bg.mp4')
        .overlay(
            ffmpeg
            .input(fr'{path}_folder/croped.mp4')
            # .filter('scale', rez['width'], -1)
            # .filter('scale', rez['width'], scale_to_y)
            , x='0'
            , y=overlay_y
        )
        .output(fr'{path}_folder/crops_on_bg.mp4', vcodec='libx264')
        .run(overwrite_output=True)
    )


def render_blur(path, blurcroped):
    scalefilt = f'scale={rez['width']}:{rez['height']},setsar=1:1'
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
    overlay = ffmpeg.input(fr'{path}_folder/blured.mp4').overlay(ffmpeg.input(fr'{path}_folder/croped.mp4').filter('scale', 1440, -1), x='0', y='756')  # only cropedo_rig
    # overlay = ffmpeg.input(fr'{path}_folder/blured.mp4').overlay(ffmpeg.input(fr'{path}').filter('scale', 1440, -1), x='0', y='864')  # only cropedo_rig

    overlay = overlay.overlay(
        ffmpeg.input(r'C:\Users\Pekarnya\Videos\Desktop\out4.mp4').filter('trim', duration=f"{ffmpeg.probe(path)['streams'][0]['duration']}"), x='342', y=400)  # add nameing
    overlay = overlay.output(ffmpeg.input(path).audio, fr'{path}_folder/final.mp4', vcodec='libx264', acodec='aac')

    ffmpeg.run(overlay, overwrite_output=True)


def take_rez(path):
    return {
        'width':ffmpeg.probe(path)['streams'][0]['width'],
        'height':ffmpeg.probe(path)['streams'][0]['height']
    }


def render(outputs, path, **kwargs):
    global rez
    os.makedirs(fr'{path}_folder/', exist_ok=True)
    rez_input = take_rez(path)
    making_bg = (
        ffmpeg
        .input(r'C:\Users\Pekarnya\Videos\stock_bg.png'
               ,loop=1
               ,t=1
               )
        # .filter('scale', rez['width'], rez['height'])
        .output(fr'{path}_folder/bg.mp4',vf=f'scale={rez['width']}:{rez['height']},setsar=1:1')
        .run(overwrite_output=True)
    )
    if kwargs['cs_crop'] == True:
        print('Начало рендера crop')
        entry = float((kwargs['cs_cropentry']).replace(",", "."))
        render_crop(path, entry, rez_input)
    # if kwargs['cs_to916'] == True:
    #     if kwargs['cs_crop'] == True:
    #         print('Начало рендера блюр из crop')
    #         render_blur(path, True)
    #     else: render_blur(path, False)
    #     print('Начало рендера блюра из оригинала')

    overlayall(path,outputs)
    # for i in kwargs:
    #     print(kwargs)
    print(outputs)


rez = {
    'width':1440,
    'height':2808,
    # 'chonit':'smth',
}


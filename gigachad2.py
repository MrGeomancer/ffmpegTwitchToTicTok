import ffmpeg
import os


def render_crop(path, scale, rez_orig):
    # print('scale:',scale)
    # type(scale)
    global rez
    crop_x = rez_orig['width'] * scale
    crop_y = rez_orig['height']
    crop_from_x = rez_orig['width'] / 2 - crop_x / 2
    scale_to_y = int(rez['width'] / crop_x * crop_y)
    overlay_y = int(rez['height'] / 2 - scale_to_y / 2)
    croped_path = fr'{path}_folder/{scale}x{int(crop_x)}x{int(crop_y)}croped.mp4'
    print('overlay_y:', overlay_y)
    print('rez[widthg]', rez['width'])
    making_neworig = (
        ffmpeg
        .input(path)
        .filter('crop', crop_x, crop_y, crop_from_x, 0)
        .filter('scale', rez['width'], scale_to_y)
        .output(croped_path, vcodec='libx264', crf=22)
        .run(overwrite_output=False)
    )

    # overlay = ffmpeg.input(fr'{path}_folder/bg.png').overlay(ffmpeg.input(fr'{path}_folder/croped.mp4').filter('scale', rez['width'], scale_to_y), x='0', y=overlay_y)
    # overlay = overlay.output(fr'{path}_folder/crops_on_bg.mp4', vcodec='libx264')
    # ffmpeg.run(overlay, overwrite_output=True)

    crop_on_bg = (
        ffmpeg
        .input(fr'{path}_folder/bg.mp4')
        .overlay(
            ffmpeg
            .input(path)
            .filter('crop', crop_x, crop_y, crop_from_x, 0)
            .filter('scale', rez['width'], scale_to_y)
            , x='0'
            , y=overlay_y
        )
        .output(fr'{path}_folder/croped_on_bg.mp4', vcodec='libx264')
        .run(overwrite_output=False)
    )
    return croped_path


def render_kills_cs(path, rez_orig, scale):
    global rez
    crop_x = 285
    crop_y = 120
    scale_to_x = crop_x * 1.5
    scale_to_y = crop_y * 1.5
    overlay_x = int(rez['width'] - scale_to_x)
    overlay_y = ((rez['height'] / 2) - (
                ((rez['width'] / (rez_orig['width'] * scale)) * rez_orig['height']) / 2)) - scale_to_y
    #
    # print('высота кадра:',rez['height'])
    # print('высота оригинального видоса:',int((rez['width']/(rez_orig['width']*scale)) * rez_orig['height']))
    # print('откуда начинается кроп', (rez['height']/2)-(((rez['width']/(rez_orig['width']*scale)) * rez_orig['height'])/2))
    # print('до каких размеров мы увеличиваем килы:', scale_to_y)
    # print('куда должен упасть по У',((rez['height']/2)-(((rez['width']/(rez_orig['width']*scale)) * rez_orig['height'])/2))-scale_to_y)
    making_kills = (
        ffmpeg
        .input(fr'{path}_folder/bg.mp4')
        .overlay(
            ffmpeg
            .input(path)
            .filter('crop', 285, 120, 1630, 70)
            .filter('scale', scale_to_x, scale_to_y)
            , x=overlay_x
            , y=overlay_y
        )
        .output(fr'{path}_folder/kills_on_bg.mp4', vcodec='libx264')
        .run(overwrite_output=False)
    )
    # making_kills = (
    #     ffmpeg
    #     .input(fr'{path}_folder/crop_on_bg.mp4')
    #     .overlay(
    #         ffmpeg
    #         .input(path)
    #         .filter('crop', 285, 120, 1630, 70)
    #         .filter('scale', scale_to_x, scale_to_y)
    #         , x=overlay_x
    #         , y=overlay_y
    #     )
    #     .output(fr'{path}_folder/kills_on_bg2.mp4', vcodec='libx264')
    #     .run(overwrite_output=False)
    # )


def render_radar_cs(path, rez_orig, scale):
    global rez
    crop_x = 289
    crop_y = 289
    scale_to_x = crop_x * 1.5
    scale_to_y = crop_y * 1.5
    overlay_y = ((rez['height'] / 2) - (
                ((rez['width'] / (rez_orig['width'] * scale)) * rez_orig['height']) / 2)) - scale_to_y

    making_radar = (
        ffmpeg
        .input(fr'{path}_folder/bg.mp4')
        .overlay(
            ffmpeg
            .input(path)
            .filter('crop', 289, 289, 6, 6)
            .filter('scale', scale_to_x, scale_to_y)
            , x=0
            , y=overlay_y
        )
        .output(fr'{path}_folder/radar_on_bg.mp4', vcodec='libx264')
        .run(overwrite_output=False)
    )


# making_radar = (
#     ffmpeg
#     .input(input_video)
#     .filter('crop', 289,289,6,6)
#     .output(outputs[2], vcodec='libx264', crf=22)
#     .run()
# )


def render_mask_apex(path, armor):
    global rez
    if armor == True:
        making_apex_mask = (
            ffmpeg
            .input(path)
            .overlay(
                ffmpeg
                .input(r'stock/mask-apex-with-armor.png')
                , x=0
                , y=0
            )
            .output(fr'{path}_folder/apex_mask.mp4', vcodec='libx264')
            .run(overwrite_output=False)
        )
    else:
        making_apex_mask = (
            ffmpeg
            .input(path)
            .overlay(
                ffmpeg
                .input(r'stock/mask-apex.png')
                , x=0
                , y=0
            )
            .output(fr'{path}_folder/apex_mask.mp4', vcodec='libx264')
            .run(overwrite_output=False)
        )


def render_radar_apex(path, rez_orig, scale, kwargs):
    global rez
    crop_x = 244
    crop_y = 244
    scale_to_x = crop_x * 1.5
    scale_to_y = crop_y * 1.5
    overlay_y = ((rez['height'] / 2) - (
                ((rez['width'] / (rez_orig['width'] * scale)) * rez_orig['height']) / 2)) - scale_to_y
    if kwargs['apex_hp'] == True:
        overlay_y -= 178
    elif kwargs['apex_hp_armor'] == True:
        overlay_y -= 220
    if kwargs['apex_zone'] == True:
        overlay_y -= 81
    making_radar = (
        ffmpeg
        .input(fr'{path}_folder/bg.mp4')
        .overlay(
            ffmpeg
            .input(fr'{path}_folder/apex_mask.mp4')
            .filter('crop', 244, 244, 48, 48)
            .filter('scale', scale_to_x, scale_to_y)
            , x=2
            , y=overlay_y
        )
        .output(fr'{path}_folder/radar_on_bg.mp4', vcodec='libx264')
        .run(overwrite_output=False)
    )


def render_zone_apex(path, rez_orig, scale, kwargs):
    global rez

    crop_x = 244
    crop_y = 53
    scale_to_x = crop_x * 1.5
    scale_to_y = crop_y * 1.5
    overlay_y = ((rez['height'] / 2) - (
                ((rez['width'] / (rez_orig['width'] * scale)) * rez_orig['height']) / 2)) - scale_to_y
    if kwargs['apex_hp'] == True:
        overlay_y -= 179
    elif kwargs['apex_hp_armor'] == True:
        overlay_y -= 220
    making_radar = (
        ffmpeg
        .input(fr'{path}_folder/bg.mp4')
        .overlay(
            ffmpeg
            .input(fr'{path}_folder/apex_mask.mp4')
            .filter('crop', crop_x, crop_y, 45, 305)
            .filter('scale', scale_to_x, scale_to_y)
            , x=2
            , y=overlay_y
        )
        .output(fr'{path}_folder/zone_on_bg.mp4', vcodec='libx264')
        .run(overwrite_output=False)
    )


def render_hp_apex(path, rez_orig, scale):
    global rez
    crop_x = 380
    crop_y = 71
    scale_to_x = crop_x * 2.5
    scale_to_y = crop_y * 2.5
    overlay_y = ((rez['height'] / 2) - (
                ((rez['width'] / (rez_orig['width'] * scale)) * rez_orig['height']) / 2)) - scale_to_y

    making_radar = (
        ffmpeg
        .input(fr'{path}_folder/bg.mp4')
        .overlay(
            ffmpeg
            .input(fr'{path}_folder/apex_mask.mp4')
            .filter('crop', 380, 71, 57, 956)
            .filter('scale', scale_to_x, scale_to_y)
            , x=2
            , y=overlay_y
        )
        .output(fr'{path}_folder/hp_on_bg.mp4', vcodec='libx264')
        .run(overwrite_output=False)
    )


def render_hp_armor_apex(path, rez_orig, scale):
    global rez
    crop_x = 423
    crop_y = 110
    scale_to_x = crop_x * 2
    scale_to_y = crop_y * 2
    overlay_y = ((rez['height'] / 2) - (
                ((rez['width'] / (rez_orig['width'] * scale)) * rez_orig['height']) / 2)) - scale_to_y

    making_radar = (
        ffmpeg
        .input(fr'{path}_folder/bg.mp4')
        .overlay(
            ffmpeg
            .input(fr'{path}_folder/apex_mask.mp4')
            .filter('crop', 423, 110, 13, 917)
            .filter('scale', scale_to_x, scale_to_y)
            , x=2
            , y=overlay_y
        )
        .output(fr'{path}_folder/hp_on_bg.mp4', vcodec='libx264')
        .run(overwrite_output=False)
    )


def render_kills_apex(path, rez_orig, scale):
    global rez
    crop_x = 207
    crop_y = 32
    scale_to_x1 = crop_x * 1.9
    scale_to_y1 = crop_y * 1.9
    overlay_x1 = rez['width'] - scale_to_x1
    overlay_y1 = ((rez['height'] / 2) - (
                ((rez['width'] / (rez_orig['width'] * scale)) * rez_orig['height']) / 2)) - scale_to_y1
    scale_to_x2 = 103 * 1.9
    scale_to_y2 = 32 * 1.9
    overlay_x2 = rez['width'] - scale_to_x1 - scale_to_x2
    overlay_y2 = ((rez['height'] / 2) - (
            ((rez['width'] / (rez_orig['width'] * scale)) * rez_orig['height']) / 2)) - scale_to_y1


    making_kills = (
        ffmpeg
        .input(fr'{path}_folder/bg.mp4')
        .overlay(
            ffmpeg
            .input(fr'{path}_folder/apex_mask.mp4')
            .filter('crop', crop_x, crop_y, 1442, 92)
            .filter('scale', scale_to_x1, scale_to_y1)
            , x=overlay_x1
            , y=overlay_y1
        )
        .overlay(
            ffmpeg
            .input(fr'{path}_folder/apex_mask.mp4')
            .filter('crop', 103, 32, 1662, 92)
            .filter('scale', scale_to_x2, scale_to_y2)
            , x=overlay_x2
            , y=overlay_y2
        )
        .output(fr'{path}_folder/kills_on_bg.mp4', vcodec='libx264')
        .run(overwrite_output=False)
    )


def render_players_cs(path, rez_orig, scale):
    global rez
    crop_x = 680
    crop_y = 180
    scale_to_x = crop_x * 1.5
    scale_to_y = crop_y * 1.5
    overlay_x = int(rez['width'] / 2 - scale_to_x / 2)
    overlay_y = ((rez['height'] / 2) - (
                ((rez['width'] / (rez_orig['width'] * scale)) * rez_orig['height']) / 2)) - scale_to_y

    making_players = (
        ffmpeg
        .input(fr'{path}_folder/bg.mp4')
        .overlay(
            ffmpeg
            .input(path)
            .filter('crop', 680, 180, 620, 0)
            .filter('scale', scale_to_x, scale_to_y)
            , x=overlay_x
            , y=overlay_y
        )
        .output(fr'{path}_folder/players_on_bg.mp4', vcodec='libx264')
        .run(overwrite_output=False)
    )


# making_players = (
#     ffmpeg
#     .input(input_video)
#     .filter('crop', 680,180,620,0)
#     .output(outputs[3], vcodec='libx264', crf=22)
#     .run()
# )


def render_webcam(path, rez_orig, scale):
    global rez
    crop_x = 270
    crop_y = 208
    scale_to_x = crop_x * 1.8
    scale_to_y = crop_y * 1.8
    if scale == 1:
        scale_to_x *= 1.5
        scale_to_y *= 1.5
    overlay_x = int(rez['width'] / 2 - scale_to_x / 2)
    overlay_y = ((rez['height'] / 2) + (((rez['width'] / (rez_orig['width'] * scale)) * rez_orig['height']) / 2))

    # print('scale_to_x:',scale_to_x)
    # print('scale_to_y:',scale_to_y)
    making_webcam = (
        ffmpeg
        .input(fr'{path}_folder/bg.mp4')
        .overlay(
            ffmpeg
            .input(path)
            .filter('crop', crop_x, crop_y, 37, 381)
            .filter('scale', scale_to_x, scale_to_y)
            , x=overlay_x
            , y=overlay_y
        )
        .output(fr'{path}_folder/webcam_on_bg.mp4', vcodec='libx264')
        .run(overwrite_output=False)
    )


def render_blur(path, blurcroped, croped_path=None):
    scalefilt = f'scale={rez['width']}:{rez['height']},setsar=1:1'
    blurfilt = 'boxblur=luma_radius=27'
    blurfilt2 = 'boxblur=luma_power=3'
    blurfilt3 = 'boxblur=chroma_radius=27'
    blurfilt4 = 'boxblur=luma_power=3'

    if blurcroped:
        making_bg = (
            ffmpeg
            .input(croped_path)
            .output(fr'{path}_folder/blured.mp4', vcodec='libx264',
                    vf=f'{scalefilt}, {blurfilt},{blurfilt2}, {blurfilt3},{blurfilt4}')
            .run()
        )
    else:
        making_bg = (
            ffmpeg
            .input(path)
            .output(fr'{path}_folder/blured.mp4', vcodec='libx264',
                    vf=f'{scalefilt}, {blurfilt},{blurfilt2}, {blurfilt3},{blurfilt4}')
            .run()
        )


def overlayall(path, outputs):
    inputs = [ffmpeg.input(path) for path in outputs]
    global rez
    overlay = overlay = ffmpeg.input(fr'{path}_folder/blured.mp4')
    for item in outputs:
        overlay = overlay.overlay(ffmpeg.input(item).filter('chromakey', color='0x00FF00', similarity=0.2, blend=0.2),
                                  x=0, y=0)

    overlay = overlay.overlay(
        ffmpeg.input(r'stock/out4.mp4').filter('trim', duration=f"{ffmpeg.probe(path)['streams'][0]['duration']}"),
        x='342', y=400)  # add nameing
    overlay = overlay.output(ffmpeg.input(path).audio, fr'{path}_folder/final.mp4', vcodec='libx264', acodec='aac')
    ffmpeg.run(overlay, overwrite_output=True)

    # overlay_all = (
    #     ffmpeg
    #     .input(fr'{path}_folder/blured.mp4')
    #     .overlay(
    #         ffmpeg
    #         .input(fr'{path}_folder/crop_on_bg.mp4')
    #         # .filter('scale', rez['width'], -1)
    #         # .filter('scale', rez['width'], scale_to_y)
    #         # .filter('scale', rez['width'], rez['height'])  # Указывайте желаемое разрешение
    #         .filter('chromakey', color='0x00FF00', similarity=0.2, blend=0.2)  # Замените цвет и настройки на подходящие
    #         , x='0'
    #         , y='0'
    #     )
    #     .output(ffmpeg.input(path).audio, fr'{path}_folder/final.mp4', vcodec='libx264')
    #     .run(overwrite_output=True)
    # )

    # overlay = ffmpeg.input(fr'{path}_folder/blured.mp4').overlay(ffmpeg.input(fr'{path}_folder/croped.mp4'), x='0', y='756')  # only cropedo_rig
    # overlay = ffmpeg.input(fr'{path}_folder/blured.mp4').overlay(ffmpeg.input(fr'{path}').filter('scale', 1440, -1), x='0', y='864')  # only cropedo_rig

    # overlay = overlay.overlay(
    #     ffmpeg.input(r'C:\Users\Pekarnya\Videos\Desktop\out4.mp4').filter('trim', duration=f"{ffmpeg.probe(path)['streams'][0]['duration']}"), x='342', y=400)  # add nameing
    # overlay = overlay.output(ffmpeg.input(path).audio, fr'{path}_folder/final6.mp4', vcodec='libx264', acodec='aac')
    #
    # ffmpeg.run(overlay, overwrite_output=True)


def take_rez(path):
    return {
        'width': ffmpeg.probe(path)['streams'][0]['width'],
        'height': ffmpeg.probe(path)['streams'][0]['height']
    }


def render(outputs, path, **kwargs):
    global rez
    colvo = len(outputs) - 1
    print('outputs:', outputs)
    os.makedirs(fr'{path}_folder/', exist_ok=True)
    rez_input = take_rez(path)
    making_bg = (
        ffmpeg
        .input(r'stock\stock_bg.png'
               , loop=1
               , t=1
               )
        # .filter('scale', rez['width'], rez['height'])
        .output(fr'{path}_folder/bg.mp4', vf=f'scale={rez['width']}:{rez['height']},setsar=1:1,fps=60')
        .run(overwrite_output=True)
    )
    try:
        entry = float(kwargs['any_cropentry'].replace(',', '.'))
    except:
        entry = 1
    if kwargs['any_crop'] == True:
        print('Начало рендера crop')
        print(kwargs['any_cropentry'])
        croped_path = render_crop(path, entry, rez_input)
    if kwargs['any_to916'] == True:
        if kwargs['any_crop'] == True:
            print('Начало рендера блюр из crop')
            render_blur(path, True, croped_path)
        else:
            render_blur(path, False)
    if kwargs['cs_kills'] == True:
        print('Начало рендера kills')
        render_kills_cs(path, rez_input, entry)
    if kwargs['cs_radar'] == True:
        print('Начало рендера kills')
        render_radar_cs(path, rez_input, entry)
    if kwargs['cs_players'] == True:
        print('Начало рендера kills')
        render_players_cs(path, rez_input, entry)
    if kwargs['any_webcam'] == True:
        print('Начало рендера kills')
        render_webcam(path, rez_input, entry)
    if kwargs['apex_make_bg'] == True:
        print('Начало рендера apex_mask')
        if kwargs['apex_hp_armor'] == True:
            render_mask_apex(path, armor=True)
        else:
            render_mask_apex(path, armor=False)
    if kwargs['apex_zone'] == True:
        print('Начало рендера apex_zone')
        render_zone_apex(path, rez_input, entry, kwargs)
    if kwargs['apex_radar'] == True:
        print('Начало рендера apex_radar')
        render_radar_apex(path, rez_input, entry, kwargs)
    if kwargs['apex_hp'] == True:
        print('Начало рендера apex_hp')
        render_hp_apex(path, rez_input, entry)
    if kwargs['apex_hp_armor'] == True:
        print('Начало рендера apex_hp')
        render_hp_armor_apex(path, rez_input, entry)
    if kwargs['apex_kills'] == True:
        print('Начало рендера apex_hp')
        render_kills_apex(path, rez_input, entry)

    overlayall(path, outputs)
    # for i in kwargs:
    #     print(kwargs)
    print(outputs)


rez = {
    'width': 1440,
    'height': 2808,
    # 'chonit':'smth',
}

overlay_y_min = 400

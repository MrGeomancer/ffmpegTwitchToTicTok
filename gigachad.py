import ffmpeg

# Исходное видео
input_video = 'in10.mp4'

with open("trying.txt", "r+") as my_file:
    i = int(my_file.read()) + 1
    my_file.seek(0)
    my_file.write(str(i))

# Название выходного файла


outputs=[f'output_blured{i}.mp4',
# outputs=[f'output_fin103.mp4',
# outputs=[f'output_blured93.mp4',
#          f'output_kills{i}.mp4',
#          f'output_kills41.mp4',
         # f'output_radar{i}.mp4',
         # f'output_radar79.mp4',
         # f'output_players{i}.mp4',
         # f'output_cropedorig{i}.mp4',
         # r'C:\Users\Pekarnya\Videos\Desktop\out4.mp4']
         f'output_cropedorig93.mp4']


output_video = f'output_fin{i}.mp4'
output_audio = 'ou.mp3'

# Создаем процесс конвертации
scalefilt = 'scale=1440:2808,setsar=1:1'
# blurfilt = 'gblur=sigma=20'
blurfilt = 'boxblur=luma_radius=27'
blurfilt2 = 'boxblur=luma_power=3'
blurfilt3 = 'boxblur=chroma_radius=27'
blurfilt4 = 'boxblur=luma_power=3'
# blurfilt = ffmpeg.filter('boxblur', luma_radius='min(h\,w)/40', luma_power=3, chroma_radius='min(cw\,ch)/40', chroma_power=1)
# boxblur=luma_radius=min(h\,w)/40:luma_power=3:chroma_radius=min(cw\,ch)/40:chroma_power=1[bg]


# making_kills = (
#     ffmpeg
#     .input(input_video)
#     .filter('crop', 285,120,1630,70)
#     .output(outputs[1], vcodec='libx264', crf=22)
#     .run()
# )

# making_radar = (
#     ffmpeg
#     .input(input_video)
#     .filter('crop', 289,289,6,6)
#     .output(outputs[2], vcodec='libx264', crf=22)
#     .run()
# )

# making_players = (
#     ffmpeg
#     .input(input_video)
#     .filter('crop', 680,180,620,0)
#     .output(outputs[3], vcodec='libx264', crf=22)
#     .run()
# )

# making_neworig = (
#     ffmpeg
#     .input(input_video)
#     .filter('crop', 1200,1080,360,0)
#     .output(outputs[1], vcodec='libx264', crf=22)  # outputs[4] раньше
#     .run()
# )

cropfilt = 'crop=1200:1080:360:0'
# making_bg = (
#     ffmpeg
#     # .input(input_video)
#     .input(outputs[1])
#     .output(outputs[0], vcodec='libx264', vf=f'{scalefilt}, {blurfilt},{blurfilt2}, {blurfilt3},{blurfilt4}')
#     .run()
# )
making_bg = (
    ffmpeg
    .input(input_video)
    # .input(outputs[1])
    .filter('crop', 1200, 1080, 360, 0)
    .filter('scale', 1440, 2808)
    .filter('setsar', 1)
    .filter('boxblur', luma_radius=27, luma_power=3)
    .filter('boxblur', chroma_radius=27, luma_power=3)
    .output(outputs[0], vcodec='libx264')
    .run()
)



infile = ffmpeg.input(input_video)
inputs=[ffmpeg.input(path) for path in outputs]
# Наложение видео друг на друга с разными координатами

# overlay = inputs[0].overlay(inputs[1], x='1636', y='1260').filter('scale', 455, 192)  # kills
# overlay = inputs[0].overlay(inputs[1].filter('scale', 342, -1), x='1098', y='612')  # kills

# overlay = inputs[0].overlay(inputs[1], x='500', y='612')  # kills

# overlay = overlay.overlay(inputs[2], x='0', y='1050').filter('scale', 480, 528)  # radar
# overlay = overlay.overlay(inputs[2].filter('scale', 348, -1), x='0', y='408')  # radar

# overlay = overlay.overlay(inputs[3], x='620', y='1200')  # players

# overlay = overlay.overlay(inputs[3], x='0', y='1056').filter('scale', 1920, 1728)  # cropedorig
# overlay = overlay.overlay(inputs[2].filter('scale', 1440, -1), x='0', y='756')  # cropedo_rig
overlay = inputs[0].overlay(inputs[1].filter('scale', 1440, -1), x='0', y='756')  # only cropedo_rig

overlay = overlay.overlay(inputs[2].filter('trim',duration=f"{ffmpeg.probe(input_video)['streams'][0]['duration']}"),x ='342', y = 400)  # add nameing


# Выбираем аудио с первого видео (можно настроить под свои нужды)
overlay = overlay.output(infile.audio,output_video, vcodec='libx264', acodec='aac')

# Запускаем FFmpeg
# ffmpeg.run(overlay, overwrite_output=True)

# print(infile)
# print




infile = ffmpeg.input(input_video)
infile2 = ffmpeg.input(output_video)
# add_orig = (
#     ffmpeg
#     .overlay(infile2, infile, y=1380)
#     .overlay(infile2, infile)
#     .output(infile.audio,output_video2,aspect='9:16', vcodec='libx264', acodec='aac', strict='experimental')
#     .run()
# )


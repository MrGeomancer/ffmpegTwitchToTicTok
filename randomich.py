import ffmpeg
import os
def add_blurred_bg():
    HEIGHT = 1920
    WIDTH = 3840
    inp = ffmpeg.input('in.mp4')
    os.system("ffmpeg -i " + inp + " -f mp3 -ab 192000 -vn music.mp3")
    print("extracting audio...")
    in_file = ffmpeg.input(inp)
    probe = ffmpeg.probe('input.mp4')
    video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
    iw = int(video_stream['width'])
    ih = int(video_stream['height'])
    nw = HEIGHT * iw / ih
    (
        ffmpeg
        .overlay(
            in_file.filter('scale', WIDTH, -2).crop(0, (WIDTH * HEIGHT / nw - HEIGHT) / 2, WIDTH, HEIGHT).filter(
                'gblur', sigma=40),
            in_file.filter('scale', -2, HEIGHT),
            x=(WIDTH - nw) / 2
        )
        .output('outputPartial.mp4')
        .run()
    )
    print("bluring...")
    os.system("ffmpeg -i outputPartial.mp4 -i music.mp3 -shortest -c:v copy -c:a aac -b:a 256k output14.mp4")
    print("mixing...")
    os.remove("outputPartial.mp4")
    os.remove("music.mp3")
    print("cleaning up...")
    print("done!")
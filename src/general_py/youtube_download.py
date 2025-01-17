import yt_dlp
import argparse
import os

VIDEO_SAVE_DIRECTORY = "/Volumes/G-DRIVE ArmorATD/movies/1"
AUDIO_SAVE_DIRECTORY = "./audio"


def download_video(url, output_path=VIDEO_SAVE_DIRECTORY):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s')
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("Video downloaded successfully")


def download_audio(url, output_path=AUDIO_SAVE_DIRECTORY):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s')
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("Audio extracted successfully")


def main():
    parser = argparse.ArgumentParser(description="Download YouTube videos or extract audio")
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument("-a", "--audio", action="store_true", help="Extract audio only")
    args = parser.parse_args("https://www.youtube.com/watch?v=wt5Bm65pUII".split())

    if args.audio:
        download_audio(args.url)
    else:
        download_video(args.url)


if __name__ == "__main__":
    main()

#to make the video playeble in the imac 
# ffmpeg -i sql.mp4 -c:v libx264 -c:a aac sql1.mp4
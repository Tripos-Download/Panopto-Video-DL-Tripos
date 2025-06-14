import ffmpeg
import argparse
import os
import tempfile

"""
Args:
    input (str): The path to the file of links (relative to where the script is
        executed or absolute).
    output (str): The folder where the mp4 files will be stored.
    m (int, optional) : The map used for stream. It tells ffmpeg which video
        quality it should use. By default it uses the highest quality, and it takes
        value from 0-2. 0=1920x1080; 1=1352x764; 2=960x540.
"""
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", required=True, type=str)
    parser.add_argument("--output", "-o", required=True, type=str)
    parser.add_argument("-map", type=str)
    args = parser.parse_args()

    input_file = args.input
    output_dir = args.output
    m = args.map

    if not os.path.isfile(input_file):
        raise argparse.ArgumentTypeError(f"input:{input_file} is not a valid file")
    else:
        input_file = os.path.abspath(input_file)
        print(input_file)
    if not os.path.isdir(output_dir):
        raise argparse.ArgumentTypeError(f"output:{output_dir} is not a valid folder")
    else:
        output_dir = os.path.abspath(output_dir)
        print(output_dir)

    with open(input_file, "r") as f:
        lines = f.read().splitlines()

    ct = 0
    audio_file = None
    with tempfile.TemporaryDirectory() as tmpdirname:
        for name, link in zip(*[iter(lines)]*2):
            if name == "Audio":
                audio_file = tmpdirname + f"/{ct}.mp4"
                ct += 1
                aud = ffmpeg.input(link)["a"].output(audio_file, acodec="copy").run()
            else:
                print(name)
                if (m):
                    vid = ffmpeg.input(link)[f"v:{m}"]
                else:
                    vid = ffmpeg.input(link)[f"v"]
                aud = ffmpeg.input(audio_file)["a"]
                ffmpeg.output(vid, aud, output_dir + "/" + name, vcodec="copy", acodec="copy").run()

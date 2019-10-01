
import argparse
from pydub import AudioSegment
from pydub.silence import split_on_silence

# https://docs.python.org/ja/3/howto/argparse.html
# https://www.pydoc.io/pypi/pydub-0.9.5/autoapi/silence/index.html
parser = argparse.ArgumentParser()
parser.add_argument("-in", "--input_file", type=str, help="input file name")
parser.add_argument("-out", "--output_file", default="output_%d.wav", type=str, help="output file name")
parser.add_argument("-min", "--min_silence_len", default=500, type=int, help="(in ms) minimum length of a silence to be used for")
parser.add_argument("-th", "--silence_thresh", default=-40, type=int, help="(in dBFS) anything quieter than this will be")
parser.add_argument("-ks", "--keep_silence", default=200, type=int, help="(in ms) amount of silence to leave at the beginning")
args = parser.parse_args()

# https://algorithm.joho.info/programming/python/pydub-split-on-silence/
sound = AudioSegment.from_file(args.input_file, format="wav")
chunks = split_on_silence(sound, min_silence_len=args.min_silence_len, silence_thresh=args.silence_thresh, keep_silence=args.keep_silence)
for idx, chunk in enumerate(chunks):
    chunk.export(args.output_file % idx, format="wav")


# SilenceSplitter

CLI tool|script to split wav file on silence just using `pydub.silence.split_on_silence`.

## How to use

```bash
python ./splitter.py --in input.wav --out ./output/%d.wav
```

## Requirements

```bash
pip install pydub
pip install argparse
```

## Help

```bash
python ./splitter.py --help
```

## Note

Please install `ffmpeg` or `avconv` to use `pydub`.

## LICENSE
MIT License

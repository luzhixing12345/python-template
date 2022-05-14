# Title

## Introduction

a python work flow template in processing small or media code problems

## Requirements

```bash
pip install -r requirements.txt
```

## Usage

All the options are in [default.py](config/defaults.py), you could add options as you like.

If you want to add many options, and each time use different configuration options, try to create a config file like [config.yaml](configs/config.yaml)

create a {PROJECT_NAME} as you like, and then run as

```python
python main.py PROJECT_NAME {PROJECT_NAME}
```

log information will be recorded in `log/{PROJECT_NAME}.log`

see a more realistic implementation in [Anime-WGAN](https://github.com/luzhixing12345/Anime-WGAN) which has similar folder structure

### Arguments

- `--config-file`: position of the configuration file, by default in configs/config.yaml
- other options in `defaults.py`

## Result

## Conclusion

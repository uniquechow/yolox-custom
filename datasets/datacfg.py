import os
from yolox.data import get_yolox_datadir
from pathlib import Path

yaml_name = '3classes_AB.yaml'  # change yamlname only



a = get_yolox_datadir()
cfg = os.path.join(get_yolox_datadir(), yaml_name)

if isinstance(cfg, dict):
    yaml = cfg
else:
    import yaml
    yaml_file = Path(cfg).name
    with open(cfg) as f:
        yaml = yaml.safe_load(f)


nc = yaml['nc']
cn = yaml['names']  # classes_name
abs_datasetsdir = yaml['datasets_dir']

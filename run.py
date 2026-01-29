#!/usr/bin/env python3

import sys
import os
import subprocess

base_dir = os.path.dirname(os.path.abspath(__file__))
libs_path = os.path.join(base_dir, "libs")
if not os.path.exists(libs_path):
    os.makedirs(libs_path)
sys.path.insert(0, libs_path)

try:
    import torch
    import onnxruntime
except ImportError:
    print("Torch или ONNXRuntime не найдены. Будет установка в libs/ ...")
    subprocess.check_call([
        sys.executable,
        "-m", "pip",
        "install",
        "--upgrade",
        "--target", libs_path,
        "torch",
        "onnxruntime-gpu==1.21.0",
        "--index-url", "https://download.pytorch.org/whl/cu128"
    ])
    import torch
    import onnxruntime

import tkinter_fix
from modules import core

if __name__ == '__main__':
    core.run()

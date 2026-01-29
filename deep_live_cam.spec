# -*- mode: python ; coding: utf-8 -*-
block_cipher = None

import PyInstaller.utils.hooks

a = Analysis(
    ['run.py'],
    pathex=['.'],
    binaries=[],
    datas=[],
    hiddenimports=[
        'customtkinter', 'PIL', 'cv2', 'numpy', 'tensorflow', 'tkinter_fix', 'modules'
    ],
    hookspath=[],
    excludes=[
        'tests', 'torchvision', 'matplotlib', 'pip', 'setuptools', 'onnxruntime/testdata', 'tkinter/test', 'torch', 'onnxruntime'
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='DeepLiveCam',
    debug=False,
    strip=False,
    upx=True,        # сжимает exe
    console=False,   # GUI без консоли
)

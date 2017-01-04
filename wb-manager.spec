# -*- mode: python -*-
import os, os.path

block_cipher = None
here = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
print(here)
base = '%s/maybeBetterPywb'%here

paths = [base,'%s/mpywb'%base]
added_files = [
  ('%s/mpywb/config.yaml'%base,'.'),
  ('%s/mpywb/rules.yaml'%base,'.'),
  ('%s/mpywb/default_config.yaml'%base,'.')
]

a = Analysis(['mpywb/collectionsManager.py'],
             pathex=paths,
             binaries=None,
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='wb-manager',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='wbMan')

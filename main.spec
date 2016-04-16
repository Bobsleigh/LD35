# To generate .exe and .app
#
# To generate, do :
#        OSX : pyinstaller --onefile main_local.spec
#    Windows : pyinstaller --onefile main_local.spec
#
# Other options : --windowed
#
# Check pyinstaller for full documentation
#

block_cipher = None

addedFiles = [ ('tiles_map', 'tiles_map'), ('music','music'), ('img', 'img'), ('fonts', 'fonts') ]

a = Analysis(['main.py'],
             pathex=['LD35'],
             binaries=None,
             datas=addedFiles,
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
          a.binaries,
          a.zipfiles,
          a.datas,
          name='mainWindows.exe',
          debug=False,
          strip=False,
          upx=True,
          console=False )
app = BUNDLE(exe,
             name='mainOSX.app',
             icon=None,
             bundle_identifier=None)

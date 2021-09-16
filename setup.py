from distutils.core import setup
import py2exe
setup(console=['game.py'], data_files=[('img', ["img/wrsprite.png", "img/yrsprite.png", "img/wbsprite.png"])])
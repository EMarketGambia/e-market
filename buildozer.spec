[app]
title = Emarket Gambia
package.name = emarketgambia
package.domain = com.ebrima.emarket
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0

requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow,requests

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 0

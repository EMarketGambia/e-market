[app]
title = Emarket Gambia
package.name = emarketgambia
package.domain = com.ebrima.emarket
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0

# Using baseline requirements to ensure a smooth compilation environment
requirements = python3,kivy

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a
android.allow_backup = True

[buildozer]
log_level = 2

# ⚠️ THIS KEY TRACE BYPASSES THE 21-SECOND ROOT SECURITY CRASH
warn_on_root = 0

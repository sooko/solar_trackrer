 
 
[app]
title = Solar Tracker
package.name = solar_tracker
package.domain = com.sooko
#source.dir =/home/han/SOOKO_PROJECT/kivy/mqtt/mqtt_client_app/
source.dir =.
source.include_exts = py,png,jpg,kv,atlas,ttf,obj,glsl
version = 0.1
requirements = python3,kivy,docutils
orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0
android.permissions = INTERNET,CAMERA,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
garden_requirements =navigationdrawer
android.logcat_filters = *:S python:D
android.arch = armeabi-v7a
p4a.source_dir =/home/han/vscode/python-for-android/

[buildozer]
log_level = 2
warn_on_root = 1

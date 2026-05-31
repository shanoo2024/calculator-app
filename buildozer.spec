[app]
title = Calculator
package.name = calculator
package.domain = org.example

source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,webp,ttf,otf,txt,json

version = 0.1

requirements = python3,kivy,kivymd,lark

orientation = portrait
fullscreen = 0

# اگر اپ شما فقط در حالت debug build می‌شود، همین کافی است
android.permissions =

# خروجی‌ها و فایل‌های موقت
exclude_dirs = .git,__pycache__,bin,build,.github

# اگر از فایل KV استفاده می‌کنید، بهتر است در source.dir باشد و include_exts kv داشته باشید
# فایل ui.kv در ریشه پروژه قرار دارد و با Builder.load_file("ui.kv") لود می‌شود

[buildozer]
log_level = 2
warn_on_root = 1

[apptools]

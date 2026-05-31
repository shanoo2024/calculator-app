[app]
title = Calculator
package.name = calculator
package.domain = org.shanoo

source.dir = .
source.include_exts = py,kv

version = 0.1

requirements = python3,kivy,kivymd,lark

orientation = portrait
fullscreen = 0

# اگر اپ شما فقط در حالت debug build می‌شود، همین کافی است
android.permissions =

# خروجی‌ها و فایل‌های موقت
exclude_dirs = .git,__pycache__,bin,build,.github

# قبول خودکار لایسنس‌ها
android.accept_sdk_license = True

# قفل نسخه‌ها برای جلوگیری از build-tools 37 و خطاهای aidl
android.api = 34
android.minapi = 21

# NDK پیشنهادی p4a طبق لاگ شما
android.ndk = 28c

# اختیاری ولی مفید: ثابت کردن Build Tools
android.sdk_build_tools = 34.0.0

# اگر از فایل KV استفاده می‌کنید، بهتر است در source.dir باشد و include_exts kv داشته باشید
# فایل ui.kv در ریشه پروژه قرار دارد و با Builder.load_file("ui.kv") لود می‌شود

[buildozer]
log_level = 2
warn_on_root = 1



[apptools]

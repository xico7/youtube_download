import os
import subprocess
import time
import sys
from functools import partial

printe = partial(print, file=sys.stderr)


if __name__ == '__main__':
    with open(f"{os.getcwd()}\watch-history.html", 'r', encoding="utf8") as f:
        watch_history = f.read()

    for link in watch_history.split('\n'):
        time.sleep(30)

        printe(f"Starting to download {link}")
        download_file = subprocess.run([
            "powershell", "-Command", f".\yt-dlp.exe --config-location {os.getcwd()}/https://www.youtube.com/watch?v=VUoM6XV05U0"],
            capture_output=True)
        printe(f"Successfully finished downloading {link}")

        if download_file.returncode:
            if any(error_txt in download_file.stderr for error_txt in [b'This video has been removed by the uploader',
                   b'use the YouTube account associated with this video has been terminated',
                   b'This video contains content from BMG Rights Management',
                   b'Video unavailable',
                   b's been removed for violating YouTub',
                   b'Video unavailable. This video has',
                   b'no longer available',
                   b'Private video. Sign in if you',
                   b'This live stream recording',
                   b'unable to download video da',
                   b'his video may be inappropriate for some us',
                   b'access to members-only content like ',
                   b'ocessing this video. Check back',
                   b'not available']):
                continue
            else:
                printe(link)
                printe(download_file.stderr)
                exit(1)

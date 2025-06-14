# Panopto-Video-DL-Tripos

This userscript adds a button that fetches the streaming links (*.m3u8) of the lectures. It works by injecting javascript into the panopto page; hence, you must have a way to manage userscripts.

## Install Userscript

1. Install [TamperMonkey](https://www.tampermonkey.net/) or open-source [ViolentMonkey](https://violentmonkey.github.io/) Script-Manager browser extension
	- [Chrome](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo)  
		- Enable browser [`Developer Mode`](https://www.tampermonkey.net/faq.php#Q209)
	- [Firefox](https://addons.mozilla.org/en-US/firefox/addon/tampermonkey/)
	- [Others](https://www.tampermonkey.net/)  
2. Install this script from [GreasyFork](https://greasyfork.org/en/scripts/539400-panopto-video-dl-tripos) or copy the .js code from this repo into *Monkey.

## Usage Userscript

This plugin adds a **[Get Link]** button to the video viewer and the list page.

- Open video on Panopto website.
- Click on **[Get Link]** button in the _bottom-left_ corner.
- You should have the following in your clip board.
  ```
  Audio
  https://[string].cloudfront.net/sessions/[string]/[string].mp4
  Left_Camera_Dec03_09-05-09.mp4
  https://[string].cloudfront.net/sessions/[string]/[string].object.hls/master.m3u8
  Right_Camera_Dec03_09-05-09.mp4
  https://[string].cloudfront.net/sessions/[string]/[string].object.hls/master.m3u8
  ```

Alternatively, you can use it in the list page.
- Open folder that shows a list of lectures.
- Click on **[Get Link]** button in the _top-right_ corner, next to sort.
- You should have a longer list of each lecture in your clipboard.

The audio link has one view and audio, whereas the other two hls links don't have sound. You can stop here and use `yt-dlp` or `ffmpeg` to download the videos. Or, you can use the following python script to do it in batches.

## Install Python Script
The python script uses a wrapper for `ffmpeg` to download the hls links. It attaches the sound from the .mp4 file to the hls streams and names the new files as given by the link list above.

1. Install `ffmpeg` to the system and `ffmpeg-python` via pip, see [link](https://ffmpeg.org/download.html) for instructions for both.
2. Copy the `tripos-download.py` script to the folder where the archive lives.

## Basic Workflow
1. Go to the lecture folder for Topics in Statistical Theory, click get link to copy the links to clip board.
2. `cd /path-to-archive/` and create a new folder for the course in `Tripos-Archive`.
3. Create a file called `src.txt` and paste the links from userscript in. Now your folder should look like this.
  ```
  .
  └── Tripos-Archive/
      ├── tripos-download.py
      └── Topics-in-Statistical-Theory/
          └── src.txt
  ```
4. Now we go back to `Tripos-Archive` and invoke the python script.
   - `python tripos-download.py -i Topics-in-Statistical-Theory/src.txt -o Topics-in-Statistical-Theory/ -m 2`
   - We specified the input list of links, output directory and mapping respectively. The mapping specifies which quality of stream the script should use. 0=1920x1080, 1=1352x764, 2=960x540. If not specified, it uses the highest quality one available.
   - `ffmpeg` will be invoked and start downloading everything in `Topics-in-Statistical-Theory/src.txt`.

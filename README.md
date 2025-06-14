# Panopto-Video-DL-Tripos

This userscript adds a button that fetches the streaming links (*.m3u8) of the lectures. It works by injecting javascript into the panopto page; hence, you must have a way to manage userscripts.

## Install

1. Install [TamperMonkey](https://www.tampermonkey.net/) or open-source [ViolentMonkey](https://violentmonkey.github.io/) Script-Manager browser extension
	- [Chrome](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo)  
		- Enable browser [`Developer Mode`](https://www.tampermonkey.net/faq.php#Q209)
	- [Firefox](https://addons.mozilla.org/en-US/firefox/addon/tampermonkey/)
	- [Others](https://www.tampermonkey.net/)  
2. Install this script from [GreasyFork]([https://greasyfork.org/scripts/423661-panopto-video-dl](https://greasyfork.org/en/scripts/539400-panopto-video-dl-tripos)) or copy the .js code from this repo into *Monkey.

## Usage  

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

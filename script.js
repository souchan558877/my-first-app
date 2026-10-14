// 無料動画の公開時に、下の空欄へ https:// で始まる動画URLを設定してください。
const VIDEO_URL = '';

document.getElementById('year').textContent = String(new Date().getFullYear());
document.getElementById('watch-video').addEventListener('click', () => {
  if (VIDEO_URL) {
    const url = new URL(VIDEO_URL);
    if (url.protocol === 'https:') {
      window.open(url.href, '_blank', 'noopener,noreferrer');
      return;
    }
  }
  document.getElementById('video-status').hidden = false;
});

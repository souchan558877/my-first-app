// 正式な申し込み先を決めたら、空欄に https:// から始まるURLを入れてください。
// 例示用・仮のURLは設定していません。変更後は python3 lp/build_preview.py を実行。
const APPLICATION_URL = '';

(() => {
  document.getElementById('lp-year').textContent = String(new Date().getFullYear());
  let destination;
  try {
    const url = new URL(APPLICATION_URL);
    if (url.protocol === 'https:' && !url.username && !url.password) {
      destination = url.href;
    }
  } catch {
    // 空欄や不正なURLの場合は、申し込みボタンを無効のままにする。
  }

  if (!destination) return;

  document.querySelectorAll('[data-apply]').forEach(button => {
    button.disabled = false;
    button.addEventListener('click', () => window.location.assign(destination));
  });
  document.querySelectorAll('[data-availability]').forEach(message => {
    message.textContent = '申し込みボタンから、正式な受付ページへお進みください。';
  });
})();

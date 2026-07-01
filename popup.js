document.getElementById('save').addEventListener('click', () => {
  const token = document.getElementById('token').value.trim();
  const repo = document.getElementById('repo').value.trim();

  chrome.storage.local.set({ githubToken: token, githubRepo: repo }, () => {
    const status = document.getElementById('status');
    status.innerText = "Settings saved successfully! 👍";
    setTimeout(() => { status.innerText = ""; }, 3000);
  });
});

// Purana saved data load karne ke liye agar pehle se save ho
chrome.storage.local.get(['githubToken', 'githubRepo'], (data) => {
  if (data.githubToken) document.getElementById('token').value = data.githubToken;
  if (data.githubRepo) document.getElementById('repo').value = data.githubRepo;
});
function toBase64(str) {
  return btoa(unescape(encodeURIComponent(str)));
}

async function pushToGitHub(token, repo, fileData) {
  const { title, slug, code, lang } = fileData;
  const filename = `solutions/leetcode/${slug}/solution.${lang}`;
  const url = `https://api.github.com/repos/${repo}/contents/${filename}`;
  
  const dateStr = new Date().toISOString().split('T')[0];
  const commentChar = ['cpp', 'java', 'js', 'ts', 'go', 'rs'].includes(lang) ? '//' : '#';
  const fullContent = `${commentChar} Problem: ${title}\n${commentChar} URL: https://leetcode.com/problems/${slug}/\n${commentChar} Solved on: ${dateStr}\n\n${code}`;

  let sha = null;
  try {
    const res = await fetch(url, { headers: { 'Authorization': `token ${token}` } });
    if (res.status === 200) {
      const data = await res.json();
      sha = data.sha;
    }
  } catch (err) { console.log("Creating new file."); }

  const body = {
    message: `[Auto-Sync] Solved: ${title}`,
    content: toBase64(fullContent)
  };
  if (sha) body.sha = sha;

  const response = await fetch(url, {
    method: 'PUT',
    headers: {
      'Authorization': `token ${token}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(body)
  });

  return response.ok;
}

// 👂 Listen for the message from content.js
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "process_submission") {
    console.log("Background received submission data. Fetching token...");
    
    // Get stored GitHub credentials
    chrome.storage.local.get(['githubToken', 'githubRepo'], async (storedData) => {
      if (!storedData.githubToken || !storedData.githubRepo) {
        console.error("GitHub Credentials missing! Please set them up in extension popup.");
        return;
      }
      
      console.log("Pushing to GitHub repo:", storedData.githubRepo);
      const success = await pushToGitHub(storedData.githubToken, storedData.githubRepo, request.data);
      if (success) {
        console.log("Successfully pushed to GitHub! 🚀");
      } else {
        console.error("Failed to push to GitHub.");
      }
    });
  }
  return true;
});
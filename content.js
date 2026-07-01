// Function to extract problem info and code from LeetCode page
function extractSubmissionDetails() {
  const titleElement = document.querySelector('span.text-title-large');
  const problemTitle = titleElement ? titleElement.innerText : window.location.pathname.split('/')[2];
  const slug = window.location.pathname.split('/')[2];
  
  // Monaco editor text extractor
  const codeLines = document.querySelectorAll('.monaco-editor .view-line');
  let codeText = "";
  codeLines.forEach(line => {
    codeText += line.innerText + "\n";
  });

  // Detect language
  const langElement = document.querySelector('button.id_code-category-button');
  let lang = "txt";
  if (langElement) {
    const detectedLang = langElement.innerText.toLowerCase();
    if (detectedLang.includes('python')) lang = 'py';
    else if (detectedLang.includes('c++')) lang = 'cpp';
    else if (detectedLang.includes('java')) lang = 'java';
    else if (detectedLang.includes('javascript')) lang = 'js';
    else if (detectedLang.includes('typescript')) lang = 'ts';
    else if (detectedLang.includes('go')) lang = 'go';
    else if (detectedLang.includes('rust')) lang = 'rs';
  }

  return { title: problemTitle, slug: slug, code: codeText, lang: lang };
}

// 👀 MutationObserver to watch for the "Accepted" status on screen
const observer = new MutationObserver((mutations) => {
  for (let mutation of mutations) {
    if (mutation.addedNodes.length) {
      // Modern LeetCode displays "Success" or "Accepted" inside specific classes
      const successBadge = document.querySelector('[data-e2e-locator="submission-result"]') || 
                            document.body.innerText.includes("Accepted");
      
      if (successBadge) {
        console.log("BOOM! Submission Accepted detected by Extension!");
        const details = extractSubmissionDetails();
        
        // Send this data to background.js immediately to push to GitHub
        chrome.runtime.sendMessage({ action: "process_submission", data: details });
        
        // Stop observing to avoid multiple triggers for the same submission
        observer.disconnect();
        break;
      }
    }
  }
});

// Start tracking the webpage changes
observer.observe(document.body, { childList: true, subtree: true });
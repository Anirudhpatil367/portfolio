// // Smooth scroll to sections
// document.querySelectorAll('a[href^="#"]').forEach(anchor => {
//   anchor.addEventListener('click', function (e) {
//     e.preventDefault();
//     document.querySelector(this.getAttribute('href')).scrollIntoView({
//       behavior: 'smooth'
//     });
//   });
// });

// document.addEventListener('DOMContentLoaded', () => {
//   const themeToggleCheckbox = document.getElementById('theme-toggle');
//   const themeLabel = document.getElementById('theme-label');
//   const currentTheme = localStorage.getItem('theme');

//   // Apply saved theme on load
//   if (currentTheme === 'dark') {
//     document.body.classList.add('dark-mode');
//     themeToggleCheckbox.checked = true;
//     themeLabel.textContent = '☀️ Light Mode';
//   } else {
//     document.body.classList.remove('dark-mode');
//     themeToggleCheckbox.checked = false;
//     themeLabel.textContent = '🌙 Dark Mode';
//   }

//   // Toggle on change
//   themeToggleCheckbox.addEventListener('change', () => {
//     if (themeToggleCheckbox.checked) {
//       document.body.classList.add('dark-mode');
//       localStorage.setItem('theme', 'dark');
//       themeLabel.textContent = '☀️ Light Mode';
//     } else {
//       document.body.classList.remove('dark-mode');
//       localStorage.setItem('theme', 'light');
//       themeLabel.textContent = '🌙 Dark Mode';
//     }
//   });
// });

// // document.addEventListener("DOMContentLoaded", () => {
// //   const chatButton = document.getElementById("chat-button");
// //   const chatPopup = document.getElementById("chat-popup");
// //   const chatClose = document.getElementById("chat-close");
// //   const chatMessages = document.getElementById("chat-messages");
// //   const chatForm = document.getElementById("chat-form");
// //   const chatInput = document.getElementById("chat-input");

// //   // Toggle chat popup
// //   chatButton.addEventListener("click", () => {
// //     const currentDisplay = window.getComputedStyle(chatPopup).display;
// //     if (currentDisplay === "none") {
// //       chatPopup.style.display = "flex";
// //       // Add welcome message only if chat is empty
// //       if (!chatMessages.hasChildNodes()) {
// //         addMessage("assistant", "Hello! I'm your assistant. How can I help you today?");
// //       }
// //       chatInput.focus();
// //     } else {
// //       chatPopup.style.display = "none";
// //     }
// //   });

// //   chatClose.addEventListener("click", () => {
// //     chatPopup.style.display = "none";
// //   });

// //   function addMessage(sender, text) {
// //     const msgDiv = document.createElement("div");
// //     msgDiv.style.marginBottom = "10px";
// //     msgDiv.style.padding = "8px 12px";
// //     msgDiv.style.borderRadius = "12px";
// //     msgDiv.style.maxWidth = "80%";
// //     if (sender === "user") {
// //       msgDiv.style.backgroundColor = "#0a2540";
// //       msgDiv.style.color = "white";
// //       msgDiv.style.marginLeft = "auto";
// //     } else {
// //       msgDiv.style.backgroundColor = "#e0e0e0";
// //       msgDiv.style.color = "#000";
// //       msgDiv.style.marginRight = "auto";
// //     }
// //     msgDiv.textContent = text;
// //     chatMessages.appendChild(msgDiv);
// //     chatMessages.scrollTop = chatMessages.scrollHeight;
// //   }

// //   // Handle form submit
// //   chatForm.addEventListener("submit", async (e) => {
// //     e.preventDefault();
// //     const question = chatInput.value.trim();
// //     if (!question) return;

// //     addMessage("user", question);
// //     chatInput.value = "";
// //     chatInput.disabled = true;

// //     try {
// //       const response = await fetch("/api/chat", {
// //         method: "POST",
// //         headers: {
// //           "Content-Type": "application/json"
// //         },
// //         body: JSON.stringify({ question })  // ✅ use 'question', not 'message'
// //       });
// //       const data = await response.json();
// //       console.log("Backend response:", data);
// //       if (data.error) {
// //         addMessage("assistant", "Oops! " + data.error);
// //       } else {
// //         addMessage("assistant", data.answer);
// //       }
// //     } catch (err) {
// //       addMessage("assistant", "Error connecting to server.");
// //     } finally {
// //       chatInput.disabled = false;
// //       chatInput.focus();
// //     }
// //   });
// // });
// // console.log("script.js loaded");

// // document.addEventListener("DOMContentLoaded", () => {
// //   console.log("DOM fully loaded");

// //   const chatForm = document.getElementById("chat-form");
// //   const chatInput = document.getElementById("chat-input");

// //   // function addMessage(sender, text) {
// //   //   const chatMessages = document.getElementById("chat-messages");
// //   //   const messageDiv = document.createElement("div");
// //   //   messageDiv.className = sender === "user" ? "user-message" : "assistant-message";
// //   //   messageDiv.textContent = (sender === "user" ? "You: " : "Assistant: ") + text;
// //   //   chatMessages.appendChild(messageDiv);
// //   //   chatMessages.scrollTop = chatMessages.scrollHeight; // scroll to bottom
// //   // }
// //   function addMessage(sender, text) {
// //     const container = document.getElementById("chat-messages");
// //     const msg = document.createElement("p");
// //     msg.style.padding = "8px";
// //     msg.style.margin = "4px 0";
// //     msg.style.borderRadius = "5px";
// //     msg.style.backgroundColor = sender === "user" ? "#d1e7dd" : "#bee5eb";
// //     msg.textContent = text;
// //     container.appendChild(msg);
// //     container.scrollTop = container.scrollHeight;
// //   }
  
// //   chatForm.addEventListener("submit", async (e) => {
// //     e.preventDefault();
// //     console.log("Form submitted");

// //     const question = chatInput.value.trim();
// //     if (!question) {
// //       console.log("Empty question submitted, ignoring.");
// //       return;
// //     }

// //     addMessage("user", question);
// //     chatInput.value = "";
// //     chatInput.disabled = true;

// //     try {
// //       console.log("Sending fetch request to /api/chat with question:", question);

// //       const response = await fetch("/api/chat", {
// //         method: "POST",
// //         headers: {
// //           "Content-Type": "application/json"
// //         },
// //         body: JSON.stringify({ question })
// //       });

// //       console.log("Response received, parsing JSON...");
// //       const data = await response.json();
// //       console.log("Response JSON:", data);

// //       if (data.error) {
// //         addMessage("assistant", "Oops! " + data.error);
// //       } else if (data.answer) {
// //         addMessage("assistant", data.answer);
// //       } else {
// //         addMessage("assistant", "Sorry, no reply.");
// //       }
// //     } catch (err) {
// //       console.error("Fetch error:", err);
// //       addMessage("assistant", "Error connecting to server.");
// //     } finally {
// //       chatInput.disabled = false;
// //       chatInput.focus();
// //     }
// //   });
// // });
// document.addEventListener("DOMContentLoaded", () => {
//   const chatButton = document.getElementById("chat-button");
//   const chatPopup = document.getElementById("chat-popup");
//   const chatClose = document.getElementById("chat-close");
//   const chatMessages = document.getElementById("chat-messages");
//   const chatForm = document.getElementById("chat-form");
//   const chatInput = document.getElementById("chat-input");

//   // --- MANUAL linkify test ---
//   const testHTML = linkify("Contact me at apatil3@Uab.edu or visit https://www.linkedin.com/in/anirudhpatil367/");
//   // Append a visible div with the test output at the end of body:
//   const testDiv = document.createElement('div');
//   testDiv.style.background = '#eee';
//   testDiv.style.padding = '20px';
//   testDiv.style.margin = '10px 0';
//   testDiv.innerHTML = testHTML;
//   document.body.appendChild(testDiv);

//   // function linkify(text) {
//   //   // Convert markdown links [text](url) to HTML links
//   //   const mdLinkPattern = /\[([^\]]+)\]\((https?:\/\/[^\s)]+)\)/gi;
//   //   text = text.replace(mdLinkPattern, (match, p1, p2) => {
//   //     return `<a href="${p2}" target="_blank" rel="noopener noreferrer">${p1}</a>`;
//   //   });
  
//   //   // Convert URLs wrapped in angle brackets <https://example.com>
//   //   const angleBracketPattern = /<((https?|ftp|file):\/\/[^>\s]+)>/gi;
//   //   text = text.replace(angleBracketPattern, (match, p1) => {
//   //     return `<a href="${p1}" target="_blank" rel="noopener noreferrer">${p1}</a>`;
//   //   });
  
//   //   // Convert plain URLs to clickable links, trimming trailing punctuation
//   //   const urlPattern = /(\b(https?|ftp|file):\/\/[^\s<>"'`{}|\\^~\[\]`]+[^\s.,;:!?)\]])/gi;
//   //   text = text.replace(urlPattern, function(url) {
//   //     return `<a href="${url}" target="_blank" rel="noopener noreferrer">${url}</a>`;
//   //   });
  
//   //   return text;
//   // }
  
//   function linkify(text) {
//     // Markdown-style links [text](url)
//     text = text.replace(/\[([^\]]+)\]\((https?:\/\/[^\s)]+)\)/gi, (match, p1, p2) => {
//       return `<a href="${p2}" target="_blank" rel="noopener noreferrer">${p1}</a>`;
//     });
  
//     // URLs inside parentheses or plain
//     text = text.replace(/(\()?(https?:\/\/[^\s)]+)(\))?/gi, (match, open, url, close) => {
//       return `${open || ''}<a href="${url}" target="_blank" rel="noopener noreferrer">${url}</a>${close || ''}`;
//     });
  
//     // Emails
//     text = text.replace(
//       /\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b/g,
//       email => `<a href="mailto:${email}">${email}</a>`
//     );
  
//     // Phone numbers like +12052226249 or (205) 222-6249
//     text = text.replace(
//       /(\+?\d[\d\s\-().]{7,}\d)/g,
//       phone => `<a href="tel:${phone.replace(/[^+\d]/g, '')}">${phone}</a>`
//     );
  
//     return text.trim();
//   }
  
  
  
//   // Add message to chat box
//   function addMessage(sender, text) {
//     console.log("Original text:", text);
//     console.log("Linkified HTML:", linkify(text));
//     const msg = document.createElement("div");
//     msg.style.padding = "8px";
//     msg.style.margin = "6px 0";
//     msg.style.borderRadius = "6px";
//     msg.style.maxWidth = "85%";
//     msg.style.wordWrap = "break-word";
//     msg.style.fontSize = "14px";

//     if (sender === "user") {
//       msg.style.backgroundColor = "#d1e7dd"; // light green
//       msg.style.marginLeft = "auto";
//       msg.style.color = "#0f5132";
//       msg.innerHTML = `<strong>You:</strong> ${text}`;
//     } else {
//       msg.style.backgroundColor = "#bee5eb"; // light blue
//       msg.style.marginRight = "auto";
//       msg.style.color = "#055160";
//       // Convert URLs to clickable links
//       msg.innerHTML = `<strong>Assistant:</strong> ${linkify(text)}`;
//     }

//     chatMessages.appendChild(msg);
//     chatMessages.scrollTop = chatMessages.scrollHeight;
//   }

//   // Show welcome message once when chat opens first time
//   let welcomeShown = false;
//   function showWelcomeMessage() {
//     if (!welcomeShown) {
//       addMessage("assistant", "Welcome to Assistant! Feel free to ask me any questions related to Anirudh.");
//       welcomeShown = true;
//     }
//   }

//   // Toggle chat popup display
//   function toggleChatPopup() {
//     if (chatPopup.style.display === "flex") {
//       chatPopup.style.display = "none";
//     } else {
//       chatPopup.style.display = "flex";
//       showWelcomeMessage();
//       chatInput.focus();
//     }
//   }

//   chatButton.addEventListener("click", toggleChatPopup);
//   chatClose.addEventListener("click", () => {
//     chatPopup.style.display = "none";
//   });

//   chatForm.addEventListener("submit", async (e) => {
//     e.preventDefault();

//     const question = chatInput.value.trim();
//     if (!question) return;

//     addMessage("user", question);
//     chatInput.value = "";
//     chatInput.disabled = true;

//     try {
//       const response = await fetch("/api/chat", {
//         method: "POST",
//         headers: { "Content-Type": "application/json" },
//         body: JSON.stringify({ question }),
//       });

//       const data = await response.json();

//       if (data.error) {
//         addMessage("assistant", "Oops! " + data.error);
//       } else if (data.answer) {
//         console.log("Raw backend answer:", data.answer);
//         addMessage("assistant", data.answer);
//       } else {
//         addMessage("assistant", "Sorry, no reply.");
//       }
//     } catch (err) {
//       addMessage("assistant", "Error connecting to server.");
//       console.error(err);
//     } finally {
//       chatInput.disabled = false;
//       chatInput.focus();
//     }
//   });
// });
// Smooth scroll to sections
console.log("Chat script loaded");

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    document.querySelector(this.getAttribute('href')).scrollIntoView({
      behavior: 'smooth'
    });
  });
});

document.addEventListener('DOMContentLoaded', () => {
  const themeToggleCheckbox = document.getElementById('theme-toggle');
  const themeLabel = document.getElementById('theme-label');
  const currentTheme = localStorage.getItem('theme');

  // Apply saved theme on load
  if (currentTheme === 'dark') {
    document.body.classList.add('dark-mode');
    themeToggleCheckbox.checked = true;
    themeLabel.textContent = '☀️ Light Mode';
  } else {
    document.body.classList.remove('dark-mode');
    themeToggleCheckbox.checked = false;
    themeLabel.textContent = '🌙 Dark Mode';
  }

  // Toggle on change
  themeToggleCheckbox.addEventListener('change', () => {
    if (themeToggleCheckbox.checked) {
      document.body.classList.add('dark-mode');
      localStorage.setItem('theme', 'dark');
      themeLabel.textContent = '☀️ Light Mode';
    } else {
      document.body.classList.remove('dark-mode');
      localStorage.setItem('theme', 'light');
      themeLabel.textContent = '🌙 Dark Mode';
    }
  });

  // HTML entity decoder helper
  function decodeHTMLEntities(text) {
    const txt = document.createElement('textarea');
    txt.innerHTML = text;
    return txt.value;
  }

  // Linkify function to convert URLs, emails, phones to clickable links
  function linkify(text) {
    // Markdown-style links [text](url)
    text = text.replace(/\[([^\]]+)\]\((https?:\/\/[^\s)]+)\)/gi, (match, p1, p2) => {
      return `<a href="${p2}" target="_blank" rel="noopener noreferrer">${p1}</a>`;
    });

    // URLs inside parentheses or plain URLs
    text = text.replace(/(\()?(https?:\/\/[^\s)]+)(\))?/gi, (match, open, url, close) => {
      return `${open || ''}<a href="${url}" target="_blank" rel="noopener noreferrer">${url}</a>${close || ''}`;
    });

    // Emails
    text = text.replace(
      /\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b/g,
      email => `<a href="mailto:${email}">${email}</a>`
    );

    // Phone numbers like +12052226249 or (205) 222-6249
    text = text.replace(
      /(\+?\d[\d\s\-().]{7,}\d)/g,
      phone => `<a href="tel:${phone.replace(/[^+\d]/g, '')}">${phone}</a>`
    );

    return text.trim();
  }

  // Chat UI elements
  const chatButton = document.getElementById("chat-button");
  const chatPopup = document.getElementById("chat-popup");
  const chatClose = document.getElementById("chat-close");
  const chatMessages = document.getElementById("chat-messages");
  const chatForm = document.getElementById("chat-form");
  const chatInput = document.getElementById("chat-input");

  // Add message to chat box
  function addMessage(sender, text) {
    console.log("Original text:", text);
    console.log("Linkified HTML:", linkify(text));
    const msg = document.createElement("div");
    msg.style.padding = "8px";
    msg.style.margin = "6px 0";
    msg.style.borderRadius = "6px";
    msg.style.maxWidth = "85%";
    msg.style.wordWrap = "break-word";
    msg.style.fontSize = "14px";

    if (sender === "user") {
      msg.style.backgroundColor = "#d1e7dd"; // light green
      msg.style.marginLeft = "auto";
      msg.style.color = "#0f5132";
      msg.innerHTML = `<strong>You:</strong> ${text}`;
    } else {
      msg.style.backgroundColor = "#bee5eb"; // light blue
      msg.style.marginRight = "auto";
      msg.style.color = "#055160";

      // Decode HTML entities then linkify
      const decodedText = decodeHTMLEntities(text);
      msg.innerHTML = `<strong>Assistant:</strong> ${linkify(decodedText)}`;
    }

    chatMessages.appendChild(msg);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  // Show welcome message once when chat opens first time
  let welcomeShown = false;
  function showWelcomeMessage() {
    if (!welcomeShown) {
      addMessage("assistant", "Welcome to Assistant! Feel free to ask me any questions related to Anirudh.");
      welcomeShown = true;
    }
  }

  // Toggle chat popup display
  function toggleChatPopup() {
    if (chatPopup.style.display === "flex") {
      chatPopup.style.display = "none";
    } else {
      chatPopup.style.display = "flex";
      showWelcomeMessage();
      chatInput.focus();
    }
  }

  chatButton.addEventListener("click", toggleChatPopup);
  chatClose.addEventListener("click", () => {
    chatPopup.style.display = "none";
  });

  // Handle chat form submit
  chatForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const question = chatInput.value.trim();
    if (!question) return;

    addMessage("user", question);
    chatInput.value = "";
    chatInput.disabled = true;

    try {
      const response = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question }),
      });

      const data = await response.json();

      if (data.error) {
        addMessage("assistant", "Oops! " + data.error);
      } else if (data.answer) {
        console.log("Raw backend answer:", data.answer);
        addMessage("assistant", data.answer);
      } else {
        addMessage("assistant", "Sorry, no reply.");
      }
    } catch (err) {
      addMessage("assistant", "Error connecting to server.");
      console.error(err);
    } finally {
      chatInput.disabled = false;
      chatInput.focus();
    }
  });
});

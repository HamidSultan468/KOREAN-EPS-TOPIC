// --- 1. TRANSLATION FUNCTIONS ---
function translateElementText(transElement) {
    if (!transElement) return;
    const item = {
        korean: transElement.dataset.korean || transElement.innerText,
        urdu: transElement.dataset.urdu
    };
    
    if (item.urdu) {
        transElement.innerText = item.urdu;
    } else {
        const targetLang = 'ur';
        fetch(`https://translate.googleapis.com/translate_a/single?client=gtx&sl=ko&tl=${targetLang}&dt=t&q=${encodeURIComponent(item.korean)}`)
            .then(response => response.json())
            .then(data => {
                if (data && data[0] && data[0][0]) {
                    transElement.innerText = data[0][0][0];
                }
            })
            .catch(() => {
                transElement.innerText = "Translation Error";
            });
    }
}

function translateCustomText() {
    const input = document.getElementById('koInput');
    const output = document.getElementById('translationOutput');
    if (!input || !output) return;
    
    const text = input.value.trim();
    if (!text) return;

    output.innerText = "Translating...";
    fetch(`https://translate.googleapis.com/translate_a/single?client=gtx&sl=ko&tl=ur&dt=t&q=${encodeURIComponent(text)}`)
        .then(res => res.json())
        .then(data => {
            if (data && data[0] && data[0][0]) {
                output.innerText = data[0][0][0];
            }
        })
        .catch(() => {
            output.innerText = "ترجمہ کرنے میں مسئلہ آیا۔ دوبارہ کوشش کریں۔";
        });
}

// --- 2. CHATBOT FUNCTIONS ---
function sendChatMessage() {
    const input = document.getElementById('chatInput');
    const chatLog = document.getElementById('chatLog');
    if (!input || !chatLog) return;
    
    const message = input.value.trim();
    if (!message) return;

    chatLog.innerHTML += `<p><strong>You:</strong> ${message}</p>`;
    input.value = '';

    setTimeout(() => {
        chatLog.innerHTML += `<p style="color: #38bdf8;"><strong>AI:</strong> کورین ٹیسٹ میں اچھے نمبروں کے لیے Vocabulary اور Grammar کا روزانہ دہرائیں۔</p>`;
        chatLog.scrollTop = chatLog.scrollHeight;
    }, 500);
}
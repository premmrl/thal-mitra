import streamlit as st
from google import genai

# १. पेज कॉन्फिगरेशन
st.set_page_config(
    page_title="थॅलेसेमिया मित्र | ThalMitra AI",
    page_icon="🩸",
    layout="centered"
)

# २. CSS स्टाईल
st.markdown("""
    <style>
    .footer-container {
        text-align: center;
        margin-top: 45px;
        padding-top: 18px;
        border-top: 1px solid #333333;
    }
    .brand-title {
        font-size: 13px;
        color: #ff4b4b;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    .footer-text {
        color: #aaaaaa;
        font-size: 12px;
        margin-top: 5px;
        line-height: 1.6;
    }
    .mission-badge {
        display: inline-block;
        background: #2b0000;
        color: #ff6b6b;
        border: 1px solid #ff4b4b;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
        margin-bottom: 8px;
    }
    .stRadio > div {
        display: flex;
        justify-content: center;
        gap: 12px;
    }
    </style>
""", unsafe_allow_html=True)

# ३. सर्व १० भाषांचे संपूर्ण स्थानिक भाषांतर
LOCALIZATION = {
    "मराठी": {
        "badge": "🎯 मिशन थॅलेसेमिया मुक्त भारत २०३५",
        "title": "🩸 थॅलेसेमिया मित्र (ThalMitra)",
        "caption": "मिशन थॅलेसेमिया मुक्त भारत २०३५ | कॉलेज व तरुणांसाठी विवाहपूर्व तपासणी मार्गदर्शक",
        "modes": [
            "💍 लग्नाआधी तपासणी (Pre-Marital Check)",
            "🧪 कोणती टेस्ट करावी? (Test Guide)",
            "💡 गैरसमज विरुद्ध सत्य (Myth Busters)"
        ],
        "input_placeholder": "थॅलेसेमिया, रक्ताची चाचणी किंवा लग्नाआधीच्या तपासणीबाबत विचारा...",
        "thinking": "थॅलेसेमिया मित्र माहिती पडताळत आहे...",
        "brand_title": "MISSION THALASSEMIA FREE INDIA 2035",
        "brand_desc": "संयुक्त उपक्रम: <b>विघ्नहर्ता गोल्ड फाउंडेशन</b> आणि <b>Rotary Club of Pune Amanora</b><br>अधिकृत माहितीसाठी भेट द्या: <a href='https://thalassemia.rcpamanora.org/' target='_blank' style='color:#ff6b6b;'>thalassemia.rcpamanora.org</a>",
        "disclaimer": "⚠️ ही माहिती केवळ जनजागृती आणि शिक्षणासाठी आहे. वैद्यकीय सल्ल्यासाठी तज्ज्ञ डॉक्टरांचा (Hematologist) सल्ला घ्यावा."
    },
    "हिंदी": {
        "badge": "🎯 मिशन थैलेसीमिया मुक्त भारत 2035",
        "title": "🩸 थैलेसीमिया मित्र (ThalMitra)",
        "caption": "मिशन थैलेसीमिया मुक्त भारत 2035 | युवाओं के लिए विवाह-पूर्व जांच गाइड",
        "modes": [
            "💍 शादी से पहले जांच (Pre-Marital Check)",
            "🧪 कौन सा टेस्ट करवाएं? (Test Guide)",
            "💡 भ्रम बनाम सच (Myth Busters)"
        ],
        "input_placeholder": "थैलेसीमिया, ब्लड टेस्ट या शादी से पहले की जांच के बारे में पूछें...",
        "thinking": "थैलेसीमिया मित्र जानकारी जुटा रहे हैं...",
        "brand_title": "MISSION THALASSEMIA FREE INDIA 2035",
        "brand_desc": "संयुक्त पहल: <b>विघ्नहर्ता गोल्ड फाउंडेशन</b> एवं <b>Rotary Club of Pune Amanora</b><br>वेबसाइट: <a href='https://thalassemia.rcpamanora.org/' target='_blank' style='color:#ff6b6b;'>thalassemia.rcpamanora.org</a>",
        "disclaimer": "⚠️ यह जानकारी केवल जागरूकता के लिए है। चिकित्सकीय सलाह हेतु डॉक्टर से संपर्क करें।"
    },
    "English": {
        "badge": "🎯 Mission Thalassemia Free India 2035",
        "title": "🩸 ThalMitra AI",
        "caption": "Mission Thalassemia Free India 2035 | Pre-Marital Screening & Youth Guide",
        "modes": [
            "💍 Pre-Marital Screening",
            "🧪 Test Guide (CBC & HPLC)",
            "💡 Myth Busters & FAQs"
        ],
        "input_placeholder": "Ask about Thalassemia Minor/Major, tests, or pre-marital screening...",
        "thinking": "ThalMitra is finding accurate facts...",
        "brand_title": "MISSION THALASSEMIA FREE INDIA 2035",
        "brand_desc": "Joint Initiative: <b>Vighnaharta Gold Foundation</b> & <b>Rotary Club of Pune Amanora</b><br>Official Portal: <a href='https://thalassemia.rcpamanora.org/' target='_blank' style='color:#ff6b6b;'>thalassemia.rcpamanora.org</a>",
        "disclaimer": "⚠️ For educational and awareness purposes only. Consult a certified medical practitioner/hematologist for medical diagnosis."
    },
    "ગુજરાતી (Gujarati)": {
        "badge": "🎯 મિશન થેલેસેમિયા મુક્ત ભારત ૨૦૩૫",
        "title": "🩸 થેલેસેમિયા મિત્ર (ThalMitra)",
        "caption": "મિશન થેલેસેમિયા મુક્ત ભારત ૨૦૩૫ | યુવાનો માટે લગ્ન પહેલાંની તપાસ માર્ગદર્શિકા",
        "modes": [
            "💍 લગ્ન પહેલાંની તપાસ (Pre-Marital Check)",
            "🧪 કયો ટેસ્ટ કરાવવો? (Test Guide)",
            "💡 ગેરમાન્યતાઓ અને સત્ય (Myth Busters)"
        ],
        "input_placeholder": "થેલેસેમિયા, બ્લડ ટેસ્ટ કે લગ્ન પહેલાંની તપાસ વિશે પૂછો...",
        "thinking": "થેલેસેમિયા મિત્ર માહિતી તપાસી રહ્યા છે...",
        "brand_title": "MISSION THALASSEMIA FREE INDIA 2035",
        "brand_desc": "સંયુક્ત પહેલ: <b>વિઘ્નહર્તા ગોલ્ડ ફાઉન્ડેશન</b> અને <b>Rotary Club of Pune Amanora</b><br>વેબસાઇટ: <a href='https://thalassemia.rcpamanora.org/' target='_blank' style='color:#ff6b6b;'>thalassemia.rcpamanora.org</a>",
        "disclaimer": "⚠️ આ માહિતી માત્ર જાગૃતિ અને શિક્ષણ માટે છે. તબીબી સલાહ માટે નિષ્ણાત ડૉક્ટરનો સંપર્ક કરવો."
    },
    "ಕನ್ನಡ (Kannada)": {
        "badge": "🎯 ಮಿಷನ್ ಥಲಸ್ಸೆಮಿಯಾ ಮುಕ್ತ ಭಾರತ 2035",
        "title": "🩸 ಥಲಸ್ಸೆಮಿಯಾ ಮಿತ್ರ (ThalMitra)",
        "caption": "ಮಿಷನ್ ಥಲಸ್ಸೆಮಿಯಾ ಮುಕ್ತ ಭಾರತ 2035 | ಯುವಜನರಿಗಾಗಿ ವಿವಾಹ ಪೂರ್ವ ತಪಾಸಣಾ ಮಾರ್ಗದರ್ಶಿ",
        "modes": [
            "💍 ವಿವಾಹ ಪೂರ್ವ ಪರೀಕ್ಷೆ (Pre-Marital Check)",
            "🧪 ಯಾವ ಪರೀಕ್ಷೆ ಮಾಡಿಸಬೇಕು? (Test Guide)",
            "💡 ತಪ್ಪು ಕಲ್ಪನೆಗಳು ಮತ್ತು ಸತ್ಯ (Myth Busters)"
        ],
        "input_placeholder": "ಥಲಸ್ಸೆಮಿಯಾ ಅಥವಾ ರಕ್ತ ಪರೀಕ್ಷೆಯ ಬಗ್ಗೆ ಕೇಳಿ...",
        "thinking": "ಥಲಸ್ಸೆಮಿಯಾ ಮಿತ್ರ ಪರಿಶೀಲಿಸುತ್ತಿದ್ದಾರೆ...",
        "brand_title": "MISSION THALASSEMIA FREE INDIA 2035",
        "brand_desc": "ಜಂಟಿ ಉಪಕ್ರಮ: <b>ವಿಘ್ನಹರ್ತಾ ಗೋಲ್ಡ್ ಫೌಂಡೇಶನ್</b> ಮತ್ತು <b>Rotary Club of Pune Amanora</b><br>ವೆಬ್‌ಸೈಟ್: <a href='https://thalassemia.rcpamanora.org/' target='_blank' style='color:#ff6b6b;'>thalassemia.rcpamanora.org</a>",
        "disclaimer": "⚠️ ಈ ಮಾಹಿತಿಯು ಕೇವಲ ಜಾಗೃತಿಗಾಗಿ ಮಾತ್ರ. ವೈದ್ಯಕೀಯ ಸಲಹೆಗಾಗಿ ತಜ್ಞ ವೈದ್ಯರನ್ನು ಸಂಪರ್ಕಿಸಿ."
    },
    "తెలుగు (Telugu)": {
        "badge": "🎯 మిషన్ థలస్సేమియా రహిత భారత్ 2035",
        "title": "🩸 థలస్సేమియా మిత్ర (ThalMitra)",
        "caption": "మిషన్ థలస్సేమియా రహిత భారత్ 2035 | యువత కోసం వివాహ పూర్వ పరీక్షా మార్గదర్శి",
        "modes": [
            "💍 వివాహ పూర్వ పరీక్ష (Pre-Marital Check)",
            "🧪 ఏ పరీక్ష చేయించుకోవాలి? (Test Guide)",
            "💡 అపోహలు vs నిజాలు (Myth Busters)"
        ],
        "input_placeholder": "థలస్సేమియా లేదా రక్త పరీక్షల గురించి అడగండి...",
        "thinking": "థలస్సేమియా మిత్ర సమాచారం సేకరిస్తున్నారు...",
        "brand_title": "MISSION THALASSEMIA FREE INDIA 2035",
        "brand_desc": "సంయుక్త చొరవ: <b>విఘ్నహర్త గోల్డ్ ఫౌండేషన్</b> & <b>Rotary Club of Pune Amanora</b><br>వెబ్‌సైట్: <a href='https://thalassemia.rcpamanora.org/' target='_blank' style='color:#ff6b6b;'>thalassemia.rcpamanora.org</a>",
        "disclaimer": "⚠️ ఈ సమాచారం అవగాహన కోసం మాత్రమే. వైద్య సలహా కోసం నిపుణులైన వైద్యుడిని సంప్రదించండి."
    },
    "தமிழ் (Tamil)": {
        "badge": "🎯 தலசீமியா இல்லாத இந்தியா மிஷன் 2035",
        "title": "🩸 தலசீமியா மித்ரா (ThalMitra)",
        "caption": "தலசீமியா இல்லாத இந்தியா 2035 | திருமணத்திற்கு முந்தைய பரிசோதனை வழிகாட்டி",
        "modes": [
            "💍 திருமணத்திற்கு முந்தைய பரிசோதனை",
            "🧪 என்ன பரிசோதனை செய்ய வேண்டும்?",
            "💡 மூடநம்பிக்கைகளும் உண்மைகளும்"
        ],
        "input_placeholder": "தலசீமியா அல்லது இரத்த பரிசோதனை பற்றி கேளுங்கள்...",
        "thinking": "தலசீமியா மித்ரா விவரங்களை சரிபார்க்கிறது...",
        "brand_title": "MISSION THALASSEMIA FREE INDIA 2035",
        "brand_desc": "கூட்டு முயற்சி: <b>விக்னஹர்த்தா கோல்ட் ஃபவுண்டேஷன்</b> & <b>Rotary Club of Pune Amanora</b><br>இணையதளம்: <a href='https://thalassemia.rcpamanora.org/' target='_blank' style='color:#ff6b6b;'>thalassemia.rcpamanora.org</a>",
        "disclaimer": "⚠️ இந்தத் தகவல் விழிப்புணர்வுக்காக மட்டுமே. மருத்துவ ஆலோசனைக்கு மருத்துவரை அணுகவும்."
    },
    "বাংলা (Bengali)": {
        "badge": "🎯 মিশন থ্যালাসেমিয়া মুক্ত ভারত ২০৩৫",
        "title": "🩸 থ্যালাসেমিয়া মিত্র (ThalMitra)",
        "caption": "মিশন থ্যালাসেমিয়া মুক্ত ভারত ২০৩৫ | বিবাহের পূর্ববর্তী রক্তপরীক্ষা নির্দেশিকা",
        "modes": [
            "💍 বিবাহের পূর্বে পরীক্ষা (Pre-Marital Check)",
            "🧪 কোন পরীক্ষা করাবেন? (Test Guide)",
            "💡 ভ্রান্ত ধারণা বনাম সত্য (Myth Busters)"
        ],
        "input_placeholder": "থ্যালাসেমিয়া বা রক্তের পরীক্ষা সম্পর্কে জিজ্ঞাসা করুন...",
        "thinking": "থ্যালাসেমিয়া মিত্র তথ্য সংগ্রহ করছে...",
        "brand_title": "MISSION THALASSEMIA FREE INDIA 2035",
        "brand_desc": "যৌথ উদ্যোগ: <b>বিঘ্নহর্তা গোল্ড ফাউন্ডেশন</b> ও <b>Rotary Club of Pune Amanora</b><br>ওয়েবসাইট: <a href='https://thalassemia.rcpamanora.org/' target='_blank' style='color:#ff6b6b;'>thalassemia.rcpamanora.org</a>",
        "disclaimer": "⚠️ এই তথ্যটি শুধুমাত্র সচেতনতার জন্য। চিকিৎসার জন্য ডাক্তারের পরামর্শ নিন।"
    },
    "മലയാളം (Malayalam)": {
        "badge": "🎯 തലസീമിയ മുക്ത ഭാരതം മിഷൻ 2035",
        "title": "🩸 തലസീമിയ മിത്ര (ThalMitra)",
        "caption": "തലസീമിയ മുക്ത ഭാരതം 2035 | വിവാഹപൂർവ്വ പരിശോധനാ മാർഗ്ഗരേഖ",
        "modes": [
            "💍 വിവാഹപൂർവ്വ പരിശോധന (Pre-Marital Check)",
            "🧪 ഏത് ടെസ്റ്റാണ് ചെയ്യേണ്ടത്? (Test Guide)",
            "💡 മിഥ്യകളും യാഥാർത്ഥ്യങ്ങളും (Myth Busters)"
        ],
        "input_placeholder": "തലസീമിയ അല്ലെങ്കിൽ രക്തപരിശോധനയെക്കുറിച്ച് ചോദിക്കുക...",
        "thinking": "തലസീമിയ മിത്ര വിവരങ്ങൾ ശേഖരിക്കുന്നു...",
        "brand_title": "MISSION THALASSEMIA FREE INDIA 2035",
        "brand_desc": "സംയുക്ത സംരംഭം: <b>വിഘ്നഹർത്ത ഗോൾഡ് ഫൗണ്ടേഷൻ</b> & <b>Rotary Club of Pune Amanora</b><br>വെബ്സൈറ്റ്: <a href='https://thalassemia.rcpamanora.org/' target='_blank' style='color:#ff6b6b;'>thalassemia.rcpamanora.org</a>",
        "disclaimer": "⚠️ ഈ വിവരങ്ങൾ അവബോധത്തിന് മാത്രമുള്ളതാണ്. വൈദ്യോപദേശത്തിനായി ഡോക്ടറെ സമീപിക്കുക."
    },
    "ਪੰਜਾਬੀ (Punjabi)": {
        "badge": "🎯 ਮਿਸ਼ਨ ਥੈਲੇਸੀਮੀਆ ਮੁਕਤ ਭਾਰਤ 2035",
        "title": "🩸 ਥੈਲੇਸੀਮੀਆ ਮਿੱਤਰ (ThalMitra)",
        "caption": "ਮਿਸ਼ਨ ਥੈਲੇਸੀਮੀਆ ਮੁਕਤ ਭਾਰਤ 2035 | ਵਿਆਹ ਤੋਂ ਪਹਿਲਾਂ ਜਾਂਚ ਗਾਈਡ",
        "modes": [
            "💍 ਵਿਆਹ ਤੋਂ ਪਹਿਲਾਂ ਜਾਂਚ (Pre-Marital Check)",
            "🧪 ਕਿਹੜਾ ਟੈਸਟ ਕਰਵਾਉਣਾ ਹੈ? (Test Guide)",
            "💡 ਵਹਿਮ ਬਨਾਮ ਸੱਚ (Myth Busters)"
        ],
        "input_placeholder": "ਥੈਲੇਸੀਮੀਆ ਜਾਂ ਖੂਨ ਦੇ ਟੈਸਟ ਬਾਰੇ ਪੁੱਛੋ...",
        "thinking": "ਥੈਲੇਸੀਮੀਆ ਮਿੱਤਰ ਜਾਣਕਾਰੀ ਇਕੱਠੀ ਕਰ ਰਹੇ ਹਨ...",
        "brand_title": "MISSION THALASSEMIA FREE INDIA 2035",
        "brand_desc": "ਸਾਂਝਾ ਉਪਰਾਲਾ: <b>ਵਿਘਨਹਰਤਾ ਗੋਲਡ ਫਾਊਂਡੇਸ਼ਨ</b> ਅਤੇ <b>Rotary Club of Pune Amanora</b><br>ਵੈੱਬਸਾਈਟ: <a href='https://thalassemia.rcpamanora.org/' target='_blank' style='color:#ff6b6b;'>thalassemia.rcpamanora.org</a>",
        "disclaimer": "⚠️ ਇਹ ਜਾਣਕਾਰੀ ਸਿਰਫ਼ ਜਾਗਰੂਕਤਾ ਲਈ ਹੈ। ਡਾਕਟਰੀ ਸਲਾਹ ਲਈ ਮਾਹਿਰ ਡਾਕਟਰ ਨਾਲ ਸੰਪਰਕ ਕਰੋ।"
    }
}

# ४. भाषा निवड
LANGUAGES = list(LOCALIZATION.keys())

language = st.selectbox(
    "🌐 Choose Language / भाषा निवडा / अपनी भाषा चुनें:",
    LANGUAGES
)

content = LOCALIZATION[language]

# ५. UI हेडर
st.markdown(f"<div style='text-align: center;'><span class='mission-badge'>{content['badge']}</span></div>", unsafe_allow_html=True)
st.title(content["title"])
st.caption(content["caption"])

selected_mode = st.radio(
    "मार्गदर्शन प्रकार:",
    content["modes"],
    horizontal=True,
    label_visibility="collapsed"
)

# ६. सिस्टीम सूचना
system_prompt = (
    "तू 'थॅलेसेमिया मित्र' (ThalMitra AI) आहेस - एक संवेदनशील, वैज्ञानिक आणि विश्वासू डिजिटल समुपदेशक. "
    "हा उपक्रम 'विघ्नहर्ता गोल्ड फाउंडेशन' आणि 'Rotary Club of Pune Amanora' यांच्या 'मिशन थॅलेसेमिया मुक्त भारत २०३५' अंतर्गत चालवला जात आहे. "
    f"सध्या निवडलेली भाषा: {language}. सध्या निवडलेला विभाग: {selected_mode}. "
    f"महत्त्वाचे वैज्ञानिक नियम: "
    f"१. संपूर्ण उत्तर १००% शुद्ध व सहज समजणाऱ्या {language} भाषेतच दे. "
    "२. आदरार्थी, संवेदनशील आणि मित्रासारखी स्पष्ट भाषा वापर. "
    "३. वैज्ञानिक तथ्ये: थॅलेसेमिया मायनर (Carrier) हा आजार नाही; व्यक्ती सामान्य, निरोगी आयुष्य जगू शकते आणि लग्न करू शकते. "
    "केवळ दोन मायनर व्यक्तींचे लग्न झाल्यास बाळाला २५% मेजर (गंभीर आजार) होण्याचा धोका असतो. "
    "लग्नाआधी प्रत्येकाने CBC (यात MCV < 80, MCH < 27) आणि Hb Electrophoresis / HPLC टेस्ट करावी. "
    "४. अधिकृत संकेतस्थळ: अधिक माहितीसाठी thalassemia.rcpamanora.org चा आवर्जून उल्लेख कर."
)

# ७. क्लायंट इनिशियलायझेशन
token_str = st.secrets.get("GEMINI_API_KEY", "").strip()

if not token_str:
    st.info("कृपया Streamlit Secrets मध्ये GEMINI_API_KEY जोडा.", icon="ℹ️")
    st.stop()

@st.cache_resource(show_spinner=False)
def get_client(tok):
    return genai.Client(api_key=tok)

client = get_client(token_str)

# ८. चॅट हिस्ट्री
if "thal_messages" not in st.session_state:
    st.session_state.thal_messages = []

for message in st.session_state.thal_messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ९. प्रश्न हाताळणी
if user_prompt := st.chat_input(content["input_placeholder"]):
    st.session_state.thal_messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    with st.chat_message("assistant"):
        with st.spinner(content["thinking"]):
            try:
                full_input = f"{system_prompt}\n\n[विभाग: {selected_mode}]\nप्रश्न: {user_prompt}"
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=full_input
                )
                if response and response.text:
                    st.markdown(response.text)
                    st.session_state.thal_messages.append({"role": "assistant", "content": response.text})
                else:
                    st.error("उत्तर मिळण्यात अडचण आली, कृपया पुन्हा विचारून पहा.")
            except Exception as e:
                st.error(f"तांत्रिक अडचण: {str(e)}")

# १०. तळटीप ब्रँडिंग व अस्वीकरण
st.markdown(f"""
    <div class='footer-container'>
        <div class='brand-title'>{content["brand_title"]}</div>
        <div class='footer-text'>{content["brand_desc"]}</div>
        <div style='font-size: 11px; color: #777777; margin-top: 10px;'>{content["disclaimer"]}</div>
    </div>
""", unsafe_allow_html=True)

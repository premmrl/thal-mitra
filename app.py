import streamlit as st
import google.generativeai as genai

# १. पेज कॉन्फिगरेशन
st.set_page_config(
    page_title="थॅलेसेमिया मित्र | ThalMitra AI",
    page_icon="🩸",
    layout="centered"
)

# २. आधुनिक CSS स्टाईल (आरोग्य व जनजागृतीसाठी रेड-गोल्ड थीम)
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

# ३. भाषांची यादी (१० प्रमुख भाषा)
LANGUAGES = [
    "मराठी", 
    "हिंदी", 
    "English", 
    "ગુજરાતી (Gujarati)", 
    "ಕನ್ನಡ (Kannada)", 
    "తెలుగు (Telugu)", 
    "தமிழ் (Tamil)", 
    "বাংলা (Bengali)", 
    "മലയാളം (Malayalam)", 
    "ਪੰਜਾਬੀ (Punjabi)"
]

language = st.selectbox(
    "🌐 Choose Language / भाषा निवडा / अपनी भाषा चुनें:",
    LANGUAGES
)

# ४. भाषेनुसार स्थानिक माहिती व विभाग
LOCALIZATION = {
    "मराठी": {
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
        "disclaimer": "⚠️️ ही माहिती केवळ जनजागृती आणि शिक्षणासाठी आहे. वैद्यकीय सल्ल्यासाठी तज्ज्ञ डॉक्टरांचा (Hematologist) सल्ला घ्यावा."
    },
    "हिंदी": {
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
    }
}

content = LOCALIZATION.get(language, LOCALIZATION["मराठी"])

# ५. UI हेडर
st.markdown("<div style='text-align: center;'><span class='mission-badge'>🎯 मिशन थॅलेसेमिया मुक्त भारत २०३५</span></div>", unsafe_allow_html=True)
st.title(content["title"])
st.caption(content["caption"])

selected_mode = st.radio(
    "मार्गदर्शन प्रकार:",
    content["modes"],
    horizontal=True,
    label_visibility="collapsed"
)

# ६. सिस्टीम प्रॉम्ट (वैज्ञानिक, तरुणांना समजणारा व मित्रत्वाचा टोन)
SYSTEM_INSTRUCTION = f"""
तू 'थॅलेसेमिया मित्र' (ThalMitra AI) आहेस - एक संवेदनशील, वैज्ञानिक आणि विश्वासू डिजिटल समुपदेशक.
हा उपक्रम 'विघ्नहर्ता गोल्ड फाउंडेशन' आणि 'Rotary Club of Pune Amanora' यांच्या 'मिशन थॅलेसेमिया मुक्त भारत २०३५' अंतर्गत चालवला जात आहे.

सध्या निवडलेली भाषा: {language}
सध्या निवडलेला मोड: {selected_mode}

महत्त्वाचे वैज्ञानिक नियम व भाषेची शैली:
१. निवडलेल्या भाषेतच ({language}) सोप्या आणि थेट भाषेत उत्तर दे. कॉलेजच्या तरुणांना भीती न वाटता वैज्ञानिक सत्य समजले पाहिजे.
२. लिंग-तटस्थ आणि आदरार्थी भाषा (Gender-Neutral & Respectful) वापर.
३. मूलभूत वैज्ञानिक तथ्ये:
   - थॅलेसेमिया मायनर (Carrier) हा कोणताही आजार नाही; ही व्यक्ती १००% सामान्य, निरोगी आयुष्य जगते, लग्न करू शकते आणि रक्तदानही करू शकते.
   - धोका फक्त तेव्हाच असतो जेव्हा 'मायनर' व्यक्तीचे लग्न दुसऱ्या 'मायनर' व्यक्तीशी होते. अशा वेळी जन्माला येणाऱ्या बाळाला २५% थॅलेसेमिया मेजर (गंभीर विकार) होण्याचा धोका असतो.
   - जर एका जोडीदाराचा रिपोर्ट 'Normal' असेल आणि दुसरा 'Minor' असेल, तरीही बाळ १००% सुरक्षित (Non-Major) राहते.
   - "कुंडली जुळवण्याआधी एक साधी रक्ताची चाचणी करा" या वैज्ञानिक विचाराला प्रोत्साहन दे.
४. तपासणी (Testing Guide):
   - पहिली पायरी: साधी CBC टेस्ट (यात MCV < 80 किंवा MCH < 27 असेल तर शंका येते).
   - अंतिम खात्री: Hb Electrophoresis / HPLC / HbA2 टेस्ट (HbA2 > 3.5% असेल तर मायनर निश्चित होतो).
५. उत्तराची रचना:
   - थेट आणि स्पष्ट उत्तर (२-३ ओळींत).
   - वैज्ञानिक कारण व आनुवंशिकतेचे सोपे गणित.
   - पुढील कृती (Actionable Steps / लॅब टेस्ट).
   - तळाशी १ ओळीची सूचना: "अधिकृत माहितीसाठी thalassemia.rcpamanora.org ला भेट द्या."
"""

# ७. API Key आणि Client कॉन्फिगरेशन
api_key = st.secrets.get("GEMINI_API_KEY", None)
if not api_key:
    st.info("कृपया पुढे जाण्यासाठी API Key आवश्यक आहे.", icon="ℹ️")
    st.stop()

# गुगल जेनेरेटिव्ह AI मॉडेल सेटअप
genai.configure(api_key=api_key)
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=SYSTEM_INSTRUCTION
)

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
                full_prompt = f"[विभाग: {selected_mode}]\nप्रश्न: {user_prompt}"
                response = model.generate_content(full_prompt)
                
                if response and response.text:
                    st.markdown(response.text)
                    st.session_state.thal_messages.append({"role": "assistant", "content": response.text})
                else:
                    st.error("माहिती मिळवण्यात अडचण आली, कृपया पुन्हा प्रयत्न करा.")
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

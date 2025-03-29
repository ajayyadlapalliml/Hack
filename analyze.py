import re
from collections import Counter
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# -------------------- Configuration --------------------
# Sender email and app password
SENDER_EMAIL = "udayachandrika.g@gmail.com"
APP_PASSWORD = "ekye eoan besm jqkg"  # ⚠️ Keep this secure or load from env

# Receiver email
RECEIVER_EMAIL = "shivatejapspk@gmail.com"

# Suspect trigger keywords
SUSPECT_WORDS = {
    "bomb", "war", "terrorism", "protests", "weapons",
    "explosive", "attack", "rebel", "militia", "conflict",
    "assault", "gunfire", "hostage", "radical", "extremist",
    "coup", "insurgency", "threat", "security", "danger",
    "violence", "anarchist", "riot", "subversive", "sabotage"
}

# Common filler words to ignore
FILLER_WORDS = {
    "a", "an", "the", "and", "but", "or", "nor", "for", "yet", "so",
    "at", "around", "by", "after", "along", "from", "of", "on", "to", "with", "without"
}

# -------------------- Helper Functions --------------------

def clean_text(text):
    cleaned_text = re.sub(r'[^\w\s]', '', text.lower())
    return [word for word in cleaned_text.split() if word not in FILLER_WORDS]

def get_top_words(words, n=45):
    return Counter(words).most_common(n)

def check_suspect(top_words):
    top_word_set = {word for word, count in top_words}
    return "Suspect" if top_word_set & SUSPECT_WORDS else "Non-Suspect"

def send_email_alert(subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        server.quit()
        print("✅ Email sent successfully.")
    except Exception as e:
        print("❌ Email failed:", e)

# -------------------- Main Analysis --------------------

def analyze_summary(summary_path):
    with open(summary_path, 'r', encoding='utf-8') as file:
        text = file.read()

    words = clean_text(text)
    top_words = get_top_words(words)
    result = check_suspect(top_words)

    # Save the result
    analysis_result_file = os.path.join("outputs", "analysis_result.txt")
    with open(analysis_result_file, 'w', encoding='utf-8') as file:
        file.write(f"Analysis Result: {result}\n\n")
        file.write("Top Words:\n")
        for word, count in top_words:
            file.write(f"{word}: {count}\n")

    # Trigger email alert if suspect terms found
    if result == "Suspect":
        alert_body = (
            "🚨 ALERT: Suspect words detected in analyzed content.\n"
            f"Top Words:\n" +
            "\n".join([f"- {word} ({count})" for word, count in top_words if word in SUSPECT_WORDS])
        )
        send_email_alert("🚨 Suspect Alert Detected", f"\n\nSummary:\n{text}")


    return analysis_result_file

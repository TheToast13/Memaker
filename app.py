import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import os
import random

# --- KİŞİSELLEŞTİRME FIRSATI ---
# Başlığı ve ikonları değiştirebilirsiniz!
st.set_page_config(page_title="Memaker", page_icon="😹", layout="centered")

st.title("Memaker v0.1")
st.caption("Make ur very own Memes!")

st.sidebar.header("Choose a Picture!")

# ÖNEMLİ: Bu kod M6L4/2 klasöründen çalışacağı için
# 'M6L3/templates' yerine sadece 'templates' diyoruz.
# Çünkü bu klasör app.py'nin yanında olacak.
try:
    dosyalar = os.listdir("templates")
except:
    dosyalar = []
    
yuklenen_dosya = st.sidebar.file_uploader("Load a picture", type=["jpg", "png", "jpeg"])
secilen_sablon = st.sidebar.selectbox("Or select from here!", dosyalar)
resim_yolu = f"templates/{secilen_sablon}"

# --- RESİM AÇMA ---
if yuklenen_dosya is not None:
    orijinal_resim = Image.open(yuklenen_dosya)
else:
    try:
        orijinal_resim = Image.open(resim_yolu)
    except:
        st.error("Picture can't be loaded! Please control the folder 'templates'!")
        st.stop()

resim = orijinal_resim.copy()
boyut = st.sidebar.text_input("Size", "Please enter size")

# --- FİLTRE VE ÇİZİM ---
if st.sidebar.button("80's style"):
    resim = resim.convert("L")

if st.sidebar.button("Done!"):
    done()

draw = ImageDraw.Draw(resim)
# Font dosyasını da yanından alıyor
try:
    font = ImageFont.truetype("font.ttf", boyut)
except:
    font = ImageFont.load_default()

st.sidebar.header("📝 Yazı Ayarları")
ust_yazi = st.sidebar.text_input("Üst Yazı", "Enter txt")
alt_yazi = st.sidebar.text_input("Alt Yazı", "Enter txt")
ust_renk = st.sidebar.color_picker("Üst Renk", "#FFFFFF")
alt_renk = st.sidebar.color_picker("Alt Renk", "#FFFF00") 

if ust_yazi:
    try:
        draw.text((resim.width / 2, boyut), ust_yazi, font=font, fill=ust_renk, anchor="mm")
    except:
        draw.text((resim.width / 2, boyut), ust_yazi, font=font, fill="white", anchor="mm")

if alt_yazi:
    try:
        draw.text((resim.width / 2, resim.height - boyut), alt_yazi, font=font, fill=alt_renk, anchor="mm")
    except:
        draw.text((resim.width / 2, resim.height - boyut), alt_yazi, font=font, fill="white", anchor="mm")

st.image(resim)

def done():
    good_message = ["Wow! Very cool Meme!", "Brilliant!", "It's LoL time!", "I want to be funny like u!", "UNBELIEVABLE!"]
    choosen_message = random.choice("good_message")
    st.balloons()
    st.success(choosen_message)

st.sidebar.markdown("---")
st.sidebar.write(" Made by @--TheToast- on scratch")
st.sidebar.write("17/05/2026")
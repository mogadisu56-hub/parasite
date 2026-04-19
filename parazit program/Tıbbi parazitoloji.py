import streamlit as st
import os

# --- MOBİL SAYFA AYARLARI ---
st.set_page_config(
    page_title="Parazitoloji Veri Bankası", 
    page_icon="🔬",
    layout="centered"
)

# --- KURUMSAL RENKLER VE STİL (CSS) ---
st.markdown("""
    <style>
    .main { background-color: #f5f5f5; }
    .stTextInput > div > div > input {
        background-color: #ffffff;
        border: 2px solid #8b0000;
        border-radius: 10px;
        padding: 10px;
        font-size: 18px !important;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        background-color: #8b0000;
        color: white;
        height: 3em;
        font-weight: bold;
    }
    .result-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #8b0000;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOGO VE ÜST BİLGİ ---
col1, col2 = st.columns([1, 3])
with col1:
    if os.path.exists("logo.png"):
        st.image("logo.png", width=80)
with col2:
    st.markdown("<h3 style='margin-bottom:0;'>KAEÜ Tıp Fakültesi</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color:gray;'>Tıbbi Parazitoloji AD</p>", unsafe_allow_html=True)

st.markdown("---")

# --- AKADEMİK VERİ SETİ (PDF Kaynaklı) ---
import tkinter as tk
from tkinter import messagebox, scrolledtext

# --- AKADEMİK VERİ SETİ (Kısaltılmış Örnek - Tüm liste buraya gelecek) ---
terimler = {
    "Parazitizm": "Bir canlının (parazit) diğerinin (konak) üzerinde veya içinde yaşayarak ondan faydalanması ve ona zarar vermesi durumudur.",
    "Kommensalizm": "Canlılardan birinin fayda sağladığı, diğerinin ise bu durumdan etkilenmediği ilişki türü.",
    "Mutualizm": "İki farklı türün birbirine bağımlı olarak her ikisinin de fayda sağladığı zorunlu yaşam biçimi.",
    "Simbiyoz": "İki farklı türün beraber yaşaması (Kommensalizm, Mutualizm ve Parazitizm alt dallarıdır).",
    "Obligat Parazit": "Yaşam döngüsünü tamamlamak için mutlaka bir konağa ihtiyaç duyan canlı.",
    "Fakültatif Parazit": "Normalde serbest yaşayan ancak uygun ortam bulduğunda parazit olabilen canlı.",
    "Ektoparazit": "Konağın vücut yüzeyinde yaşayan ve enfestasyon yapan canlılar (Örn: Bit, Kene).",
    "Endoparazit": "Konağın doku ve organlarında yaşayan ve enfeksiyon yapan canlılar (Örn: Helminthler).",
    "Son Konak": "Parazitin erişkin şeklinin bulunduğu veya eşeyli üremesinin gerçekleştiği konak.",
    "Ara Konak": "Parazitin larva şekillerinin bulunduğu veya eşeysiz üremesinin gerçekleştiği konak.",
    "Rezervuar Konak": "Paraziti doğada barındıran ve insan enfeksiyonu için kaynak oluşturan hayvan.",
    "Vektör": "Patojen bir etkeni bir konaktan diğerine taşıyan eklembacaklı (Biyolojik veya Mekanik).",
    "Prepatens Süre": "Konağa girişten, tanısal formların (yumurta, kist vb.) görülmesine kadar geçen süre.",
    "Patens Süre": "Parazitin konak vücudunda tanısal formlar üretmeye devam ettiği toplam süre.",
    "Zoonoz": "Hayvanlardan insanlara doğal yollarla bulaşan paraziter hastalıklar.",
    "Miyazis": "Sinek larvalarının canlı doku veya organlara yerleşmesi.",
    "Otoyenfeksiyon": "Kişinin kendi vücudundaki parazit formlarıyla kendini tekrar enfekte etmesi.",
    "Hiperparazitlik": "Bir parazitin başka bir parazit üzerinde yaşaması.",
    "İnsidans": "Belirli bir sürede, belirli bir toplumda yeni ortaya çıkan vaka sayısı.",
    "Prevalans": "Belirli bir zamanda, belirli bir toplumda var olan toplam vaka sayısı.",
    "Patojenite": "Bir parazitin konakta hastalık oluşturabilme yeteneği.",
    "Virülans": "Bir patojenin hastalık yapma derecesi veya şiddeti.",
    "Mekanik Vektör": "Parazitin içinde hiçbir gelişme evresi geçirmeden sadece taşındığı vektör.",
    "Biyolojik Vektör": "Parazitin yaşam döngüsünün bir kısmını vektörün içinde tamamladığı taşıyıcı."
}

# --- 2. BÖLÜM: TÜM PARAZİTLER LİSTESİ (TAM LİSTE & BÜYÜK HARF) ---
parazit_verisi = {
    # --- AMİPLER (AMEBAE) ---
    "Entamoeba histolytica": "MORFOLOJİ: Trofozoit (merkezi endozom), Kist (1-4 çekirdek). | DÖNGÜ: Kist alımı -> Kalın bağırsak yerleşimi. | TANI: Dışkıda hematofaj trofozoit. | TEDAVİ: Metronidazol.",
    "Entamoeba hartmanni": "BİLGİ: Non-patojen amip. E. histolytica'ya benzer ancak daha küçüktür (<10µm).",
    "Entamoeba coli": "MORFOLOJİ: Kist 8 çekirdekli, eksantrik endozom. BİLGİ: Non-patojen bağırsak kommensali.",
    "Entamoeba polecki": "BİLGİ: Domuz/maymun amibi. TANI: Tek çekirdekli kist yapısı karakteristiktir.",
    "Endolimax nana": "BİLGİ: En küçük bağırsak amibi. Kisti 4 çekirdekli ve ovaldir. Non-patojen.",
    "Iodamoeba bütschlii": "BİLGİ: Kistinde iyot ile boyanan çok büyük bir glikojen vakuolü bulunur. Non-patojen.",
    "Entamoeba gingivalis": "BİLGİ: Sadece trofozoit formu vardır. Diş eti ve ağız hijyeni ile ilişkilidir.",
    "Naegleria fowleri": "BİLGİ: PAM (Primer Amibik Meningoensefalit) etkeni. Burun yoluyla MSS'ye girer.",
    "Acanthamoeba türleri": "BİLGİ: Keratit (lens kullanıcıları) ve GAE etkeni. Çift çeperli kist yapısı.",

    # --- KAMÇILILAR (FLAGELLATES) ---
    "Giardia intestinalis": "MORFOLOJİ: Vantuzlu trofozoit. | DÖNGÜ: Duodenum yerleşimi. | KLİNİK: Steatore. | TEDAVİ: Metronidazol.",
    "Chilomastix mesnili": "BİLGİ: Limon şeklinde kist yapısı tipiktir. Non-patojen bağırsak kamçılısı.",
    "Dientamoeba fragilis": "BİLGİ: Kisti yoktur. Trofozoit formu amip gibi görünse de kamçılıdır.",
    "Trichomonas hominis": "BİLGİ: Kalın bağırsak yerleşimli non-patojen kamçılı. Kisti yoktur.",
    "Enteromonas hominis": "BİLGİ: Küçük, non-patojen bağırsak kamçılısı.",
    "Retortamonas intestinalis": "BİLGİ: Nadir görülen, non-patojen bir bağırsak kamçılısıdır.",
    "Trichomonas tenax": "BİLGİ: Ağız boşluğu kommensali. Diş eti hastalıklarında görülür.",
    "Trichomonas vaginalis": "BİLGİ: Ürogenital patojen. STD etkeni. TANI: Akıntıda sıçrayıcı trofozoit.",

    # --- HEMOFLAGELLATLAR ---
    "Leishmania braziliensis kompleksi": "KLİNİK: Mukokutanöz Leishmaniasis (Espundia). Vektör: Phlebotomine.",
    "Leishmania donovani kompleksi": "KLİNİK: Viseral Leishmaniasis (Kala-azar). TANI: Kemik iliğinde LD cisimcikleri.",
    "Leishmania mexicana kompleksi": "KLİNİK: Yeni Dünya kutanöz leishmaniasis.",
    "Leishmania tropica kompleksi": "KLİNİK: Eski Dünya kutanöz leishmaniasis (Şark Çıbanı).",
    "Trypanosoma brucei gambiense": "KLİNİK: Batı Afrika Uyku Hastalığı. Vektör: Glossina.",
    "Trypanosoma brucei rhodesiense": "KLİNİK: Doğu Afrika Uyku Hastalığı. Daha akut seyir.",
    "Trypanosoma cruzi": "KLİNİK: Chagas Hastalığı. Vektör: Triatomine. C-şekilli tripomastigot.",
    "Trypanosoma rangeli": "BİLGİ: Güney Amerika'da yaygın, insan için non-patojen.",

    # --- SPOROZOONLAR ---
    "Plasmodium vivax": "KLİNİK: Tersiyana sıtması. Schüffner noktaları mevcuttur.",
    "Plasmodium ovale": "KLİNİK: Tersiyana benzeri sıtma. James noktaları görülür.",
    "Plasmodium malariae": "KLİNİK: Kuartana sıtması (72 saat). Bant formu trofozoit.",
    "Plasmodium falciparum": "KLİNİK: Malign sıtma. Muz şeklinde gametosit ve Maurer noktaları.",
    "Plasmodium knowlesi": "KLİNİK: Primat sıtması (24 saatlik döngü). Güneydoğu Asya.",
    "Babesia microti": "KLİNİK: Kene ile bulaş. Eritrosit içi 'Maltız Haçı' görünümü.",
    "Babesia divergens": "KLİNİK: Sığırlardan bulaşır, ağır seyreder.",

    # --- DİĞER PROTOZOONLAR ---
    "Balantidium coli": "KLİNİK: Patojen tek siliyat. Rezervuar: Domuz. Fasulye şeklinde makronükleus.",
    "Isospora belli": "BİLGİ: İnce bağırsak epiteli. TANI: Dışkıda eliptik ookistler.",
    "Sarcocystis türleri": "BİLGİ: İnsan hem ara konak hem son konak olabilir.",
    "Cryptosporidium parvum": "KLİNİK: HIV hastalarında ağır ishal. TANI: Modifiye Asit-Fast boyama.",
    "Blastocystis hominis": "BİLGİ: Vakuollü form en yaygın formdur.",
    "Cyclospora cayetanensis": "BİLGİ: Meyve/sebze ile bulaş. Asido-rezistan ookistler.",
    "Microsporidia": "BİLGİ: Hücre içi zorunlu parazit. Polar tüp içerir.",
    "Toxoplasma gondii": "BİLGİ: Son konak kedidir. Gebelerde teratojenik risk.",
    "Pneumocystis jiroveci": "KLİNİK: PCP (Pneumocystis pnömonisi). TANI: Gümüşleme boyama.",

    # --- NEMATODLAR ---
    "Enterobius vermicularis": "KLİNİK: Kıl kurdu. TANI: Selofan bant yöntemi (Yumurta asimetrik D harfi).",
    "Trichuris trichiura": "KLİNİK: Kamçı kurdu. TANI: Limon şeklinde, çift tıkaçlı yumurta.",
    "Ascaris lumbricoides": "KLİNİK: En büyük nematod. Akciğer göçü (Loeffler sendromu).",
    "Necator americanus": "KLİNİK: Yeni dünya kancalı kurdu. Kesici plaklar ile anemi yapar.",
    "Ancylostoma duodenale": "KLİNİK: Eski dünya kancalı kurdu. Dişli ağız yapısı.",
    "Strongyloides stercoralis": "KLİNİK: Larva akurens. Dışkıda rabditiform larva görülür.",
    "Trichinella spiralis": "KLİNİK: Kaslarda kist. Periorbital ödem ve kas ağrısı.",
    "Dracunculus medinensis": "KLİNİK: Medine solucanı. Ara konak: Cyclops.",

    # --- FİLARİALAR ---
    "Wuchereria bancrofti": "KLİNİK: Fil hastalığı. Gece periyodik mikrofilar. Vektör: Sivrisinek.",
    "Brugia malayi": "KLİNİK: Lenfatik filariyazis. Güneydoğu Asya.",
    "Loa loa": "KLİNİK: Göz solucanı. Calabar şişlikleri. Vektör: Chrysops.",
    "Onchocerca volvulus": "KLİNİK: Nehir körlüğü. Vektör: Simulium.",

    # --- SESTODLAR ---
    "Taenia saginata": "KLİNİK: Sığır şeridi. Skolekste çengel yok. Proglottidler hareketli.",
    "Taenia solium": "KLİNİK: Domuz şeridi. Sistiserkozis (beyin/göz yerleşimi).",
    "Hymenolepis nana": "KLİNİK: Cüce şerit. En sık görülen sestod.",
    "Hymenolepis diminuta": "KLİNİK: Fare şeridi. Ara konak (böcek) zorunludur.",
    "Diphyllobothrium latum": "KLİNİK: Balık şeridi. Vitamin B12 eksikliği anemisi.",
    "Echinococcus granulosus": "KLİNİK: Kist hidatik etkeni. Karaciğer ve akciğer tutulumu.",

    # --- TREMATODLAR ---
    "Fasciola hepatica": "KLİNİK: Karaciğer kelebeği. TANI: Operkulumlu büyük yumurta.",
    "Clonorchis sinensis": "KLİNİK: Çin karaciğer kelebeği. Safra yolları yerleşimi.",
    "Schistosoma mansoni": "KLİNİK: Kan fluku. Dışkıda lateral dikenli yumurta.",
    "Schistosoma haematobium": "KLİNİK: Üriner sistem. İdrarda terminal dikenli yumurta.",

    # --- ARTROPODLAR ---
    "Pediculus humanus capitis": "BİLGİ: Baş biti. Saçlı deri yerleşimi. Sirke tespiti.",
    "Pthirus pubis": "BİLGİ: Kasık biti. Mavi lekeler yapar.",
    "Lucilia sericata": "BİLGİ: Yeşil şişe sineği. MDT (Maggot Terapi) etkeni.",
    "Sarcoptes scabiei": "BİLGİ: Uyuz etkeni. Deride 'Sillon' tünelleri açar.",
    "Ixodes türleri": "BİLGİ: Sert kene. Lyme ve Babesiosis vektörü.",
    "Phlebotomus türleri": "BİLGİ: Tatarcık. Leishmaniasis vektörü.",
    "Glossina türleri": "BİLGİ: Çeçe sineği. Uyku hastalığı vektörü."
}

class ParazitApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tıbbi Parazitoloji Akademik Sorgulama Sistemi v12.0")
        self.root.geometry("700x550")
        self.root.configure(bg="#f0f0f0")

        # Başlık
        self.label_title = tk.Label(root, text="PARAZİTOLOJİ EĞİTİM VE SORGULAMA", 
                                    font=("Helvetica", 16, "bold"), bg="#2c3e50", fg="white", pady=10)
        self.label_title.pack(fill=tk.X)

        # Talimat
        self.label_instr = tk.Label(root, text="Parazit adını veya terimi harfi harfine yazınız:", 
                                    font=("Helvetica", 10, "italic"), bg="#f0f0f0")
        self.label_instr.pack(pady=10)

        # Giriş Kutusu (Burada harfi harfine yazım kontrol edilecek)
        self.entry_sorgu = tk.Entry(root, font=("Courier New", 14), width=40, justify='center')
        self.entry_sorgu.pack(pady=5)
        self.entry_sorgu.bind("<Return>", lambda event: self.sorgula()) # Enter tuşu ile sorgulama

        # Sorgula Butonu
        self.btn_ara = tk.Button(root, text="BİLGİLERİ GETİR", command=self.sorgula, 
                                 bg="#27ae60", fg="white", font=("Helvetica", 10, "bold"), padx=20)
        self.btn_ara.pack(pady=10)

        # Sonuç Alanı
        self.txt_sonuc = scrolledtext.ScrolledText(root, width=80, height=15, font=("Helvetica", 11))
        self.txt_sonuc.pack(pady=10, padx=20)
        self.txt_sonuc.config(state=tk.DISABLED) # Başta düzenlenemez yapıyoruz

        # Alt Bilgi
        self.label_footer = tk.Label(root, text="Kırşehir Ahi Evran Üniversitesi - Tıbbi Parazitoloji AD", 
                                     font=("Helvetica", 8), bg="#f0f0f0", fg="gray")
        self.label_footer.pack(side=tk.BOTTOM, pady=5)

    def sorgula(self):
        sorgu = self.entry_sorgu.get().strip()
        sonuc_metni = ""
        found = False

        # Terim Kontrolü
        for t_key in terimler:
            if t_key.lower() == sorgu.lower():
                sonuc_metni = f"BAŞLIK: {t_key.upper()}\n\nKATEGORİ: Akademik Terim\n\nTANIM: {terimler[t_key]}"
                found = True
                break
        
        # Parazit Kontrolü
        if not found:
            for p_key in parazit_verisi:
                if p_key.lower() == sorgu.lower():
                    detaylar = parazit_verisi[p_key].replace(" | ", "\n\n")
                    sonuc_metni = f"TÜR: {p_key.upper()}\n\nKATEGORİ: Tıbbi Parazit\n\nDETAYLAR:\n{detaylar}"
                    found = True
                    break

        # Sonucu Ekrana Yazdır
        self.txt_sonuc.config(state=tk.NORMAL)
        self.txt_sonuc.delete(1.0, tk.END)
        
        if found:
            self.txt_sonuc.insert(tk.INSERT, sonuc_metni)
        else:
            messagebox.showerror("Yazım Hatası", "Kayıt bulunamadı!\n\nİsmi harfi harfine doğru yazdığınızdan emin olun.\nÖrn: Entamoeba histolytica")
            self.txt_sonuc.insert(tk.INSERT, "Sorgulanan içerik bulunamadı. Lütfen nomenklatür kurallarına göre tekrar deneyiniz.")
        
        self.txt_sonuc.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = ParazitApp(root)
    root.mainloop()

# --- ÖĞRENCİ SORGULAMA EKRANI ---
st.markdown("#### 🔬 Parazit/Terim Sorgula")
sorgu = st.text_input("", placeholder="Örn: Entamoeba histolytica", help="Tam ve doğru yazım gereklidir.")

if st.button("BİLGİLERİ GETİR") or sorgu:
    if sorgu:
        all_data = {**terimler, **parazit_verisi}
        found = False
        
        # Harfi harfine eşleşme kontrolü
        for key, value in all_data.items():
            if key.lower() == sorgu.lower():
                st.markdown(f"""
                <div class='result-card'>
                    <h3 style='color:#8b0000;'>{key.upper()}</h3>
                    <p><b>Kategori:</b> {'Tıbbi Parazit' if key in parazit_verisi else 'Akademik Terim'}</p>
                    <hr>
                    {value.replace(' | ', '<br><br>')}
                </div>
                """, unsafe_allow_html=True)
                found = True
                break
        
        if not found:
            st.error("❌ Kayıt bulunamadı. Lütfen Latince ismin yazılışını kontrol edin. Tek bir harf hatası bile kabul edilmez.")
    else:
        st.warning("Lütfen bir isim yazın.")

# --- MOBİL ALT MENÜ ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("© 2026 Tıbbi Parazitoloji Akademik Rehberi")
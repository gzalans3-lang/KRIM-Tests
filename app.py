import streamlit as st
import time

st.set_page_config(page_title="Tiesību pamatu tests", page_icon="⚖️", layout="centered")

# Jautājumu bāze
questions = [
    {
        "q": "1. Kāda ir amatpersonas (procesa virzītāja) rīcība, kad kļuvis zināms kriminālprocesa uzsākšanas iemesls un pamats?",
        "options": [
            "A) Uzsākt kriminālprocesu un novest to līdz taisnīgam noregulējumam",
            "B) Nogaidīt līdz parādās cietušā iesniegums",
            "C) Uzsākt operatīvo izstrādi bez procesa uzsākšanas"
        ],
        "answer": 0
    },
    {
        "q": "2. Saskaņā ar kuru likumu tiek veikta noziedzīgu nodarījumu profilakse, novēršana un atklāšana, kā arī pierādījumu avotu noskaidrošana?",
        "options": [
            "A) Kriminālprocesa likumu",
            "B) Operatīvās darbības likumu",
            "C) Likumu 'Par policiju'"
        ],
        "answer": 1
    },
    {
        "q": "3. Kas ir galvenais mērķis operatīvajai meklēšanai un citiem pasākumiem saskaņā ar likumu 'Par policiju'?",
        "options": [
            "A) Sodīt vainīgās personas uz vietas",
            "B) Atklāt, pārtraukt un novērst noziedzīgus nodarījumus, konstatēt un meklēt vainīgos",
            "C) Veikt iedzīvotāju izglītošanu par drošību"
        ],
        "answer": 1
    },
    {
        "q": "4. Kuros likumos ir tieši nostiprināta prasība garantēt cilvēktiesības tiesībsargājošo iestāžu darbībā?",
        "options": [
            "A) Tikai Satversmē",
            "B) Operatīvās darbības likumā, Kriminālprocesa likumā un likumā 'Par policiju'",
            "C) Tikai Kriminālprocesa likumā"
        ],
        "answer": 1
    },
    {
        "q": "5. Ko Kriminālprocesa likuma izpratnē nozīmē 'krimināltiesisko attiecību taisnīgs noregulējums'?",
        "options": [
            "A) Jebkura soda piemērošana bez tiesas izmeklēšanas",
            "B) Kompromisa rašana starp cietušo un aizdomās turēto bez valsts iejaukšanās",
            "C) Krimināltiesiskā strīda atrisināšana atbilstoši likuma prasībām, ievērojot personu tiesības"
        ],
        "answer": 2
    },
    {
        "q": "6. Ja policijas darbiniekam ir pamats uzskatīt, ka persona gatavo noziegumu, kādi pasākumi jāveic saskaņā ar likumu 'Par policiju'?",
        "options": [
            "A) Operatīvās meklēšanas un citi likumā noteiktie pasākumi, lai to pārtrauktu un novērstu",
            "B) Jāziņo pašvaldībai un jāgaida lēmums",
            "C) Jālūdz persona rakstiski paskaidrot savus nolūkus"
        ],
        "answer": 0
    },
    {
        "q": "7. Pierādījumu avotu noskaidrošana ir specifisks uzdevums, ko primāri reglamentē:",
        "options": [
            "A) Administratīvās atbildības likums",
            "B) Operatīvās darbības likums",
            "C) Civilprocesa likums"
        ],
        "answer": 1
    },
    {
        "q": "8. Amatpersonas kompetences ietvaros uzsākts kriminālprocess nozīmē, ka:",
        "options": [
            "A) Amatpersona to var pārtraukt pēc saviem ieskatiem bez pamatojuma",
            "B) Amatpersonai ir pienākums veikt izmeklēšanu un novest to līdz noregulējumam",
            "C) Amatpersona nodod to privātām detektīvaģentūrām"
        ],
        "answer": 1
    }
]

# Inicializējam sesijas mainīgos
if 'current_q' not in st.session_state:
    st.session_state.current_q = 0
    st.session_state.score = 0
    st.session_state.finished = False
    st.session_state.time_left = 50

def trigger_next_question(selected_option=None):
    """Pārslēdz uz nākamo jautājumu un atiestata laiku"""
    if selected_option is not None:
        if selected_option == questions[st.session_state.current_q]["answer"]:
            st.session_state.score += 1
            
    if st.session_state.current_q < len(questions) - 1:
        st.session_state.current_q += 1
        st.session_state.time_left = 50
    else:
        st.session_state.finished = True

st.title("⚖️ Tiesībsargājošo iestāžu darbības pamati")
st.markdown("Pārbaudi savas zināšanas! Katram jautājumam dotas **50 sekundes**.")

if st.session_state.finished:
    st.success(f"Tests pabeigts! Jūsu rezultāts: {st.session_state.score} no {len(questions)}")
    if st.button("Sākt no jauna"):
        st.session_state.current_q = 0
        st.session_state.score = 0
        st.session_state.finished = False
        st.session_state.time_left = 50
        st.rerun()
else:
    q_data = questions[st.session_state.current_q]
    st.subheader(q_data["q"])
    
    st.progress((st.session_state.current_q) / len(questions))
    
    # Izveidojam dinamisku vietu laika atskaitei, lai tā vizuāli tikšķētu
    timer_placeholder = st.empty()
    
    # Atbilžu pogu izkārtojums (tiek parādīts pirms laika cikla sākuma)
    for i, option in enumerate(q_data["options"]):
        if st.button(option, key=f"btn_{st.session_state.current_q}_{i}"):
            trigger_next_question(i)
            st.rerun()

    st.write("") # Atstarpe vizuālajam izskatam
    st.caption("Anonīms tests, dati netiek saglabāti vai apstrādāti saskaņā ar VDAR/GDPR principiem.")

    # Aktīvais laika atskaites cikls (katru sekundi pārzīmē tikai laika logu)
    while st.session_state.time_left > 0:
        timer_placeholder.info(f"⏳ Atlicis laiks: {st.session_state.time_left} sekundes")
        time.sleep(1)
        st.session_state.time_left -= 1
        st.rerun()

    # Ja laiks ir 0 un lietotājs nav nospiedis nevienu pogu
    if st.session_state.time_left == 0:
        trigger_next_question(selected_option=None)
        st.rerun()

import streamlit as st
import pandas as pd 
import base64
import codecs
t1 = r"t1.PNG"
t2 = r"python.png"
t3 = r"t3.jpeg"
logo = r"icons.png"
st.markdown(f"""<p>
                    <img style="float:left; height: 50px;
            width: 50px;"  src="data:image/png;base64,{base64.b64encode(open(logo, "rb").read()).decode()}"></p>
                    <h2 style="font-family:Bradley Hand, cursive;"> SanSamSak</h2>""", unsafe_allow_html=True)
st.markdown(f"""<p >
                    <img style="float:right; height: 250px;
            width: 350px;" class="logo-img" src="data:image/png;base64,{base64.b64encode(open(t1, "rb").read()).decode()}">
                    </p><br><br>
                    <h2 class="sc-1vqnue2-2 DnHbM">Nous simplifions la gestion des fichiers <span style="color : #61C653;">CSV</span></h2>""", unsafe_allow_html=True)

st.markdown("""<center><hr size="6" width="50%"  color="#838982"></center>""", unsafe_allow_html=True)
st.markdown(f"""<p >
                            <img style="float:left; height: 250px;
            width: 350px;" class="logo-img" src="data:image/png;base64,{base64.b64encode(open(t2, "rb").read()).decode()}">
                            </p><br>
                            <h2 style="font-family:Verdana, sans-serif; padding-left:55%;">Filtrage des données </h2>
                            <p style="font-family:Andale Mono, monospace;-webkit-font-smoothing: antialiased;
            font-stretch: 400;
            font-weight: 400;padding-left:55%;">Supprimer des colonnes, supprimer les redondances.
                                        Renommer des colonnes.
                                    </p>""", unsafe_allow_html=True)

st.markdown("""<center><hr size="6" width="50%"  color="#838982"></center>""", unsafe_allow_html=True)
st.markdown(f"""<p >
                            <img style="float:right;height: 250px;
            width: 350px;" class="logo-img" src="data:image/png;base64,{base64.b64encode(open(t3, "rb").read()).decode()}">
                            </p><br>
                            <h2 style="font-family:Verdana, sans-serif;">Gestion des graphes</h2>
                                    <p style="font-family:Andale Mono, monospace;">Construire des graphes (Courbes, Diagramme circulaire ...).</p>
                                    """, unsafe_allow_html=True)
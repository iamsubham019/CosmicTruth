import os
<<<<<<< HEAD
<<<<<<< HEAD
=======
import io
>>>>>>> caec3e7300fade99d6c3b5550bd54dd2ee3253c1
=======
import io
>>>>>>> caec3e7300fade99d6c3b5550bd54dd2ee3253c1
import json
import torch
import numpy as np
import streamlit as st
<<<<<<< HEAD
<<<<<<< HEAD
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image
from transformers import AutoTokenizer

from config import CFG, LABEL_MAP
=======
=======
>>>>>>> caec3e7300fade99d6c3b5550bd54dd2ee3253c1
import matplotlib.pyplot as plt
from PIL import Image
from transformers import AutoTokenizer
import torchvision.transforms as transforms

from config import CFG, LABEL_MAP, LABEL_COLORS
<<<<<<< HEAD
>>>>>>> caec3e7300fade99d6c3b5550bd54dd2ee3253c1
=======
>>>>>>> caec3e7300fade99d6c3b5550bd54dd2ee3253c1
from models.detector import FakeNewsDetector
from xai.explainer import UnifiedExplainer
from data.dataset import get_image_transform


st.set_page_config(
<<<<<<< HEAD
<<<<<<< HEAD
    page_title="CosmicTruth — Fake News Detector",
    page_icon="🌌",
=======
    page_title="Multimodal Fake News Detector",
    page_icon="🔍",
>>>>>>> caec3e7300fade99d6c3b5550bd54dd2ee3253c1
=======
    page_title="Multimodal Fake News Detector",
    page_icon="🔍",
>>>>>>> caec3e7300fade99d6c3b5550bd54dd2ee3253c1
    layout="wide",
    initial_sidebar_state="expanded",
)

<<<<<<< HEAD
<<<<<<< HEAD
COSMIC_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Exo+2:wght@300;400;600&display=swap');
.stApp { background: #030712 !important; font-family: 'Exo 2', sans-serif !important; color: #c4d4e8 !important; }
.stApp::before {
    content: ''; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
    pointer-events: none; z-index: 0;
    background-image:
        radial-gradient(1px 1px at 10% 15%, rgba(232,244,255,0.9) 0%, transparent 100%),
        radial-gradient(1px 1px at 25% 40%, rgba(232,244,255,0.7) 0%, transparent 100%),
        radial-gradient(1.5px 1.5px at 40% 8%, rgba(167,139,250,0.9) 0%, transparent 100%),
        radial-gradient(1px 1px at 55% 60%, rgba(232,244,255,0.6) 0%, transparent 100%),
        radial-gradient(1px 1px at 70% 25%, rgba(232,244,255,0.8) 0%, transparent 100%),
        radial-gradient(1.5px 1.5px at 82% 45%, rgba(125,211,252,0.9) 0%, transparent 100%),
        radial-gradient(1px 1px at 92% 12%, rgba(232,244,255,0.7) 0%, transparent 100%),
        radial-gradient(1px 1px at 5% 75%, rgba(232,244,255,0.5) 0%, transparent 100%),
        radial-gradient(1.5px 1.5px at 88% 65%, rgba(251,191,36,0.8) 0%, transparent 100%),
        radial-gradient(1px 1px at 30% 20%, rgba(232,244,255,0.9) 0%, transparent 100%),
        radial-gradient(1px 1px at 73% 5%, rgba(232,244,255,0.9) 0%, transparent 100%);
    animation: starTwinkle 6s ease-in-out infinite alternate;
}
@keyframes starTwinkle { 0% { opacity:0.6; } 50% { opacity:1.0; } 100% { opacity:0.7; } }
[data-testid="stSidebar"] { background: linear-gradient(180deg,#0f0728 0%,#07111e 60%,#030712 100%) !important; border-right:1px solid rgba(167,139,250,0.2) !important; }
[data-testid="stSidebar"] * { color:#c4d4e8 !important; }
.main .block-container { padding-top:1.5rem !important; position:relative; z-index:1; }
h1,h2,h3 { font-family:'Orbitron',monospace !important; color:#e8f4ff !important; }
.cosmic-title { font-family:'Orbitron',monospace; font-size:2.4rem; font-weight:900; letter-spacing:0.08em; background:linear-gradient(135deg,#a78bfa 0%,#818cf8 30%,#7dd3fc 60%,#34d399 100%); -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text; margin-bottom:0.2rem; animation:titlePulse 4s ease-in-out infinite; line-height:1.2; }
@keyframes titlePulse { 0%,100%{filter:brightness(1);} 50%{filter:brightness(1.3);} }
.cosmic-subtitle { font-family:'Exo 2',sans-serif; font-size:0.85rem; color:rgba(167,139,250,0.6); letter-spacing:0.15em; text-transform:uppercase; margin-bottom:1.5rem; }
.orbit-decoration { width:100%; height:2px; background:linear-gradient(90deg,transparent 0%,rgba(167,139,250,0.6) 30%,rgba(125,211,252,0.8) 50%,rgba(52,211,153,0.6) 70%,transparent 100%); margin:0.5rem 0 1.5rem; border-radius:2px; animation:orbitScan 3s linear infinite; background-size:200% 100%; }
@keyframes orbitScan { 0%{background-position:200% 0;} 100%{background-position:-200% 0;} }
.cosmos-card { background:linear-gradient(135deg,rgba(15,7,40,0.95),rgba(10,22,40,0.9)); border:1px solid rgba(167,139,250,0.25); border-radius:16px; padding:1.25rem; margin-bottom:1rem; position:relative; overflow:hidden; }
.cosmos-card::before { content:''; position:absolute; top:0;left:0;right:0;height:2px; background:linear-gradient(90deg,transparent,rgba(167,139,250,0.8),rgba(125,211,252,0.8),transparent); }
.metric-card { background:linear-gradient(135deg,rgba(15,7,40,0.9),rgba(7,17,30,0.95)); border-radius:12px; padding:1rem 0.75rem; text-align:center; border:1px solid rgba(167,139,250,0.2); transition:all 0.3s; }
.metric-card:hover { border-color:rgba(167,139,250,0.5); transform:translateY(-2px); }
.metric-value { font-size:1.6rem; font-weight:700; font-family:'Orbitron',monospace; }
.metric-label { font-size:0.65rem; color:rgba(167,139,250,0.55); margin-top:4px; letter-spacing:0.12em; text-transform:uppercase; }
.pred-real { background:rgba(52,211,153,0.15); color:#34d399; padding:0.35rem 1.2rem; border-radius:999px; font-size:1rem; font-weight:700; font-family:'Orbitron',monospace; border:1px solid rgba(52,211,153,0.4); letter-spacing:0.05em; animation:glowGreen 2s ease-in-out infinite; }
.pred-fake { background:rgba(248,113,113,0.15); color:#f87171; padding:0.35rem 1.2rem; border-radius:999px; font-size:1rem; font-weight:700; font-family:'Orbitron',monospace; border:1px solid rgba(248,113,113,0.4); letter-spacing:0.05em; animation:glowRed 2s ease-in-out infinite; }
@keyframes glowGreen { 0%,100%{box-shadow:0 0 8px rgba(52,211,153,0.3);} 50%{box-shadow:0 0 20px rgba(52,211,153,0.6);} }
@keyframes glowRed   { 0%,100%{box-shadow:0 0 8px rgba(248,113,113,0.3);} 50%{box-shadow:0 0 20px rgba(248,113,113,0.6);} }
.section-header { font-family:'Orbitron',monospace; font-size:0.78rem; font-weight:700; color:#a78bfa; margin:1.5rem 0 0.75rem; letter-spacing:0.12em; text-transform:uppercase; display:flex; align-items:center; gap:8px; }
.section-header::after { content:''; flex:1; height:1px; background:linear-gradient(90deg,rgba(167,139,250,0.5),transparent); }
.token-highlight { display:inline-block; padding:2px 7px; border-radius:5px; margin:2px; font-size:0.82rem; border:1px solid transparent; font-family:'Exo 2',sans-serif; }
.top-token { background:linear-gradient(135deg,rgba(167,139,250,0.12),rgba(79,70,229,0.08)); border:1px solid rgba(167,139,250,0.28); border-radius:8px; padding:0.6rem 0.5rem; text-align:center; }
.top-token .rank { font-family:'Orbitron',monospace; font-size:0.6rem; color:rgba(167,139,250,0.45); }
.top-token .word { font-size:1rem; font-weight:600; color:#e8f4ff; margin:4px 0; }
.top-token .score { font-family:'Orbitron',monospace; font-size:0.68rem; color:#34d399; }
.conf-bar-outer { width:100%; height:5px; background:rgba(167,139,250,0.1); border-radius:3px; overflow:hidden; margin-top:5px; }
.conf-bar-inner { height:100%; border-radius:3px; background:linear-gradient(90deg,#a78bfa,#34d399); }
.planet-orb { width:52px; height:52px; border-radius:50%; background:radial-gradient(circle at 35% 35%,rgba(167,139,250,0.9),rgba(79,70,229,0.7),rgba(30,27,75,0.95)); box-shadow:0 0 20px rgba(167,139,250,0.4),0 0 40px rgba(167,139,250,0.15); animation:planetGlow 4s ease-in-out infinite; display:inline-block; margin-right:1rem; vertical-align:middle; }
@keyframes planetGlow { 0%,100%{box-shadow:0 0 20px rgba(167,139,250,0.4),0 0 40px rgba(167,139,250,0.15);} 50%{box-shadow:0 0 30px rgba(52,211,153,0.5),0 0 50px rgba(52,211,153,0.2);} }
.stTextArea textarea { background:rgba(10,22,40,0.8) !important; border:1px solid rgba(167,139,250,0.3) !important; border-radius:10px !important; color:#c4d4e8 !important; font-family:'Exo 2',sans-serif !important; }
.stTextArea textarea:focus { border-color:rgba(167,139,250,0.7) !important; box-shadow:0 0 15px rgba(167,139,250,0.2) !important; }
.stSelectbox > div > div { background:rgba(10,22,40,0.8) !important; border:1px solid rgba(167,139,250,0.3) !important; color:#c4d4e8 !important; border-radius:10px !important; }
.stButton > button { background:linear-gradient(135deg,rgba(167,139,250,0.18),rgba(129,140,248,0.12)) !important; color:#a78bfa !important; border:1px solid rgba(167,139,250,0.45) !important; border-radius:10px !important; font-family:'Orbitron',monospace !important; font-size:0.75rem !important; letter-spacing:0.08em !important; font-weight:700 !important; transition:all 0.3s !important; }
.stButton > button:hover { background:linear-gradient(135deg,rgba(167,139,250,0.32),rgba(129,140,248,0.25)) !important; box-shadow:0 0 18px rgba(167,139,250,0.25) !important; transform:translateY(-1px) !important; }
.stButton > button[kind="primary"] { background:linear-gradient(135deg,rgba(167,139,250,0.3),rgba(52,211,153,0.18)) !important; border-color:rgba(167,139,250,0.65) !important; color:#e8f4ff !important; font-size:0.82rem !important; }
.stTabs [data-baseweb="tab-list"] { background:rgba(10,22,40,0.6) !important; border-radius:12px !important; padding:4px !important; border:1px solid rgba(167,139,250,0.2) !important; }
.stTabs [data-baseweb="tab"] { font-family:'Orbitron',monospace !important; font-size:0.68rem !important; letter-spacing:0.06em !important; color:rgba(167,139,250,0.55) !important; border-radius:8px !important; }
.stTabs [aria-selected="true"] { background:linear-gradient(135deg,rgba(167,139,250,0.22),rgba(129,140,248,0.14)) !important; color:#a78bfa !important; border:1px solid rgba(167,139,250,0.38) !important; }
[data-testid="metric-container"] { background:rgba(10,22,40,0.6) !important; border:1px solid rgba(167,139,250,0.2) !important; border-radius:10px !important; padding:0.75rem !important; }
[data-testid="metric-container"] label { color:rgba(167,139,250,0.55) !important; font-size:0.68rem !important; letter-spacing:0.08em !important; text-transform:uppercase !important; }
[data-testid="metric-container"] [data-testid="metric-value"] { color:#e8f4ff !important; font-family:'Orbitron',monospace !important; }
hr { border-color:rgba(167,139,250,0.18) !important; margin:1.5rem 0 !important; }
.stImage img { border-radius:10px !important; border:1px solid rgba(167,139,250,0.3) !important; }
[data-testid="stFileUploaderDropzone"] { background:rgba(10,22,40,0.6) !important; border:1px dashed rgba(167,139,250,0.35) !important; border-radius:10px !important; }
::-webkit-scrollbar { width:5px; }
::-webkit-scrollbar-track { background:rgba(10,22,40,0.5); }
::-webkit-scrollbar-thumb { background:rgba(167,139,250,0.35); border-radius:3px; }
</style>
"""
st.markdown(COSMIC_CSS, unsafe_allow_html=True)
=======
=======
>>>>>>> caec3e7300fade99d6c3b5550bd54dd2ee3253c1
st.markdown("""
<style>
    .main-title { font-size: 2rem; font-weight: 700; color: #6366F1; margin-bottom: 0.25rem; }
    .subtitle { font-size: 1rem; color: #6b7280; margin-bottom: 2rem; }
    .pred-real { background: #dcfce7; color: #166534; padding: 0.5rem 1.5rem; border-radius: 999px; font-size: 1.2rem; font-weight: 700; }
    .pred-fake { background: #fee2e2; color: #991b1b; padding: 0.5rem 1.5rem; border-radius: 999px; font-size: 1.2rem; font-weight: 700; }
    .metric-card { background: #f9fafb; border-radius: 12px; padding: 1rem; text-align: center; border: 1px solid #e5e7eb; }
    .metric-value { font-size: 1.8rem; font-weight: 700; }
    .metric-label { font-size: 0.8rem; color: #6b7280; margin-top: 4px; }
    .section-header { font-size: 1.1rem; font-weight: 600; color: #374151; margin: 1.5rem 0 0.75rem; border-bottom: 2px solid #6366F1; padding-bottom: 4px; }
    .token-highlight { display: inline-block; padding: 2px 6px; border-radius: 4px; margin: 2px; font-size: 0.85rem; }
    .stAlert { border-radius: 8px; }
</style>
""", unsafe_allow_html=True)
<<<<<<< HEAD
>>>>>>> caec3e7300fade99d6c3b5550bd54dd2ee3253c1
=======
>>>>>>> caec3e7300fade99d6c3b5550bd54dd2ee3253c1


@st.cache_resource
def load_model_and_explainer():
    device = torch.device("cpu")
    tokenizer = AutoTokenizer.from_pretrained(CFG.model.text_encoder)
<<<<<<< HEAD
<<<<<<< HEAD
    model = FakeNewsDetector(use_text=True, use_image=False, use_social=True).to(device)
    checkpoint_path = CFG.app.model_checkpoint
    if os.path.exists(checkpoint_path):
        ckpt = torch.load(checkpoint_path, map_location=device, weights_only=False)
        model.load_state_dict(ckpt["model_state_dict"])
        st.sidebar.success(f"Checkpoint loaded — epoch {ckpt['epoch']}")
    else:
        st.sidebar.warning("No checkpoint found. Using untrained model.")
=======
=======
>>>>>>> caec3e7300fade99d6c3b5550bd54dd2ee3253c1

    model = FakeNewsDetector(use_text=True, use_image=False, use_social=True).to(device)

    checkpoint_path = CFG.app.model_checkpoint
    if os.path.exists(checkpoint_path):
        ckpt = torch.load(checkpoint_path, map_location=device)
        model.load_state_dict(ckpt["model_state_dict"])
        st.sidebar.success(f"Model loaded (epoch {ckpt['epoch']})")
    else:
        st.sidebar.warning("No trained checkpoint found. Using untrained model (random predictions).")

<<<<<<< HEAD
>>>>>>> caec3e7300fade99d6c3b5550bd54dd2ee3253c1
=======
>>>>>>> caec3e7300fade99d6c3b5550bd54dd2ee3253c1
    model.eval()
    explainer = UnifiedExplainer(model, tokenizer, device)
    return model, tokenizer, explainer, device


<<<<<<< HEAD
<<<<<<< HEAD
def tokenize_text(text, tokenizer):
    return tokenizer(text, max_length=CFG.data.max_text_length,
                     padding="max_length", truncation=True, return_tensors="pt")


def render_token_highlights(tokens, scores):
    html = "<div style='line-height:2.6;font-family:Exo 2,sans-serif;'>"
    for token, score in zip(tokens[:60], scores[:60]):
        if not token.strip():
            continue
        s = float(score)
        if s > 0.6:
            bg = f"rgba(248,113,113,{0.12+s*0.28})"; bd = f"rgba(248,113,113,{0.3+s*0.3})"; col = "#fca5a5"
        elif s > 0.3:
            bg = f"rgba(251,191,36,{0.08+s*0.18})"; bd = f"rgba(251,191,36,{0.2+s*0.28})"; col = "#fcd34d"
        else:
            bg = f"rgba(167,139,250,{0.04+s*0.1})"; bd = "rgba(167,139,250,0.1)"; col = "#c4b5fd"
        html += f'<span class="token-highlight" style="background:{bg};border:1px solid {bd};color:{col};">{token}</span> '
=======
=======
>>>>>>> caec3e7300fade99d6c3b5550bd54dd2ee3253c1
def tokenize_text(text: str, tokenizer):
    return tokenizer(
        text,
        max_length=CFG.data.max_text_length,
        padding="max_length",
        truncation=True,
        return_tensors="pt",
    )


def prepare_image(uploaded_file):
    img = Image.open(uploaded_file).convert("RGB")
    transform = get_image_transform(train=False)
    tensor = transform(img).unsqueeze(0)
    return tensor, np.array(img.resize((224, 224))) / 255.0


def render_token_highlights(tokens, scores):
    html = "<div style='line-height:2.2;'>"
    for token, score in zip(tokens[:50], scores[:50]):
        if not token.strip():
            continue
        intensity = float(score)
        r = int(255 * intensity)
        g = int(200 * (1 - intensity))
        b = 50
        color = f"rgba({r},{g},{b},0.3)"
        html += f'<span class="token-highlight" style="background:{color};">{token}</span> '
<<<<<<< HEAD
>>>>>>> caec3e7300fade99d6c3b5550bd54dd2ee3253c1
=======
>>>>>>> caec3e7300fade99d6c3b5550bd54dd2ee3253c1
    html += "</div>"
    return html


<<<<<<< HEAD
<<<<<<< HEAD
def cosmic_bar_chart(weights):
    palette = ["#a78bfa", "#34d399", "#fbbf24", "#7dd3fc"]
    labels, values = list(weights.keys()), list(weights.values())
    fig, ax = plt.subplots(figsize=(5.5, 2.8))
    fig.patch.set_facecolor("#030712"); ax.set_facecolor("#0a0f1e")
    bars = ax.barh(labels, values, color=palette[:len(labels)], height=0.4, edgecolor="none")
    for bar, val in zip(bars, values):
        ax.text(val+0.01, bar.get_y()+bar.get_height()/2, f"{val:.0%}", va="center", ha="left",
                fontsize=9.5, fontweight="bold", color="#e8f4ff", fontfamily="monospace")
    ax.set_xlim(0, 1.18); ax.set_xlabel("Attention Weight", color="#a78bfa", fontsize=8.5)
    ax.set_title("Cross-Modal Attention", color="#a78bfa", fontsize=9, fontfamily="monospace", pad=8)
    ax.tick_params(colors="#c4d4e8", labelsize=8.5)
    for sp in ax.spines.values(): sp.set_edgecolor((0.655, 0.545, 0.980, 0.15))
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    ax.grid(axis="x", color=(0.655, 0.545, 0.980, 0.07), linestyle="--", linewidth=0.5)
    plt.tight_layout(pad=1.1)
=======
=======
>>>>>>> caec3e7300fade99d6c3b5550bd54dd2ee3253c1
def render_modality_gauge(weights: dict):
    labels = list(weights.keys())
    values = list(weights.values())
    colors = ["#6366F1", "#22c55e", "#f59e0b"]

    fig, ax = plt.subplots(figsize=(5, 3))
    bars = ax.bar(labels, values, color=colors[:len(labels)], width=0.4, edgecolor="white", linewidth=2)
    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.01,
                f"{val:.0%}", ha="center", va="bottom", fontsize=12, fontweight="bold")
    ax.set_ylim(0, 1.15)
    ax.set_ylabel("Weight", fontsize=10)
    ax.set_title("Modality Contribution", fontsize=11)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(labelsize=10)
    plt.tight_layout()
<<<<<<< HEAD
>>>>>>> caec3e7300fade99d6c3b5550bd54dd2ee3253c1
=======
>>>>>>> caec3e7300fade99d6c3b5550bd54dd2ee3253c1
    return fig


def main():
    with st.sidebar:
<<<<<<< HEAD
<<<<<<< HEAD
        st.markdown(
            '<div style="font-family:Orbitron,monospace;font-size:1rem;font-weight:900;'
            'background:linear-gradient(135deg,#a78bfa,#34d399);'
            '-webkit-background-clip:text;-webkit-text-fill-color:transparent;'
            'margin-bottom:0.2rem;">COSMICTRUTH</div>'
            '<div style="font-size:0.6rem;color:rgba(167,139,250,0.4);'
            'letter-spacing:0.15em;margin-bottom:1.2rem;">MISSION CONTROL</div>',
            unsafe_allow_html=True)
        st.markdown("---")
        show_attention = st.toggle("Modality contribution", value=True)
        show_tokens = st.toggle("Token attribution heatmap", value=True)
        st.markdown("---")
        st.markdown("""<div style="font-size:0.75rem;color:#c4d4e8;line-height:2.0;">
<span style="color:#34d399;">●</span> Text · RoBERTa-base<br>
<span style="color:#a78bfa;">●</span> Social graph · GAT<br>
<span style="color:#7dd3fc;">●</span> XAI · Gradient attribution<br>
<span style="color:#fbbf24;">●</span> Fusion · Cross-modal attn</div>""", unsafe_allow_html=True)
        log_path = os.path.join(CFG.train.log_dir, "training_results.json")
        if os.path.exists(log_path):
            with open(log_path) as f:
                tlog = json.load(f)
            tm = tlog.get("test_metrics", {})
            st.markdown("---")
            acc = tm.get("accuracy", 0); f1 = tm.get("f1_macro", 0); auc = tm.get("auc_roc", 0)
            st.markdown(
                f'<div style="font-size:0.78rem;color:#c4d4e8;line-height:2.1;">'
                f'<span style="color:#34d399;font-family:Orbitron,monospace;">{acc:.2%}</span>'
                f'<span style="color:rgba(167,139,250,0.4);"> accuracy</span><br>'
                f'<span style="color:#a78bfa;font-family:Orbitron,monospace;">{f1:.2%}</span>'
                f'<span style="color:rgba(167,139,250,0.4);"> F1 macro</span><br>'
                f'<span style="color:#fbbf24;font-family:Orbitron,monospace;">{auc:.4f}</span>'
                f'<span style="color:rgba(167,139,250,0.4);"> AUC-ROC</span></div>',
                unsafe_allow_html=True)

    c1, c2 = st.columns([1, 11])
    with c1:
        st.markdown('<div class="planet-orb"></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="cosmic-title">COSMICTRUTH</div>', unsafe_allow_html=True)
        st.markdown('<div class="cosmic-subtitle">Multimodal Fake News Detection · Explainable AI · Deep Neural Analysis</div>', unsafe_allow_html=True)
    st.markdown('<div class="orbit-decoration"></div>', unsafe_allow_html=True)

    model, tokenizer, explainer, device = load_model_and_explainer()

    tab1, tab2, tab3 = st.tabs(["🛸  ANALYZE TRANSMISSION", "🔭  XAI OBSERVATORY", "🪐  MISSION ARCHIVE"])

    with tab1:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown('<div class="section-header">📡 Incoming Transmission</div>', unsafe_allow_html=True)
            SAMPLES = {
                "── Select signal ──": "",
                "SUSPICIOUS · Disinformation signal": (
                    "SHOCKING TRUTH REVEALED: Government scientists have secretly discovered "
                    "that common tap water contains mind-control chemicals added by the global "
                    "elite to keep citizens docile. Whistleblowers who tried to expose this were "
                    "silenced. Mainstream media is HIDING this from you! Share before deleted! "
                    "They don't want you to know the REAL truth. WAKE UP before it's too late!!!"),
                "CREDIBLE · Verified news signal": (
                    "The Federal Reserve announced on Wednesday a 25 basis point increase in "
                    "the federal funds rate, bringing it to a target range of 5.25 to 5.50 "
                    "percent. Federal Reserve Chair Jerome Powell said the decision was unanimous "
                    "among voting members of the Federal Open Market Committee. Officials cited "
                    "continued concerns about inflation remaining above the 2 percent target."),
            }
            selected = st.selectbox("Load example:", list(SAMPLES.keys()))
            text_input = st.text_area("Transmit article text:", value=SAMPLES[selected], height=220,
                                      placeholder="Paste news article text here for deep-space analysis...")
        with col2:
            st.markdown('<div class="section-header">🖼️ Visual Signal</div>', unsafe_allow_html=True)
            uploaded_image = st.file_uploader("Upload image (optional)", type=["jpg","jpeg","png"])
            if uploaded_image:
                st.image(uploaded_image, use_container_width=True)

        st.markdown("<br>", unsafe_allow_html=True)
        analyze_btn = st.button("🚀  LAUNCH DEEP ANALYSIS", type="primary", use_container_width=True)

        if analyze_btn and text_input.strip():
            with st.spinner("Scanning transmission through neural constellations..."):
                encoding = tokenize_text(text_input, tokenizer)
                batch = {
                    "input_ids": encoding["input_ids"],
                    "attention_mask": encoding["attention_mask"],
                    "graph_x": [torch.zeros(1, 16)],
                    "graph_edge_index": [torch.zeros(2, 0, dtype=torch.long)],
                    "graph_num_nodes": [1],
                }
                explanation = explainer.explain_prediction(batch, news_id="user_input")

            pred = explanation["prediction"]
            conf = explanation["confidence"]
            p_real = explanation["probabilities"]["Real"]
            p_fake = explanation["probabilities"]["Fake"]

            st.markdown("---")
            r1, r2, r3, r4 = st.columns(4)
            css_cls = "pred-fake" if pred == "Fake" else "pred-real"
            col_conf = "#f87171" if pred == "Fake" else "#34d399"
            r1.markdown(f'<div class="metric-card"><div class="metric-label">VERDICT</div><div class="metric-value" style="margin-top:6px;"><span class="{css_cls}">{pred.upper()}</span></div></div>', unsafe_allow_html=True)
            r2.markdown(f'<div class="metric-card"><div class="metric-label">CONFIDENCE</div><div class="metric-value" style="color:{col_conf};margin-top:6px;">{conf:.1%}</div><div class="conf-bar-outer"><div class="conf-bar-inner" style="width:{conf*100:.0f}%;"></div></div></div>', unsafe_allow_html=True)
            r3.markdown(f'<div class="metric-card"><div class="metric-label">P(REAL)</div><div class="metric-value" style="color:#34d399;margin-top:6px;">{p_real:.1%}</div></div>', unsafe_allow_html=True)
            r4.markdown(f'<div class="metric-card"><div class="metric-label">P(FAKE)</div><div class="metric-value" style="color:#f87171;margin-top:6px;">{p_fake:.1%}</div></div>', unsafe_allow_html=True)

            if pred == "Fake":
                st.error(f"🚨 **DISINFORMATION SIGNAL DETECTED** — Confidence: {conf:.1%}. Neural analysis indicates high-probability fake news signatures.")
            else:
                st.success(f"✅ **AUTHENTIC SIGNAL CONFIRMED** — Confidence: {conf:.1%}. This transmission appears factually grounded.")

            st.session_state["explanation"] = explanation
            st.info("Switch to **XAI Observatory** tab to explore the explanation.")
        elif analyze_btn:
            st.error("⚠️ No transmission detected. Please enter article text.")

    with tab2:
        if "explanation" not in st.session_state:
            st.markdown('<div style="text-align:center;padding:3rem 0;"><div style="font-family:Orbitron,monospace;font-size:1rem;color:rgba(167,139,250,0.35);letter-spacing:0.1em;">AWAITING TRANSMISSION</div><div style="font-size:0.8rem;color:rgba(167,139,250,0.25);margin-top:0.5rem;">Run an analysis in the Analyze tab first</div></div>', unsafe_allow_html=True)
        else:
            explanation = st.session_state["explanation"]
            pred = explanation["prediction"]
            conf = explanation["confidence"]
            color = "#f87171" if pred == "Fake" else "#34d399"
            st.markdown(f'<div style="display:flex;align-items:center;gap:1rem;background:linear-gradient(135deg,rgba(167,139,250,0.07),rgba(52,211,153,0.04));border:1px solid rgba(167,139,250,0.18);border-radius:14px;padding:0.9rem 1.4rem;margin-bottom:1.4rem;"><div style="font-family:Orbitron,monospace;font-size:0.65rem;color:rgba(167,139,250,0.45);letter-spacing:0.1em;">VERDICT</div><div style="font-family:Orbitron,monospace;font-size:1.2rem;font-weight:900;color:{color};">{pred.upper()}</div><div style="color:rgba(167,139,250,0.35);">·</div><div style="font-family:Orbitron,monospace;font-size:0.9rem;color:{color};opacity:0.75;">{conf:.1%}</div></div>', unsafe_allow_html=True)

            if show_tokens and "text" in explanation:
                st.markdown('<div class="section-header">📡 Token Attribution Field</div>', unsafe_allow_html=True)
                text_exp = explanation["text"]
                st.markdown(f'<div class="cosmos-card">{render_token_highlights(text_exp["tokens"], text_exp["scores"])}</div>', unsafe_allow_html=True)
                top = text_exp.get("top_tokens", [])[:5]
                if top:
                    st.markdown('<div class="section-header">⭐ Top Influential Tokens</div>', unsafe_allow_html=True)
                    tcols = st.columns(len(top))
                    for i, (token, score) in enumerate(top):
                        with tcols[i]:
                            st.markdown(f'<div class="top-token"><div class="rank">#{i+1}</div><div class="word">{token}</div><div class="score">{score:.3f}</div><div class="conf-bar-outer"><div class="conf-bar-inner" style="width:{int(score*100)}%;background:linear-gradient(90deg,#a78bfa,#f87171);"></div></div></div>', unsafe_allow_html=True)

            if show_attention and "fusion" in explanation:
                st.markdown('<div class="section-header">🌌 Modality Contribution Matrix</div>', unsafe_allow_html=True)
                fig = cosmic_bar_chart(explanation["fusion"]["modality_weights"])
                st.pyplot(fig, use_container_width=False)
                plt.close(fig)

            st.markdown('<div class="section-header">📋 Full Signal Report</div>', unsafe_allow_html=True)
            st.json({"verdict": explanation["prediction"], "confidence": f"{explanation['confidence']:.2%}", "probabilities": explanation["probabilities"], "top_tokens": [{"token": t, "score": round(s,4)} for t,s in explanation.get("text",{}).get("top_tokens",[])], "modality_weights": explanation.get("fusion",{}).get("modality_weights",{})})

    with tab3:
        st.markdown('<div class="section-header">🪐 Model Architecture</div>', unsafe_allow_html=True)
        ca, cb = st.columns(2)
        with ca:
            st.markdown("""<div class="cosmos-card">
<div style="font-family:Orbitron,monospace;font-size:0.72rem;color:#a78bfa;letter-spacing:0.1em;margin-bottom:0.7rem;">TEXT STREAM</div>
<div style="font-size:0.8rem;color:#c4d4e8;line-height:1.9;"><span style="color:#34d399;">▸</span> Backbone: RoBERTa-base (125M params)<br><span style="color:#34d399;">▸</span> Output: 768-dim CLS embedding<br><span style="color:#34d399;">▸</span> Fine-tuning: Last 2 transformer layers</div>
<div style="font-family:Orbitron,monospace;font-size:0.72rem;color:#7dd3fc;letter-spacing:0.1em;margin:1rem 0 0.7rem;">SOCIAL STREAM</div>
<div style="font-size:0.8rem;color:#c4d4e8;line-height:1.9;"><span style="color:#7dd3fc;">▸</span> Architecture: GAT (2 layers, 4 heads)<br><span style="color:#7dd3fc;">▸</span> Pooling: Mean + Max global pool<br><span style="color:#7dd3fc;">▸</span> Output: 512-dim graph embedding</div></div>""", unsafe_allow_html=True)
        with cb:
            st.markdown("""<div class="cosmos-card">
<div style="font-family:Orbitron,monospace;font-size:0.72rem;color:#fbbf24;letter-spacing:0.1em;margin-bottom:0.7rem;">FUSION MODULE</div>
<div style="font-size:0.8rem;color:#c4d4e8;line-height:1.9;"><span style="color:#fbbf24;">▸</span> Cross-modal attention (8 heads)<br><span style="color:#fbbf24;">▸</span> Modality gating (learned weights)<br><span style="color:#fbbf24;">▸</span> FFN + GELU + LayerNorm</div>
<div style="font-family:Orbitron,monospace;font-size:0.72rem;color:#f87171;letter-spacing:0.1em;margin:1rem 0 0.7rem;">XAI METHODS</div>
<div style="font-size:0.8rem;color:#c4d4e8;line-height:1.9;"><span style="color:#f87171;">▸</span> Gradient × Embedding attribution<br><span style="color:#f87171;">▸</span> Cross-modal attention weights<br><span style="color:#f87171;">▸</span> Per-modality contribution scores</div></div>""", unsafe_allow_html=True)
=======
=======
>>>>>>> caec3e7300fade99d6c3b5550bd54dd2ee3253c1
        st.markdown("## ⚙️ Settings")
        show_attention = st.toggle("Show cross-modal attention weights", value=True)
        show_gradcam = st.toggle("Show GradCAM heatmap", value=True)
        st.markdown("---")
        st.markdown("### About this project")
        st.markdown("""
        **Multimodal Fake News Detection with XAI**

        This system analyzes:
        - 📝 Article **text** via RoBERTa
        - 🖼️ News **images** via CLIP-ViT
        - 🌐 **Social propagation** via GNN

        Explanations generated using:
        - SHAP / Gradient attribution (text)
        - GradCAM (images)
        - Cross-modal attention (fusion)
        """)

    st.markdown('<div class="main-title">🔍 Fake News Detector</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Multimodal detection with Explainable AI — Text · Image · Social Graph</div>', unsafe_allow_html=True)

    model, tokenizer, explainer, device = load_model_and_explainer()

    tab1, tab2, tab3 = st.tabs(["🔎 Analyze News", "📊 Explanation Dashboard", "📈 Model Info"])

    with tab1:
        col1, col2 = st.columns([2, 1])

        with col1:
            st.markdown("### 📝 News Article Text")
            sample_texts = {
                "Select an example...": "",
                "Suspicious (Sensational headline)": "BREAKING: Scientists discover that common household chemical CURES cancer but Big Pharma is HIDING it from you! Share before this gets deleted! The mainstream media won't cover this shocking revelation that doctors don't want you to know. Thousands have already been cured using this simple method.",
                "Credible (Factual tone)": "The Federal Reserve announced a 25 basis point interest rate increase on Wednesday, citing continued concerns about inflation. The decision was unanimous among voting members of the Federal Open Market Committee. The rate now stands at 5.5%, the highest level in over two decades. Officials signaled they may pause further increases to assess economic conditions.",
            }
            selected = st.selectbox("Load example:", list(sample_texts.keys()))
            text_input = st.text_area(
                "Paste or type news article text:",
                value=sample_texts[selected],
                height=200,
                placeholder="Enter the full news article text here...",
            )

        with col2:
            st.markdown("### 🖼️ Article Image (optional)")
            uploaded_image = st.file_uploader(
                "Upload news image",
                type=["jpg", "jpeg", "png"],
                help="Upload the image associated with the news article",
            )
            if uploaded_image:
                st.image(uploaded_image, use_container_width=True)

        analyze_btn = st.button("🚀 Analyze Article", type="primary", use_container_width=True)

        if analyze_btn and text_input.strip():
            with st.spinner("Analyzing article and generating explanations..."):
                encoding = tokenize_text(text_input, tokenizer)
                import torch as _torch
                batch = {
                 "input_ids": encoding["input_ids"],
                 "attention_mask": encoding["attention_mask"],
                 "graph_x": [_torch.zeros(1, 16)],
                 "graph_edge_index": [_torch.zeros(2, 0, dtype=_torch.long)],
                 "graph_num_nodes": [1],
                }

                image_array = None
                if uploaded_image and model.use_image:
                    img_tensor, image_array = prepare_image(uploaded_image)
                    batch["image"] = img_tensor
                else:
                    batch["image"] = torch.zeros(1, 3, 224, 224)

                explanation = explainer.explain_prediction(batch, news_id="user_input")

            st.markdown("---")
            pred = explanation["prediction"]
            conf = explanation["confidence"]

            result_col1, result_col2, result_col3, result_col4 = st.columns(4)

            css_class = "pred-fake" if pred == "Fake" else "pred-real"
            result_col1.markdown(f'<div class="metric-card"><div class="metric-value"><span class="{css_class}">{pred}</span></div><div class="metric-label">Prediction</div></div>', unsafe_allow_html=True)
            result_col2.markdown(f'<div class="metric-card"><div class="metric-value" style="color:#6366F1">{conf:.1%}</div><div class="metric-label">Confidence</div></div>', unsafe_allow_html=True)
            result_col3.markdown(f'<div class="metric-card"><div class="metric-value" style="color:#22c55e">{explanation["probabilities"]["Real"]:.1%}</div><div class="metric-label">P(Real)</div></div>', unsafe_allow_html=True)
            result_col4.markdown(f'<div class="metric-card"><div class="metric-value" style="color:#ef4444">{explanation["probabilities"]["Fake"]:.1%}</div><div class="metric-label">P(Fake)</div></div>', unsafe_allow_html=True)

            incons = explanation.get("inconsistency_score", 0)
            if incons > 0.6:
                st.warning(f"⚠️ High text-image inconsistency detected: {incons:.2%} — the image may not match the article's claims.")
            elif incons > 0.3:
                st.info(f"ℹ️ Moderate text-image inconsistency: {incons:.2%}")

            st.session_state["explanation"] = explanation
            st.session_state["image_array"] = image_array
            st.success("Analysis complete! Switch to the **Explanation Dashboard** tab for full XAI details.")

        elif analyze_btn:
            st.error("Please enter some article text before analyzing.")

    with tab2:
        if "explanation" not in st.session_state:
            st.info("Run an analysis first in the **Analyze News** tab.")
        else:
            explanation = st.session_state["explanation"]
            image_array = st.session_state.get("image_array")

            st.markdown(f'<div class="section-header">📝 Text Attribution (What words triggered the decision?)</div>', unsafe_allow_html=True)
            if "text" in explanation:
                text_exp = explanation["text"]
                token_html = render_token_highlights(text_exp["tokens"], text_exp["scores"])
                st.markdown(token_html, unsafe_allow_html=True)

                st.markdown("**Top influential tokens:**")
                token_cols = st.columns(min(5, len(text_exp["top_tokens"])))
                for i, (token, score) in enumerate(text_exp["top_tokens"][:5]):
                    with token_cols[i]:
                        st.metric(f"#{i+1}", token, f"{score:.3f}")

            if show_attention and "fusion" in explanation:
                st.markdown('<div class="section-header">⚡ Modality Contribution (Which signal drove the prediction?)</div>', unsafe_allow_html=True)
                fig = render_modality_gauge(explanation["fusion"]["modality_weights"])
                st.pyplot(fig)
                plt.close(fig)

            if show_gradcam and "image" in explanation and explanation["image"]["gradcam_map"] is not None:
                st.markdown('<div class="section-header">🖼️ GradCAM Image Attribution (Where did the model look?)</div>', unsafe_allow_html=True)
                from xai.explainer import ImageExplainer
                img_exp = ImageExplainer(model, device)
                fig = img_exp.visualize(
                    explanation["image"],
                    original_image=image_array,
                    title="GradCAM Attribution",
                )
                st.pyplot(fig)
                plt.close(fig)

            st.markdown('<div class="section-header">📋 Full Explanation Report</div>', unsafe_allow_html=True)
            report_data = {
                "prediction": explanation["prediction"],
                "confidence": f"{explanation['confidence']:.2%}",
                "probabilities": explanation["probabilities"],
                "inconsistency_score": explanation.get("inconsistency_score", 0),
                "top_tokens": explanation.get("text", {}).get("top_tokens", []),
                "modality_weights": explanation.get("fusion", {}).get("modality_weights", {}),
            }
            st.json(report_data)

    with tab3:
        st.markdown("### Model Architecture Summary")
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("""
            **Text Stream**
            - Backbone: RoBERTa-base (125M params)
            - Output: 768-dim CLS embedding
            - Fine-tuning: Last 2 transformer layers

            **Image Stream**
            - Backbone: CLIP-ViT-Base/32
            - Output: 512-dim patch CLS embedding
            - Fine-tuning: Last 2 vision layers

            **Social Stream**
            - Architecture: GAT (2 layers, 4 heads)
            - Pooling: Mean + Max global pool
            - Output: 256-dim graph embedding
            """)
        with col_b:
            st.markdown("""
            **Fusion Module**
            - Cross-modal attention (8 heads)
            - Modality gating (learned weights)
            - FFN with GELU activation
            - Text-image inconsistency score

            **Classifier**
            - 2-layer MLP (512 → 256 → 2)
            - LayerNorm + Dropout (0.1)
            - Cross-entropy + inconsistency loss

            **XAI Methods**
            - Gradient attribution (text)
            - GradCAM via Captum (images)
            - Attention weights (fusion)
            """)
<<<<<<< HEAD
>>>>>>> caec3e7300fade99d6c3b5550bd54dd2ee3253c1
=======
>>>>>>> caec3e7300fade99d6c3b5550bd54dd2ee3253c1

        log_path = os.path.join(CFG.train.log_dir, "training_results.json")
        if os.path.exists(log_path):
            with open(log_path) as f:
                training_log = json.load(f)
            tm = training_log.get("test_metrics", {})
<<<<<<< HEAD
<<<<<<< HEAD
            st.markdown('<div class="section-header">📊 Mission Performance Log</div>', unsafe_allow_html=True)
            m1, m2, m3, m4 = st.columns(4)
            for col, (label, val, clr) in zip([m1,m2,m3,m4],[("Accuracy",tm.get("accuracy",0),"#34d399"),("F1 Macro",tm.get("f1_macro",0),"#a78bfa"),("F1 Fake",tm.get("f1_fake",0),"#f87171"),("AUC-ROC",tm.get("auc_roc",0),"#fbbf24")]):
                col.markdown(f'<div class="metric-card"><div class="metric-label">{label}</div><div class="metric-value" style="color:{clr};">{val:.4f}</div></div>', unsafe_allow_html=True)

            history = training_log.get("history", {})
            if history.get("train_loss"):
                st.markdown('<div class="section-header">📈 Training Trajectory</div>', unsafe_allow_html=True)
                epochs = list(range(1, len(history["train_loss"])+1))
                fig, axes = plt.subplots(1, 2, figsize=(11, 3.4))
                fig.patch.set_facecolor("#030712")
                for ax, (ty, vy, ylabel, title) in zip(axes, [(history["train_loss"],history["val_loss"],"Loss","Training Loss"),(history["train_f1"],history["val_f1"],"F1","F1 Score")]):
                    ax.set_facecolor("#0a0f1e")
                    ax.plot(epochs, ty, color="#a78bfa", lw=2.2, label="Train", marker="o", markersize=3.5)
                    ax.plot(epochs, vy, color="#34d399", lw=2.2, label="Val", marker="s", markersize=3.5, linestyle="--")
                    ax.fill_between(epochs, ty, alpha=0.08, color="#a78bfa")
                    ax.fill_between(epochs, vy, alpha=0.08, color="#34d399")
                    ax.set_xlabel("Epoch", color="#a78bfa", fontsize=8.5)
                    ax.set_ylabel(ylabel, color="#a78bfa", fontsize=8.5)
                    ax.set_title(title, color="#e8f4ff", fontsize=9, fontfamily="monospace")
                    ax.tick_params(colors="#c4d4e8", labelsize=8)
                    ax.legend(fontsize=8, labelcolor="#c4d4e8", facecolor="#0a0f1e", edgecolor=(0.655, 0.545, 0.980, 0.18))
                    for sp in ax.spines.values(): sp.set_edgecolor((0.655, 0.545, 0.980, 0.14))
                    ax.grid(color=(0.655, 0.545, 0.980, 0.06), linestyle='--', linewidth=0.5)
                plt.tight_layout(pad=1.4)
                st.pyplot(fig, use_container_width=True)
                plt.close(fig)
=======
=======
>>>>>>> caec3e7300fade99d6c3b5550bd54dd2ee3253c1
            st.markdown("### Test Set Performance")
            m1, m2, m3, m4 = st.columns(4)
            m1.metric("Accuracy", f"{tm.get('accuracy', 0):.4f}")
            m2.metric("F1 Macro", f"{tm.get('f1_macro', 0):.4f}")
            m3.metric("F1 Fake", f"{tm.get('f1_fake', 0):.4f}")
            m4.metric("AUC-ROC", f"{tm.get('auc_roc', 0):.4f}")
<<<<<<< HEAD
>>>>>>> caec3e7300fade99d6c3b5550bd54dd2ee3253c1
=======
>>>>>>> caec3e7300fade99d6c3b5550bd54dd2ee3253c1


if __name__ == "__main__":
    main()
<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> caec3e7300fade99d6c3b5550bd54dd2ee3253c1
=======
>>>>>>> caec3e7300fade99d6c3b5550bd54dd2ee3253c1

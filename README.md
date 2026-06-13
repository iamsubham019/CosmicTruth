# 🌌 CosmicTruth — Multimodal Fake News Detection with Explainable AI

CosmicTruth is a multimodal fake news detection system that combines **text analysis (RoBERTa)**, **social propagation analysis (Graph Attention Networks)**, and an architecturally-ready **image analysis stream (CLIP-ViT)**, fused through a **cross-modal attention mechanism**. Every prediction comes with a full **Explainable AI (XAI)** breakdown — highlighted influential words, modality contribution weights, and gradient attribution maps.

The system is deployed as an interactive Streamlit web application with a custom space-themed ("CosmicTruth") UI.

**🚀 Live Demo:** [cosmictruth.streamlit.app](https://cosmictruth.streamlit.app)

---

## Pretrained Model

The trained checkpoint (`best_model.pt`, ~631MB, epoch 9, **99.20% accuracy**, **0.9998 AUC-ROC**) is not included in this repo due to GitHub's 100MB file size limit.

**Download:** [best_model.pt](https://drive.google.com/file/d/1knRfSJa4UsFyCBtopIm7-CBTNtqGH6ID/view?usp=sharing)

After downloading, place the file at:
```
outputs/checkpoints/best_model.pt
```

---

## Key Results

| Metric | Score |
|---|---|
| Accuracy | 99.20% |
| F1 Macro | 99.19% |
| F1 (Fake) | 99.13% |
| AUC-ROC | 0.9998 |

Trained and evaluated on the [GonzaloA/fake_news](https://huggingface.co/datasets/GonzaloA/fake_news) dataset (40,583 articles, 70/15/15 train/val/test split).

### Ablation Study

| Configuration | Accuracy | F1 Macro |
|---|---|---|
| Text only | 0.9851 | 0.9849 |
| Text + Social (Full) | **0.9920** | **0.9919** |

---

## Architecture

```
Text Input  ──► RoBERTa-base ──► 512-dim
                                       ╲
                                        ► Cross-Modal Attention Fusion ──► MLP ──► Real / Fake
                                       ╱
Social Graph ──► GAT (2 layers, 4 heads) ──► 512-dim
```

| Component | Technology | Output |
|---|---|---|
| Text Encoder | RoBERTa-base (fine-tuned, last 2 layers) | 768-dim → 512-dim projected |
| Social Encoder | Graph Attention Network (2 layers, 4 heads) | 512-dim graph embedding |
| Image Encoder | CLIP-ViT-B/32 (architecturally ready, inactive) | 512-dim |
| Fusion Module | Cross-modal attention (8 heads) + modality gating | 512-dim fused vector |
| Classifier | 2-layer MLP | 2-class softmax (Real / Fake) |
| XAI Layer | Gradient × Embedding attribution + attention weights | Token scores + modality weights |

---

## Explainable AI

CosmicTruth provides two forms of explanation for every prediction:

1. **Token Attribution** — Gradient-times-input attribution highlights which words in the article most influenced the prediction, displayed as a color-coded heatmap (red = high importance, amber = medium, purple = low).
2. **Modality Contribution** — A bar chart showing how much the Text stream vs. the Social stream contributed to the final decision, derived from the fusion module's learned gating weights.

---

## Project Structure

```
fakenews_xai/
├── app.py                  # Streamlit web application (CosmicTruth UI)
├── train.py                 # Training script with label smoothing & early stopping
├── evaluate.py               # Detailed evaluation + XAI report generation
├── config.py                  # All hyperparameters and configuration
├── models/
│   ├── text_encoder.py        # RoBERTa-based text encoder
│   ├── image_encoder.py        # CLIP-ViT image encoder + GradCAM
│   ├── social_encoder.py        # GAT-based social graph encoder
│   ├── fusion.py                 # Cross-modal attention fusion module
│   ├── inconsistency_detector.py  # Cross-modal inconsistency scoring
│   └── detector.py                 # Main FakeNewsDetector model
├── data/
│   └── dataset.py                   # Dataset loading & preprocessing (GonzaloA/fake_news)
├── xai/
│   └── explainer.py                  # Unified XAI explainer
└── outputs/
    ├── checkpoints/                    # Trained model weights (download separately)
    ├── logs/                             # Training history & metrics
    └── evaluation/                        # Confusion matrix, training curves, XAI samples
```

---

## Setup

### 1. Create a virtual environment

```bash
python -m venv fakenews_env
fakenews_env\Scripts\activate     # Windows
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Download the pretrained checkpoint

Download `best_model.pt` from the link above and place it at `outputs/checkpoints/best_model.pt`.

### 4. Run the app

```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

---

## Training from Scratch

```bash
python train.py
```

This will:
- Load the GonzaloA/fake_news dataset from HuggingFace (40,583 articles)
- Train with label smoothing, weight decay, and early stopping
- Save the best checkpoint to `outputs/checkpoints/best_model.pt`
- Run a final test evaluation and ablation study
- Save results to `outputs/logs/training_results.json`

**Training configuration:**
- Batch size: 16
- Learning rate: 1e-5 (OneCycleLR scheduler)
- Label smoothing: 0.1
- Early stopping patience: 5
- Hardware used: NVIDIA RTX 4050 Laptop GPU (6GB VRAM)

---

## Evaluation

```bash
python evaluate.py
```

Generates:
- Confusion matrix
- Training/validation curves
- Ablation study comparison
- Per-sample XAI reports (text attribution, fusion weights)

---

## Tech Stack

- **PyTorch** 2.6.0 + CUDA 12.4
- **HuggingFace Transformers** (RoBERTa, CLIP)
- **PyTorch Geometric** (Graph Attention Networks)
- **Streamlit** (web application)
- **scikit-learn** (evaluation metrics)
- **Matplotlib** (visualizations)

---

## Citation

If you use this work, please cite:

```
@misc{cosmictruth2026,
  title={CosmicTruth: Multimodal Fake News Detection with Explainable AI},
  author={Subham Pal and Swastika Das},
  year={2026},
  note={B.Tech Final Year Project, Department of AI \& ML}
}
```

---

## License

This project is released for academic and research purposes.

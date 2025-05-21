# 🩺 Pet Insurance Cost Simulator

This is a Streamlit-based interactive calculator for comparing pet insurance plans over time. It's designed to help pet owners evaluate whether insurance is economically worthwhile based on personalized vet care projections.

## 🔍 Features
- Compare multiple insurance plans side-by-side
- Simulate cumulative costs over your pet's life
- Add one-time health events (accidents, surgeries, etc.)
- Estimate out-of-pocket costs with and without insurance
- Project vet cost and premium inflation

## 🚀 Live Demo
Deploy your own or visit:
> _[https://pet-insurance-calculator.streamlit.app/](https://pet-insurance-calculator.streamlit.app/)_ to launch the app from this repo.

## 📁 File Structure
```
├── app.py                # Main Streamlit app
├── insurance_math.py     # Insurance logic and cost models
├── plot_helpers.py       # Matplotlib chart functions
├── requirements.txt      # Python dependencies
├── README.md             # This file
└── LICENSE               # MIT License
```

## 📦 Installation (Local)
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 📄 License
Shield: [![CC BY-NC 4.0][cc-by-nc-shield]][cc-by-nc]

This work is licensed under a
[Creative Commons Attribution-NonCommercial 4.0 International License][cc-by-nc].

[![CC BY-NC 4.0][cc-by-nc-image]][cc-by-nc]

[cc-by-nc]: https://creativecommons.org/licenses/by-nc/4.0/
[cc-by-nc-image]: https://licensebuttons.net/l/by-nc/4.0/88x31.png
[cc-by-nc-shield]: https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg

---
Made with ❤️ to help people make smarter choices about their pets' healthcare.

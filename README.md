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
This project is licensed under the MIT License (see `LICENSE` file).

---
Made with ❤️ to help people make smarter choices about their pets' healthcare.

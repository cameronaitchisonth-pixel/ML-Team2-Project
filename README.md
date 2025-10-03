### Team 2
Cameron Aitchison, Richard Mendez, Brandon LeMay, Dipak Sakharkar

  
ML-Team2-Project/  
│  
├── data/                  #  
│   └── README.md          # Note: large data not stored here, see download instructions  
│  
├── notebooks/             # Exploration, EDA, prototyping  
│   └── 01_exploration.ipynb  
│  
├── src/                   # Core code  
│   ├── __init__.py        # Makes src a Python package  
│   ├── data_loading.py    # Functions to load/download/prepare data  
│   ├── preprocessing.py   # Feature engineering, scaling, cleaning  
│   ├── models.py          # Model classes or wrappers  
│   ├── train.py           # Training script (main entry point)  
│   └── evaluate.py        # Evaluation & metrics  
│  
├── tests/                 # Unit tests  
│   └── test_data_loading.py  
│  
├── experiments/           # Keep configs + logs here  
│   └── results/           # Save metrics, plots  
│  
├── requirements.txt       # Python dependencies  
├── .gitignore             # Ignore data, logs, outputs  
├── README.md              # Project overview, setup instructions  
└── LICENSE                # MIT license  

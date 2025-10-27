# ML Team 2 Project
Cameron Aitchison, Richard Mendez, Brandon LeMay, Dipak Sakharkar  
Machine Learning class project exploring market data.   
This repo contains all code, data handling, and reports for the project.

## Usage

Training can be accessed by running   
`python -m src.train`

---

## Repository Structure

- **data/**  
  - `README.md`
  - `SPX.csv` - Data file

- **notebooks/**  
  - `Data.ipynb` - Exploratory jupyter notebook for data analysis & prototyping

- **src/** (core code)  
  - `__init__.py` - Marks `src` as a Python package  
  - `data_loading.py` - Functions to load/download/prepare data  
  - `preprocessing.py` - Feature engineering, cleaning, scaling  
  - `models.py` - Model classes or wrappers  
  - `train.py` - Training script (main entry point)  
  - `evaluate.py` - Evaluation & metrics  

- **experiments/**  
  - `results/` — Saved metrics, plots, configs, and logs

- **requirements.txt** — Python dependencies
  - Use `conda create --name <NAME> --file requirements.txt` for conda env creation
  - Use `pip install -r ./requirements.txt` for pip 
- **.gitignore** — Ignore data, logs, outputs  
- **README.md** — Project overview, setup instructions  
- **LICENSE** — MIT license

---

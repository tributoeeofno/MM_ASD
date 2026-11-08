# Acoustic Anomaly Detection

A project for detecting anomalous sounds in acoustic data.

## Project structure

- `scripts/preprocessing.py` — dataset preparation entry point
- `scripts/train.py` — model training entry point
- `scripts/evaluate.py` — model evaluation entry point
- `configs/` — configuration files
- `metadata/` — dataset and experiment metadata
- `models/` — model artifacts (large generated files are ignored by Git)
- `results/` — evaluation outputs and reports (generated files are ignored by Git)

## Getting started

1. Create and activate a Python virtual environment.
2. Install dependencies with `python -m pip install -r requirements.txt` after adding the project's chosen packages.
3. Add configuration and dataset paths under `configs/` and `metadata/`.
4. Implement and run the scripts as the project pipeline is defined.

The scripts currently provide entry points only; preprocessing, training, and evaluation logic still needs to be implemented.

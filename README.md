# qantas_code_exercise
Code exercise interview for Machine Learning Data Engineer role

## CurrencyConverter
A python module that converts values in various currencies into AUD. This module will have two inputs, both formatted as CSV files.

## Getting Started (For Mac OS or Linux)

### Installation on virtual environment
1. Using terminal, navigate to *qantas-code-exercise* directory
2. Install virtualenv if not yet installed
3. Execute ``source qantas-venv/bin/activate``
4. Execute ``pip install -r requirements.txt``

---

### Execution
1. Update/copy input csv files to the *qantas-code-exercise/main-input* noting:
    * **input.csv** : first file per code exercise specification 
    * **currencyconversiondata.csv** : second file per code exercise specification
2. Using terminal, navigate to *qantas-code-exercise* directory
2. Execute ``python3 main.py``

---

### Running test cases using data in code exercise specification
1. Using terminal, navigate to *qantas-code-exercise/tests* directory
2. Execute ``pytest test.py``
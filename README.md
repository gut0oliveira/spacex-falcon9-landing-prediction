# SpaceX Falcon 9 Landing Prediction

Can public launch data help predict whether the first stage of a Falcon 9 rocket will land successfully?

This end-to-end data science project was developed as the capstone for the [IBM Data Science Professional Certificate](https://www.coursera.org/account/accomplishments/professional-cert/7EFVREK5NY5X). It combines API consumption, web scraping, data wrangling, SQL, exploratory analysis, geospatial visualization, an interactive dashboard, and machine learning.

## Business problem

SpaceX advertises Falcon 9 launches at a lower cost than many competitors, partly because the first stage can be recovered and reused. Predicting whether that stage will land successfully can support launch-cost estimation and competitive analysis.

## Project workflow

1. **Data collection** - SpaceX API requests and Wikipedia web scraping.
2. **Data wrangling** - cleaning, missing-value treatment, and landing-outcome labels.
3. **Exploratory analysis** - Pandas, Matplotlib, Seaborn, and SQL queries.
4. **Geospatial analysis** - Folium maps of launch sites and nearby infrastructure.
5. **Interactive dashboard** - Plotly Dash filters for launch site and payload range.
6. **Predictive modeling** - Logistic Regression, SVM, Decision Tree, and KNN with hyperparameter tuning.

## Main findings

- Logistic Regression was reported as the best-performing model, with test accuracy of `1.00` in the course experiment.
- SVM also reached `1.00`, while KNN reached approximately `0.986` during hyperparameter search.
- `KSC LC-39A` had the highest launch success ratio in the dashboard analysis.
- The `SO` orbit had the lowest observed success rate (`0%`) in the analyzed sample.
- Successful outcomes were more frequent than failed outcomes in the prepared dataset.

The perfect test accuracy should be interpreted in context: this is a small educational dataset and course-defined split. It documents the experiment faithfully, but it is not evidence that the model will generalize perfectly to future launches.

## Repository structure

```text
spacex-falcon9-landing-prediction/
├── dashboard/
│   ├── app.py
│   └── spacex_launch_dash.csv
├── docs/
│   └── capstone-presentation.pdf
├── notebooks/
│   ├── data_collection/
│   ├── data_wrangling/
│   ├── exploratory_analysis/
│   ├── machine_learning/
│   └── visual_analysis/
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Notebooks

| Stage | Content |
|---|---|
| [Data collection](notebooks/data_collection) | SpaceX API and Wikipedia scraping |
| [Data wrangling](notebooks/data_wrangling) | preparation and landing classification labels |
| [Exploratory analysis](notebooks/exploratory_analysis) | visual EDA and SQL analysis |
| [Visual analysis](notebooks/visual_analysis) | Folium launch-site maps |
| [Machine learning](notebooks/machine_learning) | model training, tuning, and comparison |

The complete project presentation is available in [docs/capstone-presentation.pdf](docs/capstone-presentation.pdf).

## How to run

Create and activate a virtual environment on Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Open the notebooks in VS Code or Jupyter and select the `.venv` kernel. The notebooks are retained as the original academic artifacts, so some cells rely on course-hosted resources or Jupyter-specific commands.

Run the interactive dashboard from the repository root:

```powershell
python dashboard/app.py
```

Then open `http://127.0.0.1:8050` in a browser.

## Technologies

Python · Pandas · NumPy · SQL · Beautiful Soup · Matplotlib · Seaborn · Folium · Plotly Dash · scikit-learn · Jupyter

## Academic attribution

This repository contains work completed for IBM Skills Network/Coursera course assignments, including starter instructions and educational material provided by IBM. My completed analyses, outputs, dashboard, conclusions, and final presentation are preserved here as a portfolio artifact.

## License

The repository uses the [MIT License](LICENSE) for original code and contributions. IBM course content, third-party data, and referenced materials remain subject to their respective licenses and terms.

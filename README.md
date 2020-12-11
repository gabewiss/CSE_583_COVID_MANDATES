# Covid Case Counts and Mandates
Project for CSE 583: COVID, Mandates, etc.
[![Build Status](https://travis-ci.com/gabewiss/covid.svg?branch=main)](https://travis-ci.com/gabewiss/covid)
[![Coverage Status](https://coveralls.io/repos/github/gabewiss/covid/badge.svg?branch=main)](https://coveralls.io/github/gabewiss/covid?branch=main)


### Introduction

This is a softeware that takes the latest Covid-19 case counts data updated by _New York Times_ and shows it with the Covid-19 related Mandates in the United States.
With this tool, we can see how effective a certain mandate is in terms of increased case counts.

Includes
1. A choropleth of USA to see the overview of monthly positive Covid-19 counts of each state.

2. Line graphs of states with markers of mandates.

### Team Members

* Zhaowen Guo
* Jee Hoon Han
* Oliver Li
* Gabriel Wisswaesser

### Example & Tutorials
* Choropleth of the United States

<img src="https://github.com/gabewiss/covid/blob/main/docs/example_figure/choropleth_example.png" width=70% height=70%>



* Line graphs of states with when certain mandates were implemented
<img src="https://github.com/gabewiss/covid/blob/main/docs/example_figure/linegraph_example.png" width=70% height=70%>


### Software dependencies and license information


### Installation
Instruction to run the softeware locally   

1. Clone the git repo: 'git clone https://github.com/gabewiss/covid.git'
2. Create the conda environment: 'conda env create -f environment.yml'
3.
4.

### Directory Summary
We have _docs_ directory, where related articles, component design, and use cases can be located.

Then, we have _covid_ directory, where data, examples, and test codes can be located

### Directory Structure
```
covid/
├── LICENSE
├── README.md
├── covid
│   ├── Untitled\ Folder
│   ├── __init__.py
│   ├── data
│   │   ├── README.txt
│   │   ├── cleaned_mandates.ipynb
│   │   ├── covid_count_state.csv
│   │   ├── covid_state.csv
│   │   ├── state_case.csv
│   │   ├── state_mandates.csv
│   │   ├── state_policy.csv
│   │   ├── state_policy_updates_20201202_0721.csv
│   │   └── states_population.csv
│   ├── environment.yml
│   ├── examples
│   │   ├── Plotly_practice.ipynb
│   │   ├── app.py
│   │   ├── covid_state.ipynb
│   │   ├── covid_visualization.ipynb
│   │   └── plotly_dash_practice_JH.ipynb
│   ├── src
│   │   ├── __init__.py
│   │   ├── count_processing.py
│   │   └── covid.py
│   └── tests
│       ├── __init__.py
│       ├── test_count.py
│       └── test_covid.py
├── data_check.py
├── docs
│   ├── CSE583_ComponentDiagram.pdf
│   ├── CSE583_UseCaseDiagram.pdf
│   ├── CSE583_technical_review.pdf
│   ├── SoftwareDesign.pdf
│   └── articles
│       ├── mandate_face_covering.pdf
│       └── mandate_social_distancing.pdf
├── environment.yml
├── setup.py
└── test_repo_check.py
```

### Data Source
#### Covid-19 Case Counts
  - Covid-19 data repository held by [New York Times](https://github.com/nytimes/covid-19-data)

#### Covid-19 State and County Policy
  - State and county orders held by [HealthData.gov](https://healthdata.gov/dataset/covid-19-state-and-county-policy-orders)

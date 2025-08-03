# Replication Package: 
## "Generating Inflation Expectations with Large Language Models"
### Zarifhonarvar (2025)

## Reproducibility Notice

### Random Seed Control
- **Claude models**: Do not currently support deterministic seed parameters. [Anthropic recommends](https://github.com/anthropics/claude-code/issues/3370) setting other hyperparameters to default values for optimal reproducibility.
- **OpenAI models**: Seed control is in beta phase for OpenAI models [Reference](https://platform.openai.com/docs/advanced-usage).
- **EDSL framework**: The Expected Parrot framework used for persona generation and survey administration does not implement random seed control for cross-model experiments.

Given these technical constraints, I have specified all available hyperparameters (temperature, top-p, max tokens) and provided comprehensive documentation in this repository to enable the best possible replication by future researchers using the same experimental framework.

### Model Documentation
Complete model cards and license documentation are included in the model cards and licenses.md. All experiments use synthetic personas and public economic information with no personally identifiable information (PII) shared with APIs.

## Data Availability
The complete dataset for this research is available through Harvard Dataverse at: [https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/UJUFIN](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/UJUFIN)

The Harvard Dataverse repository contains all raw data files including LLM responses, experiment logs, and analysis datasets. This data is publicly accessible for research purposes under a CC0 license. When using this data, please cite the original paper and the dataset.

## Repository Structure

### Experiment Code
- **information_treatment.py**: Persona-based experiment for short/long-run inflation expectations
- **fed_communication_test.py**: Tests communication clarity of Federal Reserve statements
- **robustness_checks.py**: Supplementary appendix robustness checks

### Data
For the full raw data, please access the Harvard Dataverse repository linked above.

### Analysis
- **clean_data.py**: Preprocessing of experimental data with comprehensive docstrings
- **main_analysis.py**: Main experimental analysis code with economist-friendly explanations
- **appendix_results.py**: Generates figures and tables for the appendix
- **plot_figures.py**: Standalone script to recreate all manuscript figures from exported CSV data

### Documentation
- **requirements.txt**: Pinned package versions for reproducibility
- **environment.yml**: Conda environment file for cross-platform compatibility
- **models/**: Model cards and license information for all LLMs used
- **tests/**: Basic pytest tests for persona creation and response parsing

## Installation and Setup

### System Requirements
This experiment runs remotely via the EDSL framework and Expected Parrot infrastructure:
- **Local requirements**: Python 3.8+, 4GB RAM minimum
- **Model access**: Experiments execute through cloud APIs (OpenAI, Anthropic) and third-party providers (DeepInfra, Together AI) via EDSL's remote cache
- **No local GPU required**: All model inference handled remotely
- **Expected Parrot API key**: Required for accessing the unified model endpoint

### Dependencies
Install required packages:
```bash
pip install -r requirements.txt

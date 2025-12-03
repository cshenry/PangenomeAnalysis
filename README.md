# PangenomeAnalysis

Jupyter notebooks and data for pangenome analyses performed using BERDL, PLM, SKANI, and other bioinformatics tools.

## Overview

This project contains analysis workflows for:
- **BERDL**: Bacterial Evolution and Redundancy Detection Library
- **PLM**: Protein Language Models for sequence analysis
- **SKANI**: Fast and accurate Average Nucleotide Identity (ANI) calculator for genomes
- Additional pangenome analysis tools and methods

## Setup

This project was created with the `create-new-project` Claude command.

### Prerequisites

- Python 3.11+
- Jupyter Notebook/Lab
- KBUtilLib and ModelSEEDpy (from local paths)

### Installation

1. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Development

Open the Cursor workspace:
```bash
code !PangenomeAnalysis.code-workspace
```

## Project Structure

```
PangenomeAnalysis/
├── notebooks/           # Jupyter notebooks for analyses
│   ├── util.py          # Shared utility functions
│   ├── data/            # Input data files
│   ├── datacache/       # Cached intermediate data
│   ├── genomes/         # Genome files (FASTA, GBK)
│   ├── models/          # Metabolic models
│   └── nboutput/        # Notebook outputs
├── agent-io/            # Claude agent I/O files
│   ├── prds/            # Product requirement documents
│   └── docs/            # Documentation
├── .claude/             # Claude Code configuration
└── requirements.txt     # Python dependencies
```

## Tools Reference

### SKANI
Fast ANI calculator for comparing genome similarity.
- Documentation: https://github.com/bluenote-1577/skani

### BERDL
Library for bacterial evolution and redundancy detection analysis.

### PLM
Protein Language Model embeddings for functional annotation and comparison.

## License

[Add license information]

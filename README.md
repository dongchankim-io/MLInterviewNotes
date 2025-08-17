# ML Technical Interview Notes

A comprehensive, modular LaTeX document containing technical interview preparation notes for Machine Learning positions. This project has been structured for easy maintenance, collaborative editing, and professional document management.

## Overview

This document covers essential ML concepts organized into logical sections:
- **Problem Framing & Core Principles** - MLE vs MAP, generative vs discriminative models, bias-variance tradeoff
- **Data & Features** - Feature engineering, channels in deep learning
- **Learning & Training Dynamics** - Batch normalization, optimization, regularization, activation functions
- **Evaluation, Calibration & Decisioning** - Loss functions, ROC curves, recommendation metrics
- **Architectures, Adaptation & Production** - Transformers, fine-tuning, recommendation systems

## Project Structure

```
mlinterviewnotes/
├── Makefile                    # Build and format commands
├── src/
│   ├── main.tex               # Main document file (includes all sections)
│   ├── header.tex             # Document preamble, packages, and title page
│   ├── footer.tex             # Document end
│   ├── sections/              # Individual section files
│   │   ├── problem-framing.tex     # Problem Framing & Core Principles
│   │   ├── data-features.tex       # Data & Features
│   │   ├── learning-training.tex   # Learning & Training Dynamics
│   │   ├── evaluation-calibration.tex # Evaluation, Calibration & Decisioning
│   │   └── architectures-production.tex # Architectures, Adaptation & Production
│   ├── README.md              # Detailed usage instructions
│   └── [images and assets]    # PNG, JPG files for figures
```

## Requirements

- **LaTeX Distribution**: TeX Live, MiKTeX, or MacTeX
- **Required Packages**: amsmath, amssymb, geometry, fancyhdr, graphicx, enumitem, hyperref, titlesec, color, float
- **Build Tool**: Make (standard on Unix-like systems, available on Windows via WSL or MinGW)

## Quick Start

```bash
# Clone the repository
git clone <repository-url>
cd mlinterviewnotes

# Build the document
make build

# Format all LaTeX files
make format

# Show all available commands
make help
```

## Benefits of Modular Structure

1. **Easier Maintenance**: Each section can be edited independently
2. **Better Version Control**: Changes to specific sections are easier to track
3. **Collaborative Editing**: Multiple people can work on different sections simultaneously
4. **Faster Development**: Compile and test individual sections if needed
5. **Reusability**: Sections can be reused in other documents

## How to Use

### Build the Document
```bash
# Build the complete document (generates versioned PDF)
make build

# This will:
# - Detect version from header.tex automatically
# - Compile the LaTeX document
# - Generate MLInterviewNotes_v{VERSION}.pdf
# - Clean up auxiliary files
```

### Format LaTeX Files
```bash
# Format all .tex files in the src/ directory
make format

# Format a specific file
make format-file FILE=src/sections/problem-framing.tex
```

### Maintenance Commands
```bash
# Clean up auxiliary LaTeX files
make clean

# Show all available commands
make help
```

### Edit Individual Sections
- Modify content in the appropriate `sections/*.tex` file
- The main document will automatically include all changes
- Use `make format` to maintain consistent formatting

### Add New Sections
1. Create a new `.tex` file in the `sections/` directory
2. Add the section content with proper LaTeX formatting
3. Include it in `main.tex` using `\input{sections/new-section-name}`
4. Run `make format` to format the new section

### Modify Document Settings
- Edit `header.tex` to change packages, document class, or title page
- Edit `footer.tex` for any end-of-document modifications
- Update version in `header.tex` (the `\docversion` command)

## Version Management

The document version is automatically detected from `header.tex`:
```latex
\newcommand{\docversion}{v0.3}
```

When you update the version:
1. Change the version number in `header.tex`
2. Run `make build`
3. The PDF will be automatically named `MLInterviewNotes_v{VERSION}.pdf`

## Contributing

1. **Fork the repository**
2. **Create a feature branch** for your changes
3. **Edit the appropriate section file** in `src/sections/`
4. **Format your changes** with `make format`
5. **Test the build** with `make build`
6. **Submit a pull request**

## Notes

- All images and assets remain in the `src/` directory
- The document structure and formatting are preserved
- Each section file contains complete section content with proper LaTeX commands
- The main document maintains the same output as the original single file
- Use `make help` to see all available commands
# Updated at Sun Aug 17 13:47:43 PDT 2025

# ML Technical Interview Notes

This repository contains comprehensive notes for ML technical interviews, written in LaTeX.

## LaTeX Auto Formatting

This project uses `latexindent` for automatic LaTeX code formatting. The setup includes:

### Files Created
- `latexindent.yaml` - Global configuration file
- `src/.latexindent.yaml` - Project-specific configuration
- `format-latex.sh` - Formatting script
- `.vscode/settings.json` - VS Code integration

### Usage

#### Command Line
```bash
# Format all .tex files in src/ directory
./format-latex.sh

# Format a specific file
./format-latex.sh src/main.tex
```

#### VS Code Integration
- LaTeX files will be automatically formatted on save
- Use `Shift+Alt+F` to format manually
- The formatter is configured to use `latexindent` with project-specific settings

### Configuration
The formatter is configured with:
- 100-character line width for project files
- Proper indentation for environments and commands
- Preservation of mathematical expressions
- Automatic trailing whitespace removal

### Requirements
- `latexindent` (already installed on your system)
- VS Code with LaTeX extension (for editor integration)

## Document Structure

The main document (`src/main.tex`) covers:
- Model Training Fundamentals
- Optimization Algorithms  
- Regularization Techniques
- Loss Functions and Evaluation
- Model Architectures
- Fine-Tuning Techniques
- Fundamental ML Concepts
- Recommender Systems

## Building the Document

```bash
cd src
pdflatex main.tex
```

The compiled PDF will be available as `src/main.pdf`.
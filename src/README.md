# ML Technical Interview Notes - LaTeX Structure

This document has been split into modular files for easier maintenance and verification.

## File Structure

```
mlinterviewnotes/
├── Makefile                    # Build and format commands
├── src/
│   ├── main.tex               # Main document file (includes all sections)
│   ├── header.tex             # Document preamble, packages, and title page
│   ├── footer.tex             # Document end
│   └── sections/              # Individual section files
│       ├── problem-framing.tex     # Problem Framing & Core Principles
│       ├── data-features.tex       # Data & Features
│       ├── learning-training.tex   # Learning & Training Dynamics
│       ├── evaluation-calibration.tex # Evaluation, Calibration & Decisioning
│       └── architectures-production.tex # Architectures, Adaptation & Production
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

## Notes

- All images and assets remain in the `src/` directory
- The document structure and formatting are preserved
- Each section file contains complete section content with proper LaTeX commands
- The main document maintains the same output as the original single file
- Use `make help` to see all available commands

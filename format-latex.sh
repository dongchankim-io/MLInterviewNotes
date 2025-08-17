#!/bin/bash

# LaTeX formatting script using latexindent
# Usage: ./format-latex.sh [file.tex]

# Default to formatting all .tex files in src/ directory
if [ $# -eq 0 ]; then
    echo "Formatting all .tex files in src/ directory..."
    find src/ -name "*.tex" -exec latexindent --overwrite --silent {} \;
    echo "Formatting complete!"
else
    # Format specific file
    if [ -f "$1" ]; then
        echo "Formatting $1..."
        latexindent --overwrite --silent "$1"
        echo "Formatting complete!"
    else
        echo "Error: File $1 not found"
        exit 1
    fi
fi 
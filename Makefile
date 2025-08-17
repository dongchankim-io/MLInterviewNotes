# Makefile for ML Technical Interview Notes
# Usage: make <target>

.PHONY: help build format format-all format-file clean release

# Default target
help:
	@echo "Available targets:"
	@echo "  build        - Build the PDF document"
	@echo "  format       - Format all .tex files"
	@echo "  format-file  - Format a specific file (FILE=filename.tex)"
	@echo "  clean        - Remove auxiliary files and PDFs"
	@echo "  release      - Commit changes, tag release, and include PDF"

# Build the document
build:
	@echo "Building ML Technical Interview Notes..."
	@echo "Version detected: $(shell grep '\\newcommand{\\docversion}' src/header.tex | sed 's/.*\\newcommand{\\docversion}{\([^}]*\)}.*/\1/')"
	@echo "Output file: MLInterviewNotes_$(shell grep '\\newcommand{\\docversion}' src/header.tex | sed 's/.*\\newcommand{\\docversion}{\([^}]*\)}.*/\1/').pdf"
	@cd src && pdflatex -interaction=nonstopmode main.tex
	@cd src && pdflatex -interaction=nonstopmode main.tex
	@if [ -f "src/main.pdf" ]; then \
		mv src/main.pdf "../MLInterviewNotes_$(shell grep '\\newcommand{\\docversion}' src/header.tex | sed 's/.*\\newcommand{\\docversion}{\([^}]*\)}.*/\1/').pdf"; \
		echo "PDF generated successfully: MLInterviewNotes_$(shell grep '\\newcommand{\\docversion}' src/header.tex | sed 's/.*\\newcommand{\\docversion}{\([^}]*\)}.*/\1/').pdf"; \
	else \
		echo "Error: main.pdf was not generated"; \
		exit 1; \
	fi
	@echo "Cleaning up auxiliary files..."
	@rm -f src/*.aux src/*.log src/*.out src/*.toc src/*.fdb_latexmk src/*.fls src/*.synctex.gz
	@echo "Build complete! Output: MLInterviewNotes_$(shell grep '\\newcommand{\\docversion}' src/header.tex | sed 's/.*\\newcommand{\\docversion}{\([^}]*\)}.*/\1/').pdf"

# Format all .tex files
format: format-all

format-all:
	@echo "Formatting all .tex files in src/ directory..."
	@find src/ -name "*.tex" -exec latexindent --overwrite --silent {} \;
	@echo "Formatting complete!"

# Format a specific file
format-file:
	@if [ -z "$(FILE)" ]; then \
		echo "Error: Please specify a file with FILE=filename.tex"; \
		echo "Example: make format-file FILE=src/main.tex"; \
		exit 1; \
	fi
	@if [ -f "$(FILE)" ]; then \
		echo "Formatting $(FILE)..."; \
		latexindent --overwrite --silent "$(FILE)"; \
		echo "Formatting complete!"; \
	else \
		echo "Error: File $(FILE) not found"; \
		exit 1; \
	fi

# Clean auxiliary files and PDFs
clean:
	@echo "Cleaning up auxiliary files and PDFs..."
	@rm -f src/*.aux src/*.log src/*.out src/*.toc src/*.fdb_latexmk src/*.fls src/*.synctex.gz
	@rm -f MLInterviewNotes_*.pdf
	@echo "Cleanup complete!"

# Release target: commit, tag, and include PDF
release:
	@echo "Preparing release..."
	@echo "Version: $(shell grep '\\newcommand{\\docversion}' src/header.tex | sed 's/.*\\newcommand{\\docversion}{\([^}]*\)}.*/\1/')"
	@echo "Building PDF..."
	@$(MAKE) build
	@echo "Checking git status..."
	@if [ -n "$$(git status --porcelain)" ]; then \
		echo "Committing changes..."; \
		git add .; \
		git commit -m "Release $(shell grep '\\newcommand{\\docversion}' src/header.tex | sed 's/.*\\newcommand{\\docversion}{\([^}]*\)}.*/\1/') - ML Technical Interview Notes"; \
	else \
		echo "No changes to commit, using latest commit"; \
	fi
	@echo "Creating git tag..."
	@if git tag -l "$(shell grep '\\newcommand{\\docversion}' src/header.tex | sed 's/.*\\newcommand{\\docversion}{\([^}]*\)}.*/\1/')" > /dev/null 2>&1; then \
		echo "Tag already exists, updating it..."; \
		git tag -d "$(shell grep '\\newcommand{\\docversion}' src/header.tex | sed 's/.*\\newcommand{\\docversion}{\([^}]*\)}.*/\1/')" 2>/dev/null || true; \
	fi
	@git tag -a "$(shell grep '\\newcommand{\\docversion}' src/header.tex | sed 's/.*\\newcommand{\\docversion}{\([^}]*\)}.*/\1/')" -m "Release $(shell grep '\\newcommand{\\docversion}' src/header.tex | sed 's/.*\\newcommand{\\docversion}{\([^}]*\)}.*/\1/')"
	@echo "Pushing commits to remote..."
	@git push
	@echo "Pushing tags to remote..."
	@git push --tags --force
	@echo "Creating GitHub release with PDF..."
	@echo "Note: You may need to manually create the release on GitHub to include the PDF file."
	@echo "1. Go to: https://github.com/dongchankim-io/MLInterviewNotes/releases"
	@echo "2. Click 'Create a new release'"
	@echo "3. Select tag: $(shell grep '\\newcommand{\\docversion}' src/header.tex | sed 's/.*\\newcommand{\\docversion}{\([^}]*\)}.*/\1/')"
	@echo "4. Upload PDF: MLInterviewNotes_$(shell grep '\\newcommand{\\docversion}' src/header.tex | sed 's/.*\\newcommand{\\docversion}{\([^}]*\)}.*/\1/').pdf"
	@echo "5. Add release notes and publish"
	@echo ""
	@echo "Release $(shell grep '\\newcommand{\\docversion}' src/header.tex | sed 's/.*\\newcommand{\\docversion}{\([^}]*\)}.*/\1/') prepared successfully!"
	@echo "PDF: MLInterviewNotes_$(shell grep '\\newcommand{\\docversion}' src/header.tex | sed 's/.*\\newcommand{\\docversion}{\([^}]*\)}.*/\1/').pdf"
	@echo "Tag and commit are now live on the remote repository!"

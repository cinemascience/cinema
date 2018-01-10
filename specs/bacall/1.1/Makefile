DOCUMENT = spec
LATEX    = latex
BIBTEX   = bibtex
TOPDF    = dvipdf
VERSION  = 1.0
TYPE     = Composite
NAME     = B
DOC_OUTPUT_NAME = CinemaFileSpecification-$(NAME)_v$(VERSION)


all:
	$(LATEX) $(DOCUMENT).tex
	$(BIBTEX) $(DOCUMENT)
	$(LATEX) $(DOCUMENT).tex
	$(LATEX) $(DOCUMENT).tex
	$(TOPDF) $(DOCUMENT).dvi $(DOC_OUTPUT_NAME).pdf
	rm -f *.aux *.dvi *.log *.bbl *.blg *.toc
	"/System/Library/Automator/Combine PDF Pages.action/Contents/Resources/join.py" -o new.pdf coverpage/coverpage.pdf $(DOC_OUTPUT_NAME).pdf
	mv new.pdf $(DOC_OUTPUT_NAME).pdf

clean:
	rm -f *.aux *.dvi *.log *.pdf *.bbl *.blg *.toc *.swp

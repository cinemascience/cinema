DOCUMENT = spec
LATEX    = pdflatex
BIBTEX   = bibtex
SPEC_VERSION  = 1.0
SPEC_NAME     = chaplin
DOC_OUTPUT_NAME = CinemaFileSpecification-$(SPEC_NAME)_v$(SPEC_VERSION)


all:
	$(LATEX) $(DOCUMENT).tex
	$(BIBTEX) $(DOCUMENT)
	$(LATEX) $(DOCUMENT).tex
	$(LATEX) $(DOCUMENT).tex
	rm -f *.aux *.dvi *.log *.bbl *.blg *.toc
	mv $(DOCUMENT).pdf $(DOC_OUTPUT_NAME).pdf

clean:
	rm -f *.aux *.dvi *.log *.pdf *.bbl *.blg *.toc *.swp

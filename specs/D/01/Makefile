DOCUMENT = specD
LATEX    = pdflatex
BIBTEX   = bibtex
SRC      = *.tex tex/* # figures/*
BIBS     = bib/*.bib
VERSION  = 011
REPORT   = cinema_$(DOCUMENT)_v$(VERSION)

all: $(REPORT).pdf

$(REPORT).pdf: $(SRC) $(BIBS) $(IMAGES)
	$(LATEX) $(DOCUMENT).tex
	$(BIBTEX) $(DOCUMENT)
	$(LATEX) $(DOCUMENT).tex
	$(LATEX) $(DOCUMENT).tex
	mv $(DOCUMENT).pdf $(REPORT).pdf
	rm -f *.aux *.bbl *.blg *.dvi *.log *.toc *.swp *.out

clean:
	rm -f *.aux *.bbl *.blg *.dvi *.log *.toc *.swp *.out $(REPORT).pdf

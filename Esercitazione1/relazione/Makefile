################################
#
#     Makefile Lab3
#    
################################

#file di output

output = *.log Relazione1.aux Relazione1.pdf

# phony targets
.PHONY: cleanout, pdf, view

cleanout :
	rm -f $(output)

view:
	evince Relazione1.pdf

pdf: Relazione1.tex cleanout
	pdflatex -synctex=1 -interaction nonstopmode Relazione1.tex

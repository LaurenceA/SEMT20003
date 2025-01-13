#%.pdf: %.tex
#	pdflatex $<
#
all: heaviside.pdf sigmoid.pdf non_diff_loss.pdf clust_example.pdf

%.pdf: %.py
	python $< $@

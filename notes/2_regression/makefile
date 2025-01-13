#%.pdf: %.tex
#	pdflatex $<
#
all: abs.pdf const_obj.pdf const_opt.pdf families.pdf good_bad.pdf guess.pdf scatter.pdf x2.pdf quad_fam.pdf multivariate.pdf quad.pdf

%.pdf: %.py
	python $< $@

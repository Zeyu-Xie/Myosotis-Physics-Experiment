#!/bin/bash
xelatex -output-directory=. ./report.tex
bibtex ./report.aux
xelatex -output-directory=. ./report.tex
xelatex -output-directory=. ./report.tex

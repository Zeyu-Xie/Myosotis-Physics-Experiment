#!/bin/bash
cd note
xelatex -output-directory=. ./main.tex
bibtex ./main.aux
xelatex -output-directory=. ./main.tex
xelatex -output-directory=. ./main.tex

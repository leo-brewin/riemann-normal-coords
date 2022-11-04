#-------------------------------------------------------------------------------
SHELL = /bin/bash
#-------------------------------------------------------------------------------
.PHONY: all shared clean veryclean
#-------------------------------------------------------------------------------
TARGETS = \
		dGamma dRabcd\
		metric metric-inv\
		connection genGamma\
		geodesic-bvp geodesic-ivp geodesic-lsq\
		rnc2rnc gen2rnc rnc2gen\
		detg2
#-------------------------------------------------------------------------------
all:
	@ make shared
	@ for file in $(TARGETS); do make .$${file}; done;
	@ make summary
	@ make veryclean
#-------------------------------------------------------------------------------
%:
	@ make .$*
.%:	%.tex output/%.json expected/%.json
	@ echo "> cdblatex.sh $* ..."
	@ cdblatex.sh -skx -i $* &> $*.cdblog
	@ pdflatex -halt-on-error -interaction=batchmode $* &> /dev/null
	@ touch .redo-summary
	@ touch .$*
#-------------------------------------------------------------------------------
shared:
	@ cadabra2python hide/shared.cdb shared.py
#-------------------------------------------------------------------------------
summary:
	@ make .summary
.summary: .redo-summary
	@ echo "> pdflatex summary ..."
	@ pdflatex -halt-on-error -interaction=batchmode summary &> /dev/null
	@ touch .summary
#-------------------------------------------------------------------------------
rm-dot:
	@ for file in $(TARGETS) summary; \
	  do \
	     rm -rf .$${file}; \
	  done
	@ rm -rf .[a-z]*.lb
	@ rm -rf .summary .redo-summary
#-------------------------------------------------------------------------------
rm-output:
	@ rm -rf output/*
#-------------------------------------------------------------------------------
rm-expected:
	@ rm -rf expected/*
#-------------------------------------------------------------------------------
clean:
	@ for file in $(TARGETS) summary; \
	  do \
	     rm -rf $${file}.aux $${file}.log $${file}.out $${file}.synctex.gz; \
	  done
#-------------------------------------------------------------------------------
veryclean:
	@ make clean
	@ for file in $(TARGETS) summary; \
	  do \
	     rm -f $${file}.cdb; \
		  rm -f $${file}_.cdb $${file}_.txt; \
		  rm -f $${file}.cdbtex $${file}.cdbidx $${file}.cdbtxt $${file}.cdblog; \
		  rm -f $${file}.py; \
	  done
#-------------------------------------------------------------------------------
pristine:
	@ make rm-dot
	@ make rm-output
	@ make rm-expected
	@ make veryclean
	@ rm -rf shared.py
	@ rm -rf __pycache__
	@ for file in $(TARGETS) summary; \
	  do \
	     rm -rf $${file}.pdf; \
		  rm -rf $${file}.json $${file}*.c; \
		  rm -rf $${file}.cdbtex $${file}*.cdbcopy; \
	  done
#-------------------------------------------------------------------------------
github-clean:
	@ make rm-dot
	@ make rm-output
	@ make veryclean
	@ rm -rf shared.py
	@ rm -rf __pycache__
	@ for file in $(TARGETS) summary; \
	  do \
	     rm -rf $${file}.pdf; \
		  rm -rf $${file}.json $${file}*.c; \
		  rm -rf $${file}.cdbtex $${file}*.cdbcopy; \
	  done
#-------------------------------------------------------------------------------
github:
	@ make pristine
	@ make all
	@ make expected
	@ make github-clean

#-------------------------------------------------------------------------------
SHELL = /bin/bash
#-------------------------------------------------------------------------------
.PHONY: all tests
#-------------------------------------------------------------------------------
TARGETS = \
		dGamma dRabcd\
		metric metric-inv\
		connection genGamma\
		geodesic-bvp geodesic-ivp\
		rnc2rnc gen2rnc rnc2gen\
		geodesic-lsq geodesic-lsq-midpt\
		detg2\
		export
#-------------------------------------------------------------------------------
all:
	@ mkdir -p cdb pdf lib tests/output tests/expected tests/semantic/output tests/semantic/expected
	@ for file in $(TARGETS); do make .$${file}; done;
	@ # make sqrt-detg # requires pylatex.sh and friends from https://github.com/leo-brewin/hybrid-latex
	@ make summary
	@ make collection
#-------------------------------------------------------------------------------
.dGamma: dGamma.tex dGamma.sty config.sty
	@ make dGamma
.dRabcd: dRabcd.tex dRabcd.sty config.sty .dGamma
	@ make dRabcd
.metric: metric.tex metric.sty config.sty .dGamma .dRabcd
	@ make metric
.metric-inv: metric-inv.tex metric-inv.sty config.sty .dGamma .dRabcd
	@ make metric-inv
.connection: connection.tex connection.sty config.sty .metric .metric-inv
	@ make connection
.genGamma: genGamma.tex genGamma.sty config.sty .connection
	@ make genGamma
.geodesic-bvp: geodesic-bvp.tex geodesic-bvp.sty config.sty .genGamma
	@ make geodesic-bvp
.geodesic-ivp: geodesic-ivp.tex geodesic-ivp.sty config.sty .genGamma
	@ make geodesic-ivp
.geodesic-lsq: geodesic-lsq.tex geodesic-lsq.sty config.sty .metric .geodesic-bvp .rnc2rnc
	@ make geodesic-lsq
.geodesic-lsq-midpt: geodesic-lsq-midpt.tex geodesic-lsq-midpt.sty config.sty .metric .geodesic-lsq
	@ make geodesic-lsq-midpt
.rnc2rnc: rnc2rnc.tex rnc2rnc.sty config.sty .geodesic-bvp
	@ make rnc2rnc
.gen2rnc: gen2rnc.tex gen2rnc.sty config.sty
	@ make gen2rnc
.rnc2gen: rnc2gen.tex rnc2gen.sty config.sty
	@ make rnc2gen
.detg2: detg2.tex config.sty .metric
	@ make detg2
.export: dRabcd.export detg2.export gen2rnc.export genGamma.export geodesic-bvp.export geodesic-ivp.export geodesic-lsq.export metric-inv.export metric.export
	@ make export
#-------------------------------------------------------------------------------
sqrt-detg:
	@ make .sqrt-detg
.sqrt-detg: sqrt-detg.tex config.sty
	@ echo "pylatex.sh sqrt-detg ..."
	@ pylatex.sh -sx -i sqrt-detg &> sqrt-detg.pylog
	@ pdflatex -halt-on-error -interaction=batchmode sqrt-detg &> /dev/null
	@ cp -f sqrt-detg.pdf pdf/.
	@ touch .sqrt-detg
#-------------------------------------------------------------------------------
summary:
	@ make .summary
.summary: summary.tex summary.sty .redo-summary
	@ echo "pdflatex summary ..."
	@ pdflatex -halt-on-error -interaction=batchmode summary &> /dev/null
	@ cp -f summary.pdf pdf/.
	@ touch .summary
.redo-summary:
	@ touch .redo-summary
#-------------------------------------------------------------------------------
collection:
	@ make .collection
.collection: collection.tex collection.sty .redo-collection
	@ echo "pdflatex collection ..."
	@ pdflatex -halt-on-error -interaction=batchmode collection &> /dev/null
	@ cp -f collection.pdf pdf/.
	@ touch .collection
.redo-collection:
	@ touch .redo-collection
#-------------------------------------------------------------------------------
%:
	@ echo "cdblatex.sh $@ ..."
	@ cdblatex.sh -T -sx -i $@ &> $@.cdblog
	@ echo " -->"`cdbstats -i $@.cdblog`
	@ pdflatex -halt-on-error -interaction=batchmode $@ &> /dev/null
	@ pdflatex -halt-on-error -interaction=batchmode $@ &> /dev/null
	@ cp -f $@.pdf    pdf/.
	@ cp -f $@.cdb    cdb/.
	@ cp -f $@.cdbtex tests/output/.
	@ if [[ -e $@.json ]]; then cp -f $@.json tests/output/.; fi
	@ touch .redo-summary
	@ touch .redo-collection
	@ touch .$@
#-------------------------------------------------------------------------------
expected:
	@ cp -f tests/output/* tests/expected/.
	@ cp -f tests/semantic/output/* tests/semantic/expected/.
#-------------------------------------------------------------------------------
tests:
	@ tests.sh
#-------------------------------------------------------------------------------
rm-dot:
	@ for file in $(TARGETS) summary collection sqrt-detg; \
	  do \
	     rm -rf .$${file}; \
	  done
	@ rm -rf .[a-z]*.lb
	@ rm -rf .merged.tex .tmp.txt
	@ rm -rf .summary .redo-summary
	@ rm -rf .collection .redo-collection
#-------------------------------------------------------------------------------
rm-tests-output:
	@ rm -rf tests/output/*
	@ rm -rf tests/semantic/output/*
#-------------------------------------------------------------------------------
rm-output:
	@ rm -rf cdb/*
	@ rm -rf pdf/*
	@ rm -rf tests/output/*
	@ rm -rf tests/semantic/output/*
#-------------------------------------------------------------------------------
rm-expected:
	@ rm -rf tests/expected/*
	@ rm -rf tests/semantic/expected/*
#-------------------------------------------------------------------------------
clean:
	@ for file in $(TARGETS) summary collection sqrt-detg; \
	  do \
	     rm -rf $${file}.aux $${file}.log $${file}.out $${file}.synctex.gz; \
	  done
#-------------------------------------------------------------------------------
veryclean:
	@ make clean
	@ for file in $(TARGETS); \
	  do \
		  rm -rf $${file}.pdf; \
	     rm -rf $${file}.cdb $${file}_.cdb; \
		  rm -rf $${file}.cdbidx $${file}.cdbtxt $${file}.cdblog; \
		  rm -rf $${file}.py $${file}.pylog; \
	  done
#-------------------------------------------------------------------------------
pristine:
	@ make rm-dot
	@ make rm-output
	@ make rm-expected
	@ make veryclean
	@ (cd tests/semantic; make pristine)
	@ for file in $(TARGETS) summary collection sqrt-detg; \
	  do \
	     rm -rf $${file}.pdf; \
		  rm -rf $${file}.json $${file}*.c; \
		  rm -rf $${file}.cdbtex $${file}*.cdbcopy; \
		  rm -rf $${file}.pytex; \
	  done
#-------------------------------------------------------------------------------
# prepare files for github
github:
	@ make pristine
	@ make all
	@ make expected
	@ make rm-tests-output
	@ make rm-dot
	@ make veryclean
	@ rm -rf summary.pdf
	@ rm -rf collection.pdf
	@ for file in $(TARGETS); \
	  do \
		  if [[ -e $${file}.json ]];    then mv -f $${file}.json    lib/.; fi ; \
		  if [[ -e $${file}.cdbtex ]];  then mv -f $${file}.cdbtex  lib/.; fi ; \
		  if [[ -e $${file}.c ]];       then mv -f $${file}.c       lib/.; fi ; \
		  if [[ -e $${file}.cdbcopy ]]; then mv -f $${file}.cdbcopy lib/.; fi ; \
		  if [[ -e $${file}.export ]];  then mv -f $${file}.export  lib/.; fi ; \
	  done

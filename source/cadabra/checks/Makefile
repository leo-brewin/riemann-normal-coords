#-------------------------------------------------------------------------------
SHELL = /bin/bash
#-------------------------------------------------------------------------------
.PHONY: all
#-------------------------------------------------------------------------------
TARGETS = $(patsubst %.tex,%,$(wildcard check-*.tex))
#-------------------------------------------------------------------------------
all:
	@ for file in $(TARGETS); do make .$${file}; done;
#-------------------------------------------------------------------------------
%:
	@ make .$*
.%:	%.tex
	@ echo "cdblatex.sh $@ ..."
	@ cdblatex.sh -T -s -i $@ &> $@.cdblog
	@ # echo " -->"`cputime -i $*.cdblog`
#-------------------------------------------------------------------------------
rm-dot:
	@ rm -rf .[a-z]*
	@ rm -rf .[a-z]*.lb
#-------------------------------------------------------------------------------
clean:
	@ for file in $(TARGETS); \
	  do \
	     rm -f $${file}.aux $${file}.log $${file}.out $${file}.synctex.gz; \
	  done
#-------------------------------------------------------------------------------
veryclean:
	@ make clean
	@ for file in $(TARGETS); \
	  do \
	     rm -f $${file}.cdb $${file}_.cdb; \
		  rm -f $${file}.cdbidx $${file}.cdbtxt $${file}.cdblog; \
		  rm -f $${file}.py $${file}.cdbtex; \
	  done

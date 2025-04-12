SHELL = /bin/bash
#-------------------------------------------------------------------------------
.PHONY:	cadabra pdf expected tests
#-------------------------------------------------------------------------------
all:
	@ make cadabra
	@ make pdf
	@ make veryclean
#-------------------------------------------------------------------------------
cadabra:
	@ echo "> make cadabra ..."
	@ (cd source/cadabra; make)
	@ (cd source/tex; make)
#-------------------------------------------------------------------------------
pdf:
	@ echo "> copy pdf ..."
	@ (cp source/tex/paper.pdf pdf/.)
	@ (cp source/cadabra/collection.pdf pdf/.)
	@ (cp source/cadabra/summary.pdf pdf/.)
#-------------------------------------------------------------------------------
expected:
	@ echo "> make expected ..."
	@ (cd source/cadabra; make expected)
#-------------------------------------------------------------------------------
tests:
	@ echo "> make tests ..."
	@ (cd source/cadabra; make tests)
#-------------------------------------------------------------------------------
rm-dot:
	@ (cd source/cadabra;           make rm-dot)
	@ (cd source/tex;               make rm-dot)
#-------------------------------------------------------------------------------
clean:
	@ (cd source/cadabra;           make clean)
	@ (cd source/tex;               make clean)
#-------------------------------------------------------------------------------
veryclean:
	@ (cd source/cadabra;           make veryclean)
	@ (cd source/tex;               make veryclean)
#-------------------------------------------------------------------------------
pristine:
	@ rm -rf pdf/*
	@ (cd source/cadabra;           make pristine)
	@ (cd source/tex;               make pristine)
#-------------------------------------------------------------------------------
github:
	@ rm -rf pdf/*
	@ (cd source/cadabra;           make github)
	@ (cd source/tex;               make github)

# Riemann Normal Coordinates

## Overview

This repository provides all the LaTeX and Cadabra sources used in preparing the revised version of the paper [Riemann Normal Coordinate expansions using Cadabra][1]. As noted in the revised version, the [original paper][2] does contain some errors in the higher order expansions (though the underlying mathematics was correct).

[Cadabra][3] is an open access program ideally suited to complex tensor commutations in General Relativity. Tensor expressions are written in LaTeX while an enhanced version of Python is used to control the computations. For an introduction to Cadabra see [A tutorial on Cadabra][4].

All of the sources on this repository are written with the Cadabra source embedded in LaTeX documents. Simple tools are used to extract and execute the embedded Cadabra source while also capturing the output and making it available elsewhere in the LaTeX document. These tools have been cloned from the [hybrid-latex][5] repository and can be found in the `hybrid-latex` directory. A copy of the documentation for the Hybrid-LaTeX project is included in the `pdf` directory.

## Documentation

The `pdf` directory contains all of the output generated from the hybrid sources. The main document is `pdf/paper.pdf`. This describes the underlying mathematics (the definitions and algorithms for Riemann normal coordinates) as well as containing selected results. A summary of all of the results can be found in `pdf/summary.pdf` while the complete listing for all of the codes can found in `pdf/collection.pdf`. The file `hybrid-latex/hybrid.pdf` is the main documentation for the [Hybrid LaTeX][5] repository.

## Running the codes

All of the scripts for building and excuting the codes depend on a small set of environment variables. These need to be set just once in each session. To do so, just run

```sh
$ source SETUP.txt
```

form the top directory.

To build everything (provided all dependancies are satisfied, see below), just run

```sh
$ make
```

This will run Cadabra and LaTeX on each of the sources in `source/cadabra` and `source/tex`. Some of the Cadabra codes will take a few minutes to run (see `source/cadabra/TIME.txt` for a list of approximate times).

Makefiles are also provided so you can build individual codes, for example `source/cadabra/dGamma`, using

```sh
$ cd source/cadabra
$ make dGamma
```

There are strict dependencies amongst the codes. These dependencies are included in the Makefiles. See `source/cadabra/SEQUENCE.txt` for a list of the dependencies and the required order of execution.

You can also compile `source/cadabra/dGamma` without using `make` by executing

```sh
$ cd source/cadabra
$ cdblatex.sh -i dGamma
```

This should generate the `dGamma.pdf` file (along with a few other support files). A list of the command line options for `cdblatex.sh` can be found using

```sh
$ cdblatex.sh -h
```

The command line option `-k` will keep all intermediate files and can be useful when trying to locate errors.

The `cdblatex.sh` script will attempt to open the pdf file. You may need to edit that script to use the correct pdf viewer for your platform.

## Testing

You can check your installation by running

```sh
$ cd source/cadabra/
$ make
$ make tests
```

If all goes well then you should see a few lines like

```sh
> diff dGamma.cdbtex
> diff dRabcd.cdbtex
> diff gen2rnc.cdbtex
> diff genGamma.cdbtex
```

There will be more lines (from the other examples). The key thing to observe is that each `diff` command produces no output (apart from a few lines that record execution times as these may vary slightly from one run to the next). There are also some tests that do not use the `diff` command. These tests are run by Cadabra. It reads in the expected results and compares them with the actual results printing out any differences (this allows for non-important differences in expressions to be ignored, for example reordering a sum). The results of those (semantic) tests are recorded in `source/cadabra/tests/semantic/summary.pdf`.

## Dependencies

You will need the Cadabra/Python/SymPy software.

### Cadabra

Cadabra is easy to compile and install. Full details can be found on the [Cadabra repository][6].

### Python/SymPy

A popular distribution of Python3 can be found at the [Anaconda website][7].

If you are not using the latest Anaconda distribution you may need to check that your version of SymPy is at least 1.7 (this is required only during the Ada code generation). You can install the latest version of SymPy in Anaconda using `conda install sympy`.

## Uninstall

To uninstall this project simply delete this directory. This will delete all sources but it will not uninstall Cadabra.

## License

All files in this collection are distributed under the [MIT][8] license. See the file LICENSE.txt for the full details.

  [1]: https://arxiv.org/abs/0903.2087
  [2]: https://iopscience.iop.org/article/10.1088/0264-9381/26/17/175017
  [3]: https://cadabra.science
  [4]: https://github.com/leo-brewin/cadabra-tutorial
  [5]: https://github.com/leo-brewin/hybrid-latex
  [6]: https://github.com/kpeeters/cadabra2
  [7]: https://www.anaconda.com/products/individual
  [8]: https://opensource.org/licenses/MIT

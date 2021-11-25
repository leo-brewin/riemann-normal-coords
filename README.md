# Riemann Normal Coordinates

## Overview

This repository provides all the LaTeX and Cadabra sources used in preparing the revised version of the paper [Riemann Normal Coordinate expansions using Cadabra][1]. As noted in the revised version, the [original paper][2] does contain some errors in the higher order expansions (though the underlying mathematics is correct).

[Cadabra][3] is an open access program ideally suited to complex tensor commutations in General Relativity. Tensor expressions are written in LaTeX while an enhanced version of Python is used to control the computations. For an introduction to Cadabra see [A tutorial on Cadabra][4].

All of the sources on this repository are written with the Cadabra source embedded in LaTeX documents. Simple tools are used to extract and execute the embedded Cadabra source while also capturing the output and making it available elsewhere in the LaTeX document. These tools have been cloned from the [hybrid-latex][5] repository and can be found in the `hybrid-latex/` directory. A copy of the documentation for the Hybrid-LaTeX project is included in the `pdf/` directory.

Note that the hybrid LaTeX tools are not essential in order to work through the files in this repository. The raw Cadabra files (stripped bare of any of the Hybrid-Latex markup) are also included, see the files in `source/cadabra/cdb/`. These can be run either at the command line (as described below) or copied into the Cadabra2 gui. Though taking this approach does mean that the formatting of the Cadabra output will not appear exactly as shown in the tutorial's pdf files (in `pdf/`).

## Documentation

The directory `pdf/` contains all of the output generated from the hybrid sources. The main document is `pdf/paper.pdf`. This describes the underlying mathematics (the definitions and algorithms for Riemann normal coordinates) as well as containing selected results. A summary of all of the results can be found in `pdf/summary.pdf` while the complete listing for all of the codes can found in `pdf/collection.pdf`. The file `hybrid-latex/hybrid.pdf` is the main documentation for the [Hybrid LaTeX][5] repository.

## Installation

Installation is required only if you wish to run or modify any of the Cadabra sources.

Full details on how to install Cadabra can be found on the [Cadabra repository][6].

If you chose not to use the Hybrid-Latex tools then there is no installation required (apart from Cadabra).

The simplest way to install the hybrid latex files is to run the command

    $ source SETPATHS; make install

from the top directory. This will copy the files to newly created directories while also adjusting the various paths to make these files visible to LaTeX and Cadabra. The files, the new directories and their associated paths are as given in the following table.

|  Directory  | Content | Path variable |
|:------------:|:--------|:-------------|
| `$HOME/local/rnc/bin/` | Python and Shell scripts | `$PATH` |
| `$HOME/local/rnc/lib/` | Python libraries | `$PYTHONPATH` |
| `$HOME/local/rnc/tex/` | LaTeX files | `$TEXINPUTS` |

The command `source SETPATHS` will __prepend__ the directories to the appropriate paths while the command `make install` copies the files to their destinations. If you need to recover the original paths, just run `source OLDPATHS`.

If you prefer to install the hybrid latex files in some other directory then you can run the command

    $ source SETPATHS /full/path/to/dir/; make install

where /full/path/to/dir/ is the full path to your prefered directory. The `bin`, `lib` and `tex` directories will be ceated underneath this directory.

## Uninstall

The hybrid latex tools can be uninstalled by deleting the directory `$HOME/local/rnc/` (or the approrpriate directory if you chose a non-default installation).

## Running the codes

To build everything from scratch just run

    $ make

form the top directory. This will run Cadabra and LaTeX on each of the sources in `source/cadabra/` and `source/tex/`. Some of the Cadabra codes will take a few minutes to run (see `source/cadabra/TIME.txt` for a list of approximate times).

Makefiles are also provided so you can build individual codes, for example `source/cadabra/dGamma`, using

    $ cd source/cadabra
    $ make dGamma

There are strict dependencies amongst the codes. These dependencies are included in the Makefiles. See `source/cadabra/SEQUENCE.txt` for a list of the dependencies and the required order of execution.

You can also compile `source/cadabra/dGamma` without using `make` by executing

    $ cd source/cadabra
    $ cdblatex.sh -i dGamma

This should generate the `dGamma.pdf` file (along with a few other support files). A list of the command line options for `cdblatex.sh` can be found using

    $ cdblatex.sh -h

The command line option `-k` will keep all intermediate files and can be useful when trying to locate errors.

The `cdblatex.sh` script will attempt to open the pdf file. You may need to edit that script to use the correct pdf viewer for your platform.

If you are not using the Hybrid-LaTeX tools then you would type

    $ cd source/cadabra/cdb
    $ cadabra2python dGamma.cdb dGamma.py
    $ cadabra2 dGamma.py

This will produce plain text output.

You could also copy and paste `dGamma.cdb` into the Cadabra2 gui.

## Testing

You can check your installation by running (from the command line)

    $ cd source/cadabra/
    $ make
    $ make tests

If all goes well then you should see a few lines like

    > diff dGamma.cdbtex
    > diff dRabcd.cdbtex
    > diff gen2rnc.cdbtex
    > diff genGamma.cdbtex

There will be more lines (from the other examples). The key thing to observe is that each `diff` command produces no output (apart from a few lines that record execution times as these may vary slightly from one run to the next). There are also some tests that do not use the `diff` command. These tests are run by Cadabra. It reads in the expected results and compares them with the actual results printing out any differences (this allows for non-important differences in expressions to be ignored, for example reordering a sum). The results of those (semantic) tests are recorded in `source/cadabra/tests/semantic/summary.pdf`.

## Dependencies

You will need the Cadabra/Python/SymPy software.

### Cadabra

Cadabra is easy to compile and install. Full details can be found on the [Cadabra repository][6].

### Python/SymPy

The codes have been tested with both Python2 and Python3. Since Python2 is deprecated it would be wise to use Python3. A popular distribution of Python3 can be found at the [Anaconda website][7].

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

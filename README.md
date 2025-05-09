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

Ready to run binraries are available for many popular operating systems. These can be found on the [Cadabra binaries][11] page.

Cadabra can also be easily compiled from source. Full details can be found at the [Cadabra repository][6].

### Python/SymPy

Most of the popular operating system have Python3 already installed. You can check your version by running

```sh
$ python --version
```

If that does not report version 3 or later, then you will need to manually install python. Most operating systems provide native package managers (HomeBrew on macOs, apt/dnf/yum on Linux) that you can use to do the job. Otherwise, you can install Python3 using [Conda miniforge][7].

You will also need version 1.7 or later of sympy. That may already be part of your python environment. You can check which version you have (if any) by running

```sh
$ pip list | grep sympy
```

You can upgrade sympy to the latest version using

```sh
$ pip install --upgrade sympy
```

If you need to install sympy, then it is best to do so using a python virtual environment. This ensures that you leave the operating system's version of python intact. See the official [Python docs][9] on creating, using and managing virtual environments. Another very useful introduction to virtual environments can be found in this [primer][10].

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
  [7]: https://github.com/conda-forge/miniforge
  [8]: https://opensource.org/licenses/MIT
  [9]: https://docs.python.org/3/tutorial/venv.html
 [10]: https://realpython.com/python-virtual-environments-a-primer/
 [11]: https://cadabra.science/download.html
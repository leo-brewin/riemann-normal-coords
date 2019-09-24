#! /bin/bash

(cd cadabra; make github)
(cd tex; make github)

mkdir -p ../pdf

cp -rf tex/paper.pdf                           ../pdf/paper.pdf
cp -rf cadabra/pdf/summary.pdf                 ../pdf/summary.pdf
cp -rf cadabra/pdf/collection.pdf              ../pdf/collection.pdf

#! /bin/bash

mkdir -p ../pdf

(cd cadabra; make; make veryclean)
(cd tex; make; make veryclean)

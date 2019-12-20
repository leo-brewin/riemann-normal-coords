#! /bin/bash

mkdir -p ../pdf

(cd cadabra; make github)
(cd tex; make github)

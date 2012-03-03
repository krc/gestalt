#!/bin/bash

(python main.py) &
sleep 0.1
python -m unittest integration_test &
python shutdown.py

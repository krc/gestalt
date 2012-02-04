#!/bin/bash

(python main.py) &
python -m unittest integration_test

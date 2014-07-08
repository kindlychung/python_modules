#!/bin/bash

sudo rsync -avu ./startbloggerPost /usr/lib/python2.7/dist-packages/
exepy=$HOME/bin/startblogger.py
ln -s /usr/lib/python2.7/dist-packages/startbloggerPost/startblogger.py $exepy

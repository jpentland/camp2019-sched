#!/bin/sh
set -e
read -p "This should only be run on termux, press ctrl+c to exit or return to continue"
apt update
apt install -y clang python libiconv libxml2 libxslt zlib
pip install lxml pytz python-dateutil requests

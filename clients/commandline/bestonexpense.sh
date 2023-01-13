#!/bin/bash
#please set these variables


BASE_URL = http://127.0.0.1:8000

curl --data "token=$1&amount=$2&text=$3" $BASE_URL/web/Exopense/
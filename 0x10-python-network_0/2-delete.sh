#!/bin/bash
#script that sends a DELETE request to the URL passed as the first arg
curl -sX DELETE "$1"

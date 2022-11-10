#!/bin/sh
docker login -u 151214 -p salman1464
if [ "$TRAVIS_BRANCH" = "master" ]; then
    TAG="latest"
else
    TAG="$TRAVIS_BRANCH"
fi
docker build -f Dockerfile -t majic .
docker image push 151214/8dfoodh/majic:latest
#!/bin/sh
IMAGE_TAG="acsf-aoc-2022-day07-docker"
INPUT="${1:-$(pwd)/input.txt}"

if ! docker images | grep -q "$IMAGE_TAG" ; then
    docker build -t "$IMAGE_TAG" .
fi

docker run -it \
  --rm \
  -v "$INPUT:/tmp/input.txt:ro" \
  "$IMAGE_TAG"

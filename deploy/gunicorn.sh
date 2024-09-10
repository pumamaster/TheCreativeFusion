#!/bin/bash

NAME="thecreativefusion"
DJANGODIR=$(dirname $(realpath $0))
SOCKFILE=/tmp/gunicorn-thecreativefusion.sock
LOGDIR=${DJANGODIR}/logs
LOGFILE=${LOGDIR}/gunicorn.log
USER=alex
GROUP=alex
NUM_WORKERS=5
DJANGO_WSGI_MODULE=ShinyLove.wsgi

mkdir -p $LOGDIR

rm -f $SOCKFILE

echo $DJANGODIR

cd $DJANGODIR

exec /home/alex/TheCreativeFusion/env/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
--name $NAME \
--workers $NUM_WORKERS \
--user=$USER --group=$GROUP \
--bind=unix:$SOCKFILE \
--log-level=debug \
--log-file=$LOGFILE

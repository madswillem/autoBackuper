#!/bin/bash
read test

echo $1

CURRENTDATE=`date +"%d-%m-%Y"`
tar -czf /run/media/mads/Backup/backup${CURRENTDATE}.tar.gz /home/${USER}/Dokumente
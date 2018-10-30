#!/bin/bash

COLOR_SERVER="color_server.py"
SCRIPT=`realpath $0`
SCRIPTPATH=`dirname $SCRIPT`

echo $SCRIPTPATH/$COLOR_SERVER

#!/bin/bash
while :
do
    echo "Running $COLOR_SERVER"
	echo "Press [CTRL+C] to stop.."
    sudo python $SCRIPTPATH/$COLOR_SERVER
	sleep 1
done

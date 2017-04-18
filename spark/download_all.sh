#!/bin/bash

DIRNAME=$(dirname $0)
find ${DIRNAME} -name '*\.sh' -print | xargs chmod a+x
sync

for script in $(find $DIRNAME -name '*\.sh'); do
    if [[ $script != $0 ]]; then
	echo "running $script ..."
	${script}
    fi
done

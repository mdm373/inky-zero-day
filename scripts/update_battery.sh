
rm ./.temp/battery.txt
echo "updating battery value"
COUNT=0
while ! [ -s ./.temp/battery.txt ]; do
    echo "get battery" | nc -q 0 localhost 8423 > ./.temp/battery.txt
    echo "..."
    sleep 1 # throttle the check
    COUNT=$((COUNT+1))
    if test ${COUNT} -eq 3 ; then
      echo "failed to update battery"
      exit 1
    fi
done
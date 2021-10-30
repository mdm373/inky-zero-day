
rm ./.temp/battery.txt -f
echo "updating battery value"
COUNT=0
echo "get battery" | nc -q 0 localhost 8423 > ./.temp/battery.txt
while ! [ -s ./.temp/battery.txt ]; do
    echo "..."
    sleep 5 # throttle the check
    COUNT=$((COUNT+1))
    if test ${COUNT} -eq 10 ; then
      echo "failed to update battery"
      exit 1
    fi
    echo "get battery" | nc -q 0 localhost 8423 > ./.temp/battery.txt
done
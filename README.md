#buncha servers

test your multithreaded curler program!

## requires

flash

## usage

```
./servers_up NUM_SERVERS:wq
```

## gogo

```bash
sudo apt -y install virtualenv
virualenv venv
source venv/bin/activate
./servers_up 5
for i in `seq 1 5`; do
  curl "http://localhost:500$i"
done
```

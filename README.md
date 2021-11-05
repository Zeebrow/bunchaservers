#buncha servers

Get a bunch of Flasks without being known as the town alcoholic

## requires

flash

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

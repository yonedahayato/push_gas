docker build -t push_line .
docker run --rm -itp 8091:8091 push_line

docker rmi push_line

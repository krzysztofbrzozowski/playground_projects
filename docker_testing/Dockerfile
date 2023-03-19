# Use existing docker image as a base
FROM alpine

# Download and install dependencies
RUN apk add --update redis

# What to do after container started
CMD ["redis-server"]
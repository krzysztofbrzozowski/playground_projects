const express = require('express');
const redis = require('redis');
const process = require('process');

const app = express();
// Since app is running in Docker, specifying redis container name is fine
const client = redis.createClient({
  host: 'redis-server',
  port: 6379,
});
client.set('visits', 0);

app.get('/', (req, res) => {
  client.get('visits', (err, visits) => {
    // Testing purposes only
    process.exit(0)
    res.send('Number of visits ' + visits);
    client.set('visits', parseInt(visits) + 1);
  });
});

app.listen(8081, () => {
  console.log('Listening on port 8081');
});
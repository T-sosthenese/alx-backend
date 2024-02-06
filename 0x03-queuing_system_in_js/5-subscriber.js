import { createClient } from "redis";
const redis = require('redis');

const subscriber = createClient();

(async () => {
  subscriber.on('error', (error) => {
    console.log("Redis client not connected to the server:", error)
  })
  .on('connect', () => {
    console.log("Redis client connected to the server")
  });

  subscriber.subscribe('holberton school channel');

  subscriber.on('message', (channel,message) => {
    console.log(message);

    if (message === 'KILL_SERVER') {
      subscriber.unsubscribe('holberton school channel');
      subscriber.quit();
    }
  });
})();

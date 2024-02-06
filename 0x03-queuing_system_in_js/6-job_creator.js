import { createQueue } from "kue";

const queue = createQueue();

const job = queue.create('push_notification_code', {
  phoneNumber: '24512345678',
  message: 'This is to verify your account',
}).save((err) => {
  if (!err) console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => console.log('Notification job completed'));
job.on('failed', () => console.log('Notification job failed'));

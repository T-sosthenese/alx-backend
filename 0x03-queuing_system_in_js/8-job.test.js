import { createQueue } from "kue";
import { expect } from "chai";
import sinon from 'sinon';

import createPushNotificationsJobs from './8-job';

const queue = createQueue();

describe('createPushNotificationsJobs', () => {
  beforeEach(() => {
    queue.testMode.enter();
  });

  it('Displays an error message if jobs is not an array', () => {
    const jobs = { 'this is a dict': 'true' };
    expect(() => createPushNotificationsJobs(jobs, queue)).to.throw();
  });

  it('Creates two new jobs to the queue', () => {
    const jobs = [
      {
        phoneNumber: '4153118782',
        message: 'This is the code 4321 to verify your account'
      },
      {
        phoneNumber: '4153718781',
        message: 'This is the code 4562 to verify your account'
      },
    ];
    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
  });

  it('Displays the correct message when a job is created', () => {
    const jobs = [
      {
        phoneNumber: '4159518782',
        message: 'This is the code 4321 to verify your account'
      },
    ];
    createPushNotificationsJobs(jobs, queue);
    const curJob = queue.testMode.jobs[0];
    curJob._events.complete();
    const spy = sinon.spy(console, 'log');
    expect(spy.calledWith(`Notification job ${curJob.id} completed`)).to.equal(true);
    spy.restore();
  });

  it('Displays a correct message for job progress', () => {
    const jobs = [
      {
        phoneNumber: '4159518782',
        message: 'This is the code 4321 to verify your account'
      },
    ];
    createPushNotificationsJobs(jobs, queue);
    const curJob = queue.testMode.jobs[0];
    const spy = sinon.spy(console, 'log');

    const progress = 75;
    curJob._events.progress(progress);
    expect(spy.calledWith(`Notification job ${curJob.id} ${progress}% complete`)).to.equal(true);
    spy.restore();
  });

  it('Displays the correct error message when a job fails with error', () => {
    const jobs = [
      {
        phoneNumber: '4159518782',
        message: 'This is the code 4321 to verify your account'
      },
    ];
    createPushNotificationsJobs(jobs, queue);

    const curJob = queue.testMode.jobs[0];
    const spy = sinon.spy(console, 'log');
    const err = 'This job failed';

    curJob._events.failed(err);
    expect(spy.calledWith(`Notification job ${curJob.id} failed: ${err}`)).to.equal(true);
    spy.restore();
  });

  afterEach(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });
});
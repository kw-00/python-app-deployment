import http from 'k6/http';
import { sleep, check } from 'k6';

export const options = {
  stages: [
    { duration: '10s', target: 10 },   // ramp up
    { duration: '30s', target: 50 },   // steady load
    { duration: '10s', target: 0 },    // ramp down
  ],
};

const BASE_URL = 'http://localhost';

export default function () {
  // GET users page
  let res1 = http.get(`${BASE_URL}/users`);
  check(res1, {
    'users status 200': (r) => r.status === 200,
  });

  // POST new user
  let payload = JSON.stringify({
    name: 'test',
    surname: 'user'
  });

  let params = {
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
  };

  http.post(`${BASE_URL}/users`, payload, params);

  sleep(1);
}
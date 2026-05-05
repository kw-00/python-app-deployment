import http from 'k6/http';
import { sleep, check } from 'k6';

export const options = {
  stages: [
    { duration: '10s', target: 10 },
    { duration: '30s', target: 50 },
    { duration: '10s', target: 0 },
  ],
  thresholds: {
    http_req_failed: ['rate<0.01'], // <1% errors
    http_req_duration: ['p(95)<500'], // 95% under 500ms
  },
};

const BASE_URL = __ENV.BASE_URL || 'http://localhost';

export default function () {
  // GET /users
  let res1 = http.get(`${BASE_URL}/users`);

  check(res1, {
    'GET /users status 200': (r) => r.status === 200,
    'GET /users fast enough': (r) => r.timings.duration < 500,
  });

  // POST /users (JSON correctly)
  let payload = JSON.stringify({
    name: 'test',
    surname: 'user'
  });

  let params = {
    headers: {
      'Content-Type': 'application/json',
    },
  };

  let res2 = http.post(`${BASE_URL}/users`, payload, params);

  check(res2, {
    'POST /users status 200 or 201': (r) => r.status === 200 || r.status === 201,
    'POST responds fast': (r) => r.timings.duration < 500,
  });

  sleep(1);
}
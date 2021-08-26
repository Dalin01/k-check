import axios from 'axios';

export const noAuthInstance = axios.create({
  baseURL: process.env.REACT_APP_BASE_URL && process.env.REACT_APP_BASE_URL,
  timeout: 8000,
  headers: {
    'Content-Type': 'application/json',
  },
});

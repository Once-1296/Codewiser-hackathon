import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export const generateSchedule = (data) => {
  return API.post("/schedule/generate", data);
};
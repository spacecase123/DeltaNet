const express = require("express");
const app = express();

app.use(
  express.urlencoded({
    extended: true,
  })
);
app.use(express.json());

app.listen(8080, () => {
  axios
    .get("https://ifconfig.me/")
    .then((res) => {
      const ip = res.data;
    })
    .catch(() => {
      const ip = "Error";
    });
});

const gay = {};
const rateMap = new Map();

gay.checkRate = (req, res, next) => {
  if (!rateMap.has("429")) {
    rateMap.set("429", "lol");
    setTimeout(() => {
      rateMap.delete("429");
    }, 60000);
    next();
  } else {
    return res.status(429).json({
      message: "Rate Limit"
    });
  }
};

module.exports = gay;
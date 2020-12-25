var express = require('express');
const path = require("path");
const fs = require("fs");
var router = express.Router();

/* GET users listing. */
router.get('/', function(req, res, next) {
  res.render('makepdf');
});

module.exports = router;

var express = require('express');
var fs = require('fs');
const path = require("path");
const {spawn} = require('child_process'); 
var router = express.Router();

/* GET home page. */
router.post('/', (req, res) => {
    var dataToSend;
    var data = req.body;
    console.log(data)
    const python = spawn('python3', ['public/python/pdf.py', data.nSchool, data.nSubject, data.nProf,data.nQue]);
    python.stdout.on('data', function (data) {
        dataToSend = data.toString();
    });
    python.on('close', (code) => {
        console.log(`child process close all stdio with code ${code}`);

        var file = fs.createReadStream("./public/pdf/gab.pdf");
        res.contentType('application/pdf')
        file.pipe(res);
    });
});

module.exports = router;
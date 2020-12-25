document.querySelector('#submit').onclick = function(){
    fetch('/makepdf', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            nSchool: document.querySelector('#nSchool').value,
            nSubject: document.querySelector('#nSubject').value,
            nProf: document.querySelector('#nProf').value,
            nQue: document.querySelector('#nQue').value
        })
    }).then(function(res) {
        res.blob().then(function(resq){
            var fileURL = URL.createObjectURL(resq)
            document.querySelector('#img').src = fileURL
        });
    });
}


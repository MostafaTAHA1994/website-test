function calculate() {
    var num1 = parseFloat(document.getElementById('Ptot').value);
    var num2 = parseFloat(document.getElementById('Pstat').value);
    var operation = document.getElementById('gas').value;

    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
            'Ptot': num1,
            'Pstat': num2,
            'gas': operation
        })
    })
    .then(response => response.json())
    .then(data => {
        var resultContainer = document.getElementById('result-container');
        resultContainer.innerHTML = '<p> Mach Number = ' + data.result + '</p>';
    })
    .catch(error => console.error('Error:', error));
}
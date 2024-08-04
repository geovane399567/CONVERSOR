function convertTemp() {
    const inputTemp = parseFloat(document.getElementById('inputTemp').value);
    const inputUnit = document.getElementById('inputUnit').value;
    const outputUnit = document.getElementById('outputUnit').value;

    let result;

    if (isNaN(inputTemp)) {
        result = "Por favor, insira um valor válido.";
    } else {
        if (inputUnit === outputUnit) {
            result = inputTemp;
        } else if (inputUnit === 'celsius') {
            if (outputUnit === 'fahrenheit') {
                result = (inputTemp * 9/5) + 32;
            } else if (outputUnit === 'kelvin') {
                result = inputTemp + 273.15;
            }
        } else if (inputUnit === 'fahrenheit') {
            if (outputUnit === 'celsius') {
                result = (inputTemp - 32) * 5/9;
            } else if (outputUnit === 'kelvin') {
                result = ((inputTemp - 32) * 5/9) + 273.15;
            }
        } else if (inputUnit === 'kelvin') {
            if (outputUnit === 'celsius') {
                result = inputTemp - 273.15;
            } else if (outputUnit === 'fahrenheit') {
                result = ((inputTemp - 273.15) * 9/5) + 32;
            }
        }
    }

    document.getElementById('result').innerText = `Resultado: ${result} ${outputUnit.charAt(0).toUpperCase() + outputUnit.slice(1)}`;
}

function resetApp() {
    document.getElementById('inputTemp').value = '';
    document.getElementById('result').innerText = '';
}

function closeApp() {
    window.close();
}

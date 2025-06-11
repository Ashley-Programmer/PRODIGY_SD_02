// Temperature conversion functions => It's a nested object
const conversions = {
    celsius: {
        // c -> temp value
        fahrenheit: (c) => (c * 9 / 5) + 32, // arrow function conversion (celsius to fahrenheit) (=> -> Means returns)
        kelvin: (c) => c + 273.15 // arrow function => celsius to fahrenheit
    },
    fahrenheit: {
        celsius: (f) => (f - 32) * 5 / 9,
        kelvin: (f) => (f - 32) * 5 / 9 + 273.15
    },
    kelvin: {
        celsius: (k) => k - 273.15,
        fahrenheit: (k) => (k - 273.15) * 9 / 5 + 32
    }
};

// Conversion formulas for display
const formulas = {
    'celsius-fahrenheit': '°F = (°C × 9/5) + 32',
    'celsius-kelvin': 'K = °C + 273.15',
    'fahrenheit-celsius': '°C = (°F - 32) × 5/9',
    'fahrenheit-kelvin': 'K = (°F - 32) × 5/9 + 273.15',
    'kelvin-celsius': '°C = K - 273.15',
    'kelvin-fahrenheit': '°F = (K - 273.15) × 9/5 + 32'
};

// Unit symbols
const units = {
    celsius: '°C',
    fahrenheit: '°F',
    kelvin: 'K'
};

function validateInput(value, fromScale) {
    if (isNaN(value) || value === '') {
        throw new Error('Please enter a valid number');
    }

    // Check for absolute zero violations
    if (fromScale === 'celsius' && value < -273.15) {
        throw new Error('Temperature cannot be below absolute zero (-273.15°C)');
    }
    if (fromScale === 'fahrenheit' && value < -459.67) {
        throw new Error('Temperature cannot be below absolute zero (-459.67°F)');
    }
    if (fromScale === 'kelvin' && value < 0) {
        throw new Error('Kelvin temperature cannot be negative');
    }

    return parseFloat(value);
}

function convertTemperature(value, fromScale, toScale) {
    if (fromScale === toScale) {
        return value;
    }

    return conversions[fromScale][toScale](value);
}

function showResult(originalValue, fromScale, convertedValue, toScale) {
    const resultDiv = document.getElementById('result');
    const formulaDiv = document.getElementById('formula');

    resultDiv.innerHTML = `
                <strong>${originalValue}${units[fromScale]} = ${convertedValue.toFixed(2)}${units[toScale]}</strong>
            `;

    // Show formula
    const formulaKey = `${fromScale}-${toScale}`;
    if (formulas[formulaKey]) {
        formulaDiv.innerHTML = `Formula: ${formulas[formulaKey]}`;
        formulaDiv.style.display = 'block';
    }

    resultDiv.style.display = 'block';
    hideError();
}

function showError(message) {
    const errorDiv = document.getElementById('error');
    errorDiv.textContent = message;
    errorDiv.style.display = 'block';
    hideResult();
}

function hideResult() {
    document.getElementById('result').style.display = 'none';
    document.getElementById('formula').style.display = 'none';
}

function hideError() {
    document.getElementById('error').style.display = 'none';
}

function clearForm() {
    document.getElementById('converterForm').reset();
    hideResult();
    hideError();
}

// Form submission handler
document.getElementById('converterForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const temperature = document.getElementById('temperature').value;
    const fromScale = document.getElementById('fromScale').value;
    const toScale = document.getElementById('toScale').value;

    try {
        // Validate inputs
        if (!fromScale || !toScale) {
            throw new Error('Please select both source and target temperature scales');
        }

        const validatedTemp = validateInput(temperature, fromScale);
        const convertedTemp = convertTemperature(validatedTemp, fromScale, toScale);

        showResult(validatedTemp, fromScale, convertedTemp, toScale);
    } catch (error) {
        showError(error.message);
    }
});

// Real-time conversion (optional feature)
document.getElementById('temperature').addEventListener('input', function () {
    const fromScale = document.getElementById('fromScale').value;
    const toScale = document.getElementById('toScale').value;

    if (this.value && fromScale && toScale) {
        try {
            const validatedTemp = validateInput(this.value, fromScale);
            const convertedTemp = convertTemperature(validatedTemp, fromScale, toScale);
            showResult(validatedTemp, fromScale, convertedTemp, toScale);
        } catch (error) {
            // Don't show errors during real-time typing
            hideResult();
        }
    }
});

// Update conversion when scales change
['fromScale', 'toScale'].forEach(id => {
    document.getElementById(id).addEventListener('change', function () {
        const temperature = document.getElementById('temperature').value;
        const fromScale = document.getElementById('fromScale').value;
        const toScale = document.getElementById('toScale').value;

        if (temperature && fromScale && toScale) {
            try {
                const validatedTemp = validateInput(temperature, fromScale);
                const convertedTemp = convertTemperature(validatedTemp, fromScale, toScale);
                showResult(validatedTemp, fromScale, convertedTemp, toScale);
            } catch (error) {
                showError(error.message);
            }
        }
    });
});
async function analyzeData() {
    const imageInput = document.getElementById('imageInput');
    const symptoms = document.getElementById('symptoms').value;
    const resultsDiv = document.getElementById('results');
    const resultText = document.getElementById('resultText');

    if (!symptoms) {
        alert('Please enter symptoms.');
        return;
    }

    // Show loading text
    resultsDiv.style.display = 'block';
    resultText.textContent = 'Processing...';

    const formData = new FormData();
    if (imageInput.files[0]) {
        formData.append('image', imageInput.files[0]); // Optional for future use
    }
    formData.append('symptoms', symptoms);

    try {
        const response = await fetch('https://misswd-qwertymodel.hf.space/run/predict', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        resultText.textContent = `Prediction: ${data.prediction}\nDetails: ${data.details}`;

    } catch (error) {
        resultText.textContent = 'An error occurred: ' + error.message;
    }
}

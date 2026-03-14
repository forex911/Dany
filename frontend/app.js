document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('process-form');
    const urlInput = document.getElementById('url-input');
    const submitBtn = document.getElementById('submit-btn');
    const btnText = document.querySelector('.btn-text');
    const spinner = document.querySelector('.spinner');
    
    const resultContainer = document.getElementById('result-container');
    const resultDisclaimer = document.getElementById('result-disclaimer');
    const jsonOutput = document.getElementById('json-output');
    
    const errorContainer = document.getElementById('error-container');
    const errorMessage = document.getElementById('error-message');

    // The backend URL - change if deployed
    const API_BASE_URL = 'http://127.0.0.1:5000';

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const targetUrl = urlInput.value.trim();
        if (!targetUrl) return;

        // Reset UI
        hideAllContainers();
        setLoadingState(true);

        try {
            const response = await fetch(`${API_BASE_URL}/process`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ url: targetUrl })
            });

            const data = await response.json();

            if (response.ok && data.status === 'success') {
                showSuccess(data.data);
            } else {
                showError(data.message || 'An error occurred while processing the request.');
            }
        } catch (error) {
            console.error('Fetch error:', error);
            showError('Failed to connect to the backend server. Make sure it is running on ' + API_BASE_URL);
        } finally {
            setLoadingState(false);
        }
    });

    function setLoadingState(isLoading) {
        if (isLoading) {
            submitBtn.disabled = true;
            btnText.classList.add('hidden');
            spinner.classList.remove('hidden');
        } else {
            submitBtn.disabled = false;
            btnText.classList.remove('hidden');
            spinner.classList.add('hidden');
        }
    }

    function hideAllContainers() {
        resultContainer.classList.add('hidden');
        errorContainer.classList.add('hidden');
    }

    function showSuccess(data) {
        if (data.disclaimer) {
            resultDisclaimer.textContent = data.disclaimer;
        }
        
        // Pretty print JSON response
        jsonOutput.textContent = JSON.stringify(data, null, 2);
        
        resultContainer.classList.remove('hidden');
    }

    function showError(message) {
        errorMessage.textContent = message;
        errorContainer.classList.remove('hidden');
    }
});

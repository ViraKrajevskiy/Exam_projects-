document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');
    const tokenDisplay = document.getElementById('tokens');
    const errorMessage = document.getElementById('error-message');

    loginForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const data = {
            username: document.getElementById('login-username').value,
            password: document.getElementById('login-password').value,
        };

        try {
            const response = await fetch('/auth/login/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            });

            const result = await response.json();
            if (response.ok) {
                tokenDisplay.innerText = `Access: ${result.access}\nRefresh: ${result.refresh}`; // Покажет токены
            } else {
                errorMessage.innerText = `Ошибка входа: ${result.error || "Неизвестная ошибка"}`;
            }
        } catch (error) {
            errorMessage.innerText = `Ошибка подключения: ${error.message}`;
        }
    });
});

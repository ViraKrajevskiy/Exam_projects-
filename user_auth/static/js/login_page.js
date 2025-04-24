document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');
    const tokenDisplay = document.getElementById('tokens');
    const errorMessage = document.getElementById('error-message');

    loginForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const data = {
            phone_number: document.getElementById('login-phone').value,
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
                localStorage.setItem('access_token', result.access);
                localStorage.setItem('refresh_token', result.refresh);
                tokenDisplay.innerText = `Access: ${result.access}\nRefresh: ${result.refresh}`;
                window.location.href = '/main_page/'; // редирект после входа
            } else {
                errorMessage.innerText = `Ошибка входа: ${result.detail || result.error || "Неизвестная ошибка"}`;
            }
        } catch (error) {
            errorMessage.innerText = `Ошибка подключения: ${error.message}`;
        }
    });
});

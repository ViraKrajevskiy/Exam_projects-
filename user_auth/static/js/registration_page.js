document.addEventListener('DOMContentLoaded', () => {
    const registerForm = document.getElementById('register-form');
    const errorMessage = document.getElementById('error-message');

    registerForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const data = {
            username: document.getElementById('register-username').value,
            email: document.getElementById('register-email').value,
            password: document.getElementById('register-password').value,
        };

        try {
            const response = await fetch('/auth/register/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            });

            const result = await response.json();
            if (response.ok) {
                alert(result.message); // Покажет сообщение об успешной регистрации
            } else {
                errorMessage.innerText = `Ошибка регистрации: ${result.message || "Неизвестная ошибка"}`;
            }
        } catch (error) {
            errorMessage.innerText = `Ошибка подключения: ${error.message}`;
        }
    });
});

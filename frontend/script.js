document.addEventListener('DOMContentLoaded', function () {
    const loginForm = document.getElementById('login-form');
    const usernameInput = document.getElementById('username');
    const passwordInput = document.getElementById('password');
    const roleSelect = document.getElementById('role');
    const usernameError = document.getElementById('username-error');
    const passwordError = document.getElementById('password-error');
    const roleError = document.getElementById('role-error');

    function isValidEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }

    function isValidUsername(username) {
        const usernameRegex = /^[a-zA-Z0-9_]{3,20}$/;
        return usernameRegex.test(username);
    }

    function validateForm() {
        let isValid = true;

        usernameError.style.display = 'none';
        passwordError.style.display = 'none';
        roleError.style.display = 'none';
        usernameInput.style.borderColor = '#e2e8f0';
        passwordInput.style.borderColor = '#e2e8f0';
        roleSelect.style.borderColor = '#e2e8f0';

        const usernameValue = usernameInput.value.trim();
        if (!usernameValue) {
            usernameError.textContent = 'Please enter your email or username';
            usernameError.style.display = 'block';
            usernameInput.style.borderColor = '#e53e3e';
            isValid = false;
        } else if (!isValidEmail(usernameValue) && !isValidUsername(usernameValue)) {
            usernameError.textContent = 'Please enter a valid email or username (3-20 alphanumeric characters)';
            usernameError.style.display = 'block';
            usernameInput.style.borderColor = '#e53e3e';
            isValid = false;
        }

        if (passwordInput.value.length < 6) {
            passwordError.textContent = 'Password must be at least 6 characters';
            passwordError.style.display = 'block';
            passwordInput.style.borderColor = '#e53e3e';
            isValid = false;
        }

        if (!roleSelect.value) {
            roleError.textContent = 'Please select your role';
            roleError.style.display = 'block';
            roleSelect.style.borderColor = '#e53e3e';
            isValid = false;
        }

        return isValid;
    }

    function fileExists(url, callback) {
        const xhr = new XMLHttpRequest();
        xhr.open('HEAD', url, true);
        xhr.onload = function () {
            callback(xhr.status === 200);
        };
        xhr.onerror = function () {
            callback(false);
        };
        xhr.send();
    }

    function handleSubmit(e) {
        e.preventDefault();

        if (validateForm()) {
            const loginBtn = document.querySelector('.login-btn');
            const originalText = loginBtn.textContent;
            loginBtn.textContent = 'Logging in...';
            loginBtn.disabled = true;

            setTimeout(function () {
                const role = roleSelect.value;
                const roleName = role.charAt(0).toUpperCase() + role.slice(1);

                const successMessage = document.createElement('div');
                successMessage.className = 'success-message';
                successMessage.style.cssText = `
                    background-color: #48bb78;
                    color: white;
                    padding: 1rem;
                    border-radius: 8px;
                    margin-top: 1rem;
                    text-align: center;
                    font-weight: 600;
                `;
                successMessage.textContent = `Login successful! Redirecting to ${roleName} dashboard...`;
                loginForm.parentNode.insertBefore(successMessage, loginForm.nextSibling);

                localStorage.setItem("loggedInUser", JSON.stringify({
                    username: usernameInput.value.trim(),
                    role: role
                }));

                setTimeout(function () {
                    let targetPage = "";

                    if (role === "admin") targetPage = "admin_dashboard.html";
                    else if (role === "faculty") targetPage = "faculty_dashboard.html";
                    else if (role === "student") targetPage = "student_dashboard.html";

                    fileExists(targetPage, function (exists) {
                        if (exists) {
                            window.location.href = targetPage;
                        } else {
                            alert(`Error: ${targetPage} not found. Redirecting to login page.`);
                            window.location.href = "login.html";
                        }
                        loginBtn.textContent = originalText;
                        loginBtn.disabled = false;
                    });
                }, 2000);
            }, 1500);
        }
    }

    usernameInput.addEventListener('input', function () {
        if (usernameInput.value.trim()) {
            usernameError.style.display = 'none';
            usernameInput.style.borderColor = '#e2e8f0';
        }
    });

    passwordInput.addEventListener('input', function () {
        if (passwordInput.value.length >= 6) {
            passwordError.style.display = 'none';
            passwordInput.style.borderColor = '#e2e8f0';
        }
    });

    roleSelect.addEventListener('change', function () {
        if (roleSelect.value) {
            roleError.style.display = 'none';
            roleSelect.style.borderColor = '#e2e8f0';
        }
    });

    loginForm.addEventListener('submit', handleSubmit);

    loginForm.addEventListener('blur', function (e) {
        if (e.target.matches('input, select') && !e.target.value.trim()) {
            e.target.style.borderColor = '#e53e3e';
        }
    }, true);
});

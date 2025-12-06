document.addEventListener('DOMContentLoaded', function () {
    const formWrapper = document.getElementById('institute-form-wrapper');

    formWrapper.innerHTML = `
        <form id="institute-form">
            <h3>Institute Details</h3>
            <div class="input-group">
                <label for="institute-name">Institute Name</label>
                <input type="text" id="institute-name" class="input-field" placeholder="Enter institute name" required>
                <div class="error" id="institute-name-error">Please enter the institute name</div>
            </div>
            
            <div class="input-group">
                <label for="institute-email">Institute Email</label>
                <input type="email" id="institute-email" class="input-field" placeholder="Enter institute email" required>
                <div class="error" id="institute-email-error">Please enter a valid email</div>
            </div>

            <div class="input-group">
                <label for="institute-type">Institute Type</label>
                <select id="institute-type" class="select-field" required>
                    <option value="" disabled selected>Select institute type</option>
                    <option value="university">University</option>
                    <option value="college">College</option>
                    <option value="school">School</option>
                </select>
                <div class="error" id="institute-type-error">Please select institute type</div>
            </div>

            <div class="input-group">
                <label for="timezone">Timezone</label>
                <input type="text" id="timezone" class="input-field" placeholder="e.g., IST, GMT+5:30" required>
                <div class="error" id="timezone-error">Please enter timezone</div>
            </div>

            <h3>Admin Details</h3>
            <div class="input-group">
                <label for="admin-name">Admin Name</label>
                <input type="text" id="admin-name" class="input-field" placeholder="Enter admin name" required>
                <div class="error" id="admin-name-error">Please enter admin name</div>
            </div>

            <div class="input-group">
                <label for="admin-email">Admin Email</label>
                <input type="email" id="admin-email" class="input-field" placeholder="Enter admin email" required>
                <div class="error" id="admin-email-error">Please enter valid email</div>
            </div>

            <div class="input-group">
                <label for="admin-password">Password</label>
                <input type="password" id="admin-password" class="input-field" placeholder="Enter password" required>
                <div class="error" id="admin-password-error">Password must be at least 6 characters</div>
            </div>

            <div class="input-group">
                <label for="admin-password-confirm">Confirm Password</label>
                <input type="password" id="admin-password-confirm" class="input-field" placeholder="Confirm password" required>
                <div class="error" id="admin-password-confirm-error">Passwords must match</div>
            </div>

            <button type="submit" class="login-btn">Register Institute</button>
        </form>
    `;

    // You can now add validation and submission logic here, similar to login.js
});

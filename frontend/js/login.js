// Login page component
function loginForm() {
    return {
        districtCode: '',
        userNumber: '',
        password: '',
        showPassword: false,
        isLoading: false,
        errorMessage: '',
        errors: { districtCode: '', userNumber: '', password: '' },

        init() {
            const session = localStorage.getItem('eds-session');
            if (session) {
                try {
                    const parsed = JSON.parse(session);
                    if (parsed.session_id) {
                        window.location.href = '/v7/';
                    }
                } catch (e) {
                    localStorage.removeItem('eds-session');
                }
            }
        },

        validate() {
            this.errors = { districtCode: '', userNumber: '', password: '' };
            let valid = true;
            if (!this.districtCode.trim()) {
                this.errors.districtCode = 'District code is required';
                valid = false;
            }
            if (!this.userNumber.trim()) {
                this.errors.userNumber = 'User number is required';
                valid = false;
            }
            if (!this.password) {
                this.errors.password = 'Password is required';
                valid = false;
            }
            return valid;
        },

        async login() {
            this.errorMessage = '';
            if (!this.validate()) return;

            this.isLoading = true;
            try {
                const response = await fetch(`${API_BASE}/api/auth/login`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        district_code: this.districtCode,
                        user_number: this.userNumber,
                        password: this.password
                    })
                });

                if (!response.ok) {
                    let errMsg = 'Login failed';
                    try { const error = await response.json(); errMsg = error.detail || errMsg; } catch {}
                    throw new Error(errMsg);
                }

                const data = await response.json();
                localStorage.setItem('eds-session', JSON.stringify(data));
                this.password = '';
                window.location.href = '/v7/';
            } catch (error) {
                this.errorMessage = error.message || 'Unable to connect to server';
                this.password = '';
            } finally {
                this.isLoading = false;
            }
        }
    };
}

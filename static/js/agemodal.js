/**
* Initializes age modal functionality.
*/
document.addEventListener('DOMContentLoaded', function () {
    if (!localStorage.getItem('ageVerified')) {
        var ageVerificationModal = new bootstrap.Modal(document.getElementById('ageVerificationModal'));
        ageVerificationModal.show();

        document.getElementById('confirmAge').addEventListener('click', function () {
            localStorage.setItem('ageVerified', 'true');
            ageVerificationModal.hide();
        });
    }
});
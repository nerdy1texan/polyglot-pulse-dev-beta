// Ensure this script is loaded on pages where the spinner is used

document.addEventListener("DOMContentLoaded", function () {
    const spinner = document.getElementById("spinner");
    const forms = document.querySelectorAll("form");

    forms.forEach(form => {
        form.addEventListener("submit", function () {
            if (spinner) {
                spinner.style.display = "block";
            }
        });
    });

    if (spinner) {
        spinner.style.display = "none";
    }
});

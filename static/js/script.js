function validateForm() {

    const inputs = document.querySelectorAll("input");

    for (let input of inputs) {

        if (input.value.trim() === "") {
      r      alert("Please fill in all fields.");
            input.focus();
            return false;
        }

        if (isNaN(input.value)) {
            alert("Please enter a valid number.");
            input.focus();
            return false;
        }
    }

    return true;
}

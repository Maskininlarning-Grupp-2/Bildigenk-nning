var fileTag = document.getElementById("filetag"),
    preview = document.getElementById("preview");

fileTag.addEventListener("change", function() {
    const ext = this.files[0].name.split('.').pop().toLowerCase();
    if (ext === 'jpg' || ext === 'jpeg' || ext === 'png') {
        var reader;

        if (this.files && this.files[0]) {
            reader = new FileReader();

            reader.onload = function(e) {
                preview.setAttribute('src', e.target.result);
            }
            preview.style.display = "block"

            reader.readAsDataURL(this.files[0]);
        }
    } else {
        preview.style.display = "none"
        console.log("Fel filtyp! Endast jpg, jpeg och png är tillåtna.")
    }
});

const form = document.getElementById("evaluateForm");

form.addEventListener("submit", async function(e) {
    e.preventDefault();

    const formData = new FormData();
    formData.append("file", fileTag.files[0]);

    const response = await fetch("/api/evaluate", {
        method: "POST",
        body: formData
    });

    const data = await response.json();
    const resultDiv = document.getElementById("resultDisplay");

    if (data.success) {
        resultDiv.textContent = `This is a ${data.animal}, I'm ${data.accuracy} sure!`;
    } else {
        resultDiv.textContent = data.error;
    }
});
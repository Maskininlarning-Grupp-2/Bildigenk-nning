var fileTag = document.getElementById("filetag"),
    preview = document.getElementById("preview"),
    dropArea = document.getElementById('drop-area'),
    previewBlock = document.getElementById("preview-block"),
    previewText = document.getElementById("textField-preview-block");


fileTag.addEventListener("change", uploadFile) /*{
    const ext = this.files[0].name.split('.').pop().toLowerCase();
    var reader;
    if (this.files && this.files[0]) {
        reader = new FileReader();

        reader.onload = function(e) {
            preview.setAttribute('src', e.target.result);
        }
        preview.style.display = "block"

        reader.readAsDataURL(this.files[0]);
    }

});*/

function uploadFile() {
    var file = fileTag.files[0];
    var fileType = file['type'];
    var validImageTypes = ["image/gif", "image/jpeg", "image/png", "image/webp", "image/avif"];
    if (validImageTypes.includes(fileType)) {
        let imgLink = URL.createObjectURL(file);
        previewBlock.style.backgroundImage = `url(${imgLink})`;
        previewBlock.textContent = "";
    } else {
        fileTag.value = null
        previewBlock.style.backgroundImage = "";
        previewBlock.innerHTML = "<h1>Upload new File</h1><p>Drag and drop or click</p><p>to upload image</p>"
    }
    document.getElementById("resultDisplay").classList.remove('active-animation');
    document.getElementById("resultDisplay").classList.add('inactive-animation');

}

dropArea.addEventListener('dragover', function(e) {
    e.preventDefault();
})

dropArea.addEventListener('drop', function(e) {
    e.preventDefault();
    fileTag.files = e.dataTransfer.files;
    uploadFile();
})

const form = document.getElementById("evaluateForm");

form.addEventListener("submit", async function(e) {
    e.preventDefault();
    document.getElementById("resultDisplay").classList.remove('inactive-animation');
    document.getElementById("resultDisplay").classList.add('active-animation');
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

function closeIt()
{
  fileTag.value = null
  console.log("test")
}

window.onbeforeunload = closeIt;
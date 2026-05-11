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

            reader.readAsDataURL(this.files[0]);
        }
    } else {
        preview.setAttribute('src', "")
        this.value = ""
        console.log("Fel filtyp! Endast jpg, jpeg och png är tillåtna.")
    }
});
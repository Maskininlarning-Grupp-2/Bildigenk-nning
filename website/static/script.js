var fileTag = document.getElementById("filetag"),
    preview = document.getElementById("preview");

fileTag.addEventListener("change", function() {
    console.log(this.files[0].name.split('.')[1])
    if (this.files[0].name.split('.')[1] == 'jpg') {
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
        console.log("I'll give this a proper message later but for now: Wrong File Type :D")
    }
});

function evaluateAnimal() {
    /*$.ajax({
        type: 'POST',
        url: '../test.py',
        dataType: 'image/jpg',
        success: function(data) {
        }
    })*/
    const writable = fileTag.files[0].createWritable();
    writable.write();
    writable.close();
    console.log(fileTag.files[0].name.split('.')[1])
}
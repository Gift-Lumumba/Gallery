function copyLink() {
  var copyText = document.getElementById("copyimagelink");

  copyText.select();

  document.execCommand("copy");

  alert("Image link has been successfully copied: " + copyText.value);
}
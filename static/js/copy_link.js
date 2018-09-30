// function copyLink(value) {
//   console.log('copied link')
//   function handler(event){
//     event.clipboardData.setData('text/plain', value);
//     event.preventDefault();
//     document.removeEventListener('copy', handler, true);
//   }
//   document.addEventListener('copy', handler, true);
//   document.execCommand('copy');
  
//   alert("Image link has been successfully copied: " + copyLink.value);
// }
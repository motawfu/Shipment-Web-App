function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

const bgColorInput = document.querySelector('#level');
const submit =document.getElementsById('click');

submit.addEventListener('click', function() {
  const bgColorInput = document.getElementById('bgcolor').value;
  bgColorInput.style.backgroundColor = bgColorInput;
});
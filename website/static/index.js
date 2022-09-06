function delete_note(note_id){
    fetch('/delete-note', {
    method : "POST",
    body : JSON.stringify({noteId : note_id})
}).then((_res) =>{
    window.location.href = "/";
    });
}

function copytext(button) {
    const text = document.getElementById('copyValue').value;
    navigator.clipboard.writeText(text)
        .then(() => {
            button.innerText = 'Copied';
            setTimeout(() => button.innerText = 'Copy', 2000);
        })
        .catch(err => {
            console.error('Gagal copy: ', err);
        });
}

const loaderText = document.getElementById("loaderText");
const letters = "LOADING";

letters.split("").forEach((char, index) => {
    const span = document.createElement("span");
    span.textContent = char;
    span.style.setProperty("--i", index);
    loaderText.appendChild(span);
})
const nav = document.querySelector("nav");
const links = document.querySelectorAll("nav a");
const underline = document.querySelector(".underline");

// set underline ke posisi link yang active
const activeLink = document.querySelector("nav a.active");
underline.style.width = activeLink.offsetWidth + "px";
underline.style.left = activeLink.offsetLeft + "px";

links.forEach(link => {
  link.addEventListener("mouseenter", e => {
    underline.style.width = e.target.offsetWidth + "px";
    underline.style.left = e.target.offsetLeft + "px";
  });
  link.addEventListener("mouseleave", () => {
    underline.style.width = activeLink.offsetWidth + "px";
    underline.style.left = activeLink.offsetLeft + "px";
  });
});
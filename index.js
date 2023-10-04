const background = document.getElementById("introduction");
const aboutMe = document.getElementById("about-me-btn");
const aboutMeContent = document.getElementById("about-me-content");

const aboutMeDiv = document.getElementById("about-me");

const aboutMeGM = document.getElementById("about-me-gamemaker");
const aboutMePhotography = document.getElementById("about-me-photography");
const aboutMeRust = document.getElementById("about-me-rust");


aboutMe.addEventListener("click", ev => {
    aboutMeDiv.scrollIntoView({
        behavior: "smooth"
    });
});

background.style.opacity = 1;



let options = {
    root: document.querySelector("#scrollArea"),
    rootMargin: "0px",
    threshold: 0.5,
};

let opacityObserver = new IntersectionObserver((entries, _) => {
    entries.forEach(entry => {
        console.log(entry);
        entry.target.style.opacity = (entry.isIntersecting || entry.boundingClientRect.y < 0) ? 1 : 0;

    });
}, options);

opacityObserver.observe(aboutMeGM);
opacityObserver.observe(aboutMePhotography);
opacityObserver.observe(aboutMeRust);

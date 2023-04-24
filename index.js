const greetings = [
    "Hey!", 
    "Hiya!", 
    "Hello!", 
    "Hé!", 
    "Hallo!", 
    "Ahoj!", 
    "Salut!",
    "Hei!",
    "Hej!",
    "¡Hola!",
    "Servus!",
    "Bëgnudüs!",
    "Здравствуйте",
    "Сәлем",
    "こんにちわ",
    "Привіт"
];

const links = document.getElementById("links");
const about = document.getElementsByClassName("link")[0];
const games = document.getElementsByClassName("link")[1];
const articleAboutMe = document.getElementById("aboutme");
const greeting = document.getElementById("greeting");
const articleGames = document.getElementById("games");
const arrow = document.getElementById("back");

const random = max => Math.floor(Math.random() * max);

const randomGreeting = () => greeting.innerHTML = greetings[random(greetings.length)];

const reset = () => {
    about.dataset.focus = "none";
    games.dataset.focus = "none";
};

const disabled = () => links.dataset.moveleft == "yes";

about.addEventListener("mouseover", event => {
    if (disabled()) return;
    event.target.dataset.focus = "yes";
    games.dataset.focus = "no";
});

games.addEventListener("mouseover", event => {
    if (disabled()) return;
    event.target.dataset.focus = "yes";
    about.dataset.focus = "no";
});


about.addEventListener("click", event => {
    if (disabled()) return;
    links.dataset.moveleft = "yes";
    articleAboutMe.dataset.visible = "yes";
    arrow.dataset.visible = "yes";
    randomGreeting();
});

games.addEventListener("click", event => {
    if (disabled()) return;
    links.dataset.moveleft = "yes";
    articleGames.dataset.visible = "yes";
    arrow.dataset.visible = "yes";
});

arrow.addEventListener("click", event => {
    articleAboutMe.dataset.visible = "no";
    articleGames.dataset.visible = "no";
    arrow.dataset.visible = "no";
    links.dataset.moveleft = "no";
});


games.addEventListener("mouseleave", reset);
about.addEventListener("mouseleave", reset);

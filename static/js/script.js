document.addEventListener("DOMContentLoaded", function(){
    const cards = document.querySelectorAll(".info-card,.project-card,.team-card");
    cards.forEach((card, index) => {
        card.style.opacity = "0";
        card.style.transform = "translateY(25px)";
        setTimeout(() => {
            card.style.transition = "0.6s ease";
            card.style.opacity = "1";
            card.style.transform = "translateY(0)";
        }, index * 90);
    });
});

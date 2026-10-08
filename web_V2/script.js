document.documentElement.classList.add("js");

const menuToggle = document.querySelector(".menu-toggle");
const siteNav = document.querySelector(".site-nav");

function closeMenu() {
    menuToggle.setAttribute("aria-expanded", "false");
    menuToggle.setAttribute("aria-label", "Abrir menú");
    siteNav.classList.remove("is-open");
}

menuToggle.addEventListener("click", () => {
    const isOpen = menuToggle.getAttribute("aria-expanded") === "true";
    menuToggle.setAttribute("aria-expanded", String(!isOpen));
    menuToggle.setAttribute("aria-label", isOpen ? "Abrir menú" : "Cerrar menú");
    siteNav.classList.toggle("is-open", !isOpen);
});

siteNav.addEventListener("click", (event) => {
    if (event.target.closest("a")) {
        closeMenu();
    }
});

document.querySelector("#current-year").textContent = new Date().getFullYear();

const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
const revealElements = document.querySelectorAll(
    ".intro-grid, .intro-logo, .features-top, .feature-card, .features-disclaimer, " +
    ".screenshots-heading, .screenshot-card, .project-image-wrap, .project-copy, .footer-inner"
);

if (reducedMotion.matches || !("IntersectionObserver" in window)) {
    revealElements.forEach((element) => element.classList.add("is-visible"));
} else {
    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add("is-visible");
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.12, rootMargin: "0px 0px -35px 0px" });

    revealElements.forEach((element) => {
        element.classList.add("reveal");
        revealObserver.observe(element);
    });
}

const carousel = document.querySelector(".hero-carousel");
const slides = [...carousel.querySelectorAll(".carousel-slide")];
const dots = [...carousel.querySelectorAll(".carousel-dots button")];
const captionPrimary = document.querySelector(".caption-primary");
const captionHighlight = document.querySelector(".caption-highlight");
const pauseButton = carousel.querySelector(".carousel-pause");
const previousButton = carousel.querySelector(".carousel-previous");
const nextButton = carousel.querySelector(".carousel-next");
let activeSlide = 0;
let rotationPaused = reducedMotion.matches;
let pointerIsOver = false;
let rotationTimer;
let swipeStartX;

function updateSlide(index) {
    activeSlide = (index + slides.length) % slides.length;

    slides.forEach((slide, slideIndex) => {
        const isActive = slideIndex === activeSlide;
        slide.classList.toggle("is-active", isActive);
        slide.setAttribute("aria-hidden", String(!isActive));
        slide.setAttribute("aria-label", `${slideIndex + 1} de ${slides.length}`);
        dots[slideIndex].setAttribute("aria-current", String(isActive));
    });

    captionPrimary.textContent = slides[activeSlide].dataset.caption;
    captionHighlight.textContent = slides[activeSlide].dataset.highlight;
    captionPrimary.parentElement.classList.remove("is-changing");
    void captionPrimary.parentElement.offsetWidth;
    captionPrimary.parentElement.classList.add("is-changing");
}

function updateRotation() {
    window.clearInterval(rotationTimer);
    rotationTimer = undefined;
    pauseButton.setAttribute("aria-pressed", String(rotationPaused));
    pauseButton.setAttribute("aria-label", rotationPaused ? "Reanudar rotación" : "Pausar rotación");
    pauseButton.textContent = rotationPaused ? "▶" : "Ⅱ";

    if (!rotationPaused && !pointerIsOver && !document.hidden) {
        rotationTimer = window.setInterval(() => {
            updateSlide(activeSlide + 1);
        }, 5000);
    }
}

previousButton.addEventListener("click", () => updateSlide(activeSlide - 1));
nextButton.addEventListener("click", () => updateSlide(activeSlide + 1));

dots.forEach((dot, index) => {
    dot.addEventListener("click", () => updateSlide(index));
});

pauseButton.addEventListener("click", () => {
    rotationPaused = !rotationPaused || reducedMotion.matches;
    updateRotation();
});

carousel.addEventListener("mouseenter", () => {
    pointerIsOver = true;
    updateRotation();
});

carousel.addEventListener("mouseleave", () => {
    pointerIsOver = false;
    updateRotation();
});

carousel.querySelector(".carousel-track").addEventListener("pointerdown", (event) => {
    swipeStartX = event.clientX;
});

carousel.querySelector(".carousel-track").addEventListener("pointerup", (event) => {
    if (swipeStartX === undefined) {
        return;
    }

    const swipeDistance = event.clientX - swipeStartX;
    swipeStartX = undefined;

    if (Math.abs(swipeDistance) >= 45) {
        updateSlide(activeSlide + (swipeDistance < 0 ? 1 : -1));
    }
});

carousel.querySelector(".carousel-track").addEventListener("pointercancel", () => {
    swipeStartX = undefined;
});

document.addEventListener("visibilitychange", updateRotation);
reducedMotion.addEventListener("change", (event) => {
    rotationPaused = event.matches;
    updateRotation();
});

updateRotation();

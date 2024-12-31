document.addEventListener("DOMContentLoaded", () => {
  // Animación del encabezado
  gsap.from(".header", {
    duration: 1,
    y: -100,
    opacity: 0,
    ease: "bounce.out",
  });

  // Animación de las tarjetas
  gsap.from(".card", {
    duration: 1,
    scale: 0,
    opacity: 0,
    stagger: 0.2,
    ease: "elastic.out(1, 0.5)",
  });
});

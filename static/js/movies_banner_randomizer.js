document.addEventListener("DOMContentLoaded", () => {
  // Lista de banners de películas en la carpeta "images"
  const banners = [
    "/static/images/movie_banner1.png",
    "/static/images/movie_banner2.png",
    "/static/images/movie_banner3.png",
    "/static/images/movie_banner4.png",
    "/static/images/movie_banner5.png",
    "/static/images/movie_banner6.png",
    "/static/images/movie_banner7.png",
    "/static/images/movie_banner8.png",
    "/static/images/movie_banner9.png",
    "/static/images/movie_banner10.png",
  ];

  // Pre-cargar todas las imágenes
  banners.forEach((src) => {
    const img = new Image();
    img.src = src;
  });

  // Seleccionar un banner aleatorio
  const randomBanner = banners[Math.floor(Math.random() * banners.length)];

  // Establecer el banner aleatorio
  const bannerElement = document.getElementById("random-banner");
  if (bannerElement) {
    bannerElement.src = randomBanner;

    // Ajustar todos los banners al tamaño del primero
    bannerElement.onload = () => {
      const width = bannerElement.offsetWidth;
      const height = bannerElement.offsetHeight;

      const allBanners = document.querySelectorAll(".img-fluid");
      allBanners.forEach((img) => {
        img.style.width = `${width}px`;
        img.style.height = `${height}px`;
      });
    };
  }
});

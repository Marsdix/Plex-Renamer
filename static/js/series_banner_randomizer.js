document.addEventListener("DOMContentLoaded", () => {
  // Lista de banners de series en la carpeta "images"
  const banners = [
    "/static/images/series_banner1.png",
    "/static/images/series_banner2.png",
    "/static/images/series_banner3.png",
    "/static/images/series_banner4.png",
    "/static/images/series_banner5.png",
    "/static/images/series_banner6.png",
    "/static/images/series_banner7.png",
    "/static/images/series_banner8.png",
    "/static/images/series_banner9.png",
    "/static/images/series_banner10.png",
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
  }
  // Asegurar que todos los banners mantengan el mismo tamaño
  bannerElement.onload = () => {
    const width = bannerElement.offsetWidth;
    const height = bannerElement.offsetHeight;

    // Ajustar todos los banners al tamaño del primero
    const allBanners = document.querySelectorAll(".img-fluid");
    allBanners.forEach((img) => {
      img.style.width = `${width}px`;
      img.style.height = `${height}px`;
    });
  };
});

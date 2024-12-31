document.addEventListener("DOMContentLoaded", () => {
  // Lista de todas las imágenes a precargar
  const images = [
    // Icons
    "/static/icons/documentaries.png",
    "/static/icons/edit.png",
    "/static/icons/extras.png",
    "/static/icons/favicon.ico",
    "/static/icons/info.png",
    "/static/icons/movies.png",
    "/static/icons/tv.png",

    // Images
    "/static/images/documentaries_background.png",
    "/static/images/documentary_banner1.png",
    "/static/images/documentary_banner2.png",
    "/static/images/documentary_banner3.png",
    "/static/images/documentary_banner4.png",
    "/static/images/documentary_banner5.png",
    "/static/images/documentary_banner6.png",
    "/static/images/documentary_banner7.png",
    "/static/images/documentary_banner8.png",
    "/static/images/documentary_banner9.png",
    "/static/images/documentary_banner10.png",
    "/static/images/index_background.png",
    "/static/images/index_background2.png",
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
    "/static/images/movies_background.png",
    "/static/images/series_background.png",
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
    "/static/images/extras_background.png",
    "/static/images/info_background.png",
    "/static/images/renombrar_series_background.png",
    "/static/images/success_background.png",
  ];

  // Pre-cargar cada imagen
  images.forEach((src) => {
    const img = new Image();
    img.src = src;
  });

  console.log("Todas las imágenes han sido precargadas.");
});

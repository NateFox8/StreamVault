var swiper = new Swiper(".mySwiper", {
    spaceBetween: 10,
    slidesPerView: 1,
    centeredSlides: true,

    autoplay: {
        delay: 5000,
    },


    breakpoints: {
        480: {
            centeredSlides: false,
            spaceBetween: 10,
            slidesPerView: 1,
        },

        780: {
            centeredSlides: false,
            spaceBetween: 30,
            slidesPerView: 3,

        },

        1024: {
            centeredSlides: false,
            spaceBetween: 40,
            slidesPerView: 5,
        },


        2048: {
            centeredSlides: false,
            slidesPerView: 8,
        },
      },
});